import json
import re
from typing import List, Tuple, Dict, Any, Union
from mo_sql_parsing import format

def load_json(path: str) -> List[Dict[str, Any]]:
    with open(path, 'r') as f:
        return json.load(f)

def extract_source_tables(from_clause: Union[str, List, Dict]) -> Dict[str, str]:
    """
    Extract alias to table mapping from the from clause.
    Returns dict alias -> full_table_name.
    If no alias, table name maps to itself.
    """
    alias_map = {}
    
    if isinstance(from_clause, str):
        # Handle variable substitution in table names
        table_name = from_clause
        alias_map[table_name] = table_name
    elif isinstance(from_clause, dict):
        # Single join or table with alias
        if 'value' in from_clause and 'name' in from_clause:
            table_name = from_clause['value']
            alias = from_clause['name']
            
            # If value is a nested query, track its output as a table
            if isinstance(table_name, dict) and 'select' in table_name:
                alias_map[alias] = alias  # Use alias as table name for derived tables
            else:
                alias_map[alias] = table_name
        elif 'value' in from_clause:
            table_name = from_clause['value']
            alias_map[table_name] = table_name
        else:
            # Various join types
            for join_type, join_value in from_clause.items():
                if isinstance(join_value, dict):
                    alias_map.update(extract_source_tables(join_value))
    elif isinstance(from_clause, list):
        # Multiple FROM items
        for item in from_clause:
            if isinstance(item, str):
                alias_map[item] = item
            elif isinstance(item, dict):
                alias_map.update(extract_source_tables(item))
    
    return alias_map

def extract_subquery_columns(subquery: Dict[str, Any]) -> List[str]:
    """
    Extract output column names from a subquery.
    """
    if not isinstance(subquery, dict):
        return []
    
    select_clause = subquery.get('select', {})
    columns = []
    
    if isinstance(select_clause, dict):
        # Single column with potential alias
        col_name = select_clause.get('name')
        if col_name:
            columns.append(col_name)
    elif isinstance(select_clause, list):
        # Multiple columns
        for item in select_clause:
            if isinstance(item, dict) and 'name' in item:
                columns.append(item['name'])
            elif isinstance(item, dict) and 'value' in item and isinstance(item['value'], str):
                columns.append(item['value'])
            elif isinstance(item, str):
                columns.append(item)
    
    return columns

def extract_columns_from_value(value: Any) -> List[str]:
    """
    Extract source columns from a select value.
    Returns list of strings like alias.column or column.
    Handles nested dicts for transformations.
    """
    columns = []
    
    if isinstance(value, str):
        columns.append(value)
    elif isinstance(value, dict):
        # Check for literals and functions that don't reference columns
        if 'literal' in value or 'current_timestamp' in value or 'current_date' in value:
            return []
        
        # Handle OVER clauses separately to extract window function columns
        if 'over' in value:
            over_clause = value.get('over', {})
            order_by = over_clause.get('orderby', [])
            partition_by = over_clause.get('partitionby', [])
            
            # Process ORDER BY columns
            if isinstance(order_by, list):
                for item in order_by:
                    if isinstance(item, dict) and 'value' in item:
                        columns.append(item['value'])
                    elif isinstance(item, str):
                        columns.append(item)
            
            # Process PARTITION BY columns
            if isinstance(partition_by, list):
                for item in partition_by:
                    if isinstance(item, dict) and 'value' in item:
                        columns.append(item['value'])
                    elif isinstance(item, str):
                        columns.append(item)
            
            # Process the main value
            if 'value' in value:
                columns.extend(extract_columns_from_value(value['value']))
        
        # Process other function types and operators
        for key, val in value.items():
            if key in ('trim', 'substr', 'add', 'coalesce', 'max', 'min', 'sum', 'avg', 'count'):
                if isinstance(val, list):
                    for item in val:
                        columns.extend(extract_columns_from_value(item))
                else:
                    columns.extend(extract_columns_from_value(val))
            elif isinstance(val, list):
                for item in val:
                    columns.extend(extract_columns_from_value(item))
            elif isinstance(val, dict):
                columns.extend(extract_columns_from_value(val))
            elif isinstance(val, str):
                columns.append(val)
    
    return columns

def normalize_column(col: str) -> str:
    """
    Normalize column string to alias.column or column.
    """
    if isinstance(col, str):
        return col.strip()
    return str(col)

def replace_alias_with_table_in_column(col: str, source_tables: Dict[str, str]) -> str:
    """
    Replace alias prefix in column with full table name if alias exists in source_tables.
    E.g. 'a.UserGroup' with source_tables={'a': 'Analytics.ReportData'} -> 'Analytics.ReportData.UserGroup'
    """
    if '.' in col:
        alias, col_name = col.split('.', 1)
        full_table = source_tables.get(alias)
        if full_table:
            return f"{full_table}.{col_name}"
    return col

def replace_aliases_with_tables_in_transformation(transformation: str, source_tables: Dict[str, str]) -> str:
    """
    Replace alias prefixes in transformation SQL string with full table names.
    E.g. replace 'a.UserGroup' with 'Analytics.ReportData.UserGroup'
    """
    def replacer(match):
        alias = match.group(1)
        col = match.group(2)
        full_table = source_tables.get(alias)
        if full_table:
            return f"{full_table}.{col}"
        else:
            return match.group(0)

    pattern = re.compile(r'\b(\w+)\.(\w+)')
    return pattern.sub(replacer, transformation)

def find_table_for_column(column: str, source_tables: Dict[str, str], subquery_columns: Dict[str, List[str]]) -> str:
    """
    Find the source table for a given column.
    First tries to match by alias prefix, then by checking if the column exists in a subquery's output.
    """
    # If column has alias prefix, use it
    if '.' in column:
        alias, col_name = column.split('.', 1)
        if alias in source_tables:
            return source_tables[alias]
        return alias  # Use the alias as is if not found in source_tables
    
    # Check if the column is from a subquery output
    for alias, columns in subquery_columns.items():
        if column in columns:
            return alias
    
    # Default to the first table if there's only one
    if len(source_tables) == 1:
        return list(source_tables.values())[0]
    
    # Try to find in table name
    for table_name in source_tables.values():
        if column.upper() in table_name.upper():
            return table_name
    
    # Default case
    return "unknown_table"

def process_subqueries_in_from(from_clause: Union[Dict[str, Any], List, str]) -> Dict[str, List[str]]:
    """
    Process subqueries in FROM clause to extract their output columns.
    Returns a mapping of alias -> [column names]
    """
    subquery_columns = {}
    
    if isinstance(from_clause, dict):
        if 'value' in from_clause and 'name' in from_clause and isinstance(from_clause['value'], dict):
            # This is a subquery with an alias
            subquery = from_clause['value']
            alias = from_clause['name']
            
            if 'select' in subquery:
                subquery_columns[alias] = extract_subquery_columns(subquery)
        else:
            # Process joins
            for join_type, join_clause in from_clause.items():
                if isinstance(join_clause, dict):
                    subquery_columns.update(process_subqueries_in_from(join_clause))
    
    elif isinstance(from_clause, list):
        # Multiple FROM items
        for item in from_clause:
            if isinstance(item, dict):
                subquery_columns.update(process_subqueries_in_from(item))
    
    return subquery_columns

def process_select_item(
    sel_item: Union[Dict[str, Any], str], 
    source_tables: Dict[str, str],
    subquery_columns: Dict[str, List[str]],
    target_table: str,
    target_col: str = None
) -> List[Tuple[str, str, str]]:
    """
    Process a single select item and generate lineage entries.
    """
    lineage = []
    
    # Handle case when sel_item is a string
    if isinstance(sel_item, str):
        src_col = sel_item
        src_table = find_table_for_column(src_col, source_tables, subquery_columns)
        
        # Use the column name itself as target column if not provided
        tgt_col = target_col if target_col else src_col
        if '.' in tgt_col:
            tgt_col = tgt_col.split('.', 1)[1]  # Remove table prefix
        
        source_full = f"{src_table}.{src_col}" if '.' not in src_col else src_col
        target_full = f"{target_table}.{tgt_col}"
        
        lineage.append((source_full, target_full, ""))
        return lineage
    
    # Handle dictionary case
    if not isinstance(sel_item, dict):
        return lineage
    
    # Get target column name
    tgt_col = sel_item.get('name', target_col)
    if not tgt_col and 'value' in sel_item and isinstance(sel_item['value'], str):
        tgt_col = sel_item['value']
    
    if not tgt_col:
        return lineage  # Skip if we can't determine target column
    
    # Extract source columns and transformation
    src_cols = []
    transformation = ""
    
    if 'value' in sel_item:
        value = sel_item['value']
        
        # Handle literal values or constants
        if isinstance(value, dict) and ('literal' in value or 'current_timestamp' in value or 'current_date' in value):
            source_expr = json.dumps(value)
            source_full = f"CONSTANT.{source_expr}"
            target_full = f"{target_table}.{tgt_col}"
            try:
                transformation = format(value)
            except:
                transformation = json.dumps(value)
            
            lineage.append((source_full, target_full, transformation))
            return lineage
        
        # Extract columns from the value expression
        src_cols = extract_columns_from_value(value)
        
        # Generate transformation string
        if isinstance(value, dict):
            try:
                transformation = format(value)
            except:
                transformation = json.dumps(value)
    
    # Create lineage entries for each source column
    for src_col in src_cols:
        src_col_norm = normalize_column(src_col)
        
        # Find the source table
        if '.' in src_col_norm:
            alias, col = src_col_norm.split('.', 1)
            table = source_tables.get(alias, alias)
        else:
            table = find_table_for_column(src_col_norm, source_tables, subquery_columns)
        
        source_full = f"{table}.{col}" if '.' in src_col_norm else f"{table}.{src_col_norm}"
        target_full = f"{target_table}.{tgt_col}"
        
        # Replace aliases in transformation
        transformation_replaced = replace_aliases_with_tables_in_transformation(transformation, source_tables)
        
        lineage.append((source_full, target_full, transformation_replaced))
    
    # If no source columns were found but we have a transformation, add a lineage entry with just the transformation
    if not src_cols and transformation:
        source_full = "EXPRESSION.value"
        target_full = f"{target_table}.{tgt_col}"
        lineage.append((source_full, target_full, transformation))
    
    return lineage

def build_lineage_from_select_query(
    select_query: Dict[str, Any],
    target_table: str,
    target_columns: List[str] = None
) -> List[Tuple[str, str, str]]:
    """
    Build lineage from a single SELECT query.
    """
    lineage = []
    
    # Extract source tables and their aliases
    source_tables = {}
    if 'from' in select_query:
        source_tables = extract_source_tables(select_query['from'])
    
    # Process subqueries to extract their output columns
    subquery_columns = {}
    if 'from' in select_query:
        subquery_columns = process_subqueries_in_from(select_query['from'])
    
    # Process each select item
    select_items = select_query.get('select', [])
    if not isinstance(select_items, list):
        select_items = [select_items]
    
    for idx, sel_item in enumerate(select_items):
        tgt_col = None
        if target_columns and idx < len(target_columns):
            tgt_col = target_columns[idx]
        
        item_lineage = process_select_item(sel_item, source_tables, subquery_columns, target_table, tgt_col)
        lineage.extend(item_lineage)
    
    return lineage

def extract_select_queries_from_set_operation(
    query_obj: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """
    Extract all SELECT queries from a set operation (UNION, UNION ALL, INTERSECT, EXCEPT).
    """
    select_queries = []
    
    for set_op in ['union', 'union_all', 'intersect', 'except']:
        if set_op in query_obj:
            for subquery in query_obj[set_op]:
                if 'select' in subquery:
                    select_queries.append(subquery)
                else:
                    # Recursive handling for nested set operations
                    select_queries.extend(extract_select_queries_from_set_operation(subquery))
    
    return select_queries

def build_lineage_for_insert(
    query_obj: Dict[str, Any]
) -> List[Tuple[str, str, str]]:
    """
    Build lineage for insert queries.
    """
    lineage = []
    target_table = query_obj.get('insert')
    if not target_table:
        return lineage

    target_columns = []
    if 'columns' in query_obj and isinstance(query_obj['columns'], list):
        target_columns = query_obj['columns']
    
    # Check if the query involves a set operation
    if 'query' in query_obj:
        query = query_obj['query']
        
        for set_op in ['union', 'union_all', 'intersect', 'except']:
            if set_op in query:
                # Extract all SELECT queries from the set operation
                select_queries = extract_select_queries_from_set_operation(query)
                
                # Build lineage for each SELECT query
                for select_query in select_queries:
                    lineage.extend(build_lineage_from_select_query(select_query, target_table, target_columns))
                
                return lineage
        
        # Simple SELECT query
        if 'select' in query:
            lineage.extend(build_lineage_from_select_query(query, target_table, target_columns))
    
    return lineage

def build_lineage_for_create_table(
    query_obj: Dict[str, Any]
) -> List[Tuple[str, str, str]]:
    """
    Build lineage for create table queries.
    """
    lineage = []
    create_table_obj = query_obj.get('create table')
    if not create_table_obj:
        return lineage

    target_table = create_table_obj.get('name')
    if not target_table:
        return lineage

    target_columns = []
    if 'columns' in query_obj and isinstance(query_obj['columns'], list):
        target_columns = query_obj['columns']
    
    if 'query' in create_table_obj:
        query = create_table_obj['query']
        
        for set_op in ['union', 'union_all', 'intersect', 'except']:
            if set_op in query:
                # Extract all SELECT queries from the set operation
                select_queries = extract_select_queries_from_set_operation(query)
                
                # Build lineage for each SELECT query
                for select_query in select_queries:
                    lineage.extend(build_lineage_from_select_query(select_query, target_table, target_columns))
                
                return lineage
        
        # Simple SELECT query
        if 'select' in query:
            lineage.extend(build_lineage_from_select_query(query, target_table, target_columns))
    
    return lineage

def build_lineage(
    parsed_json: List[Dict[str, Any]]
) -> List[Tuple[str, str, str]]:
    """
    Build column-level lineage as list of tuples:
    (source_db.table.column, target_db.table.column, transformation)
    """
    lineage = []
    for query_obj in parsed_json:
        if 'insert' in query_obj:
            lineage.extend(build_lineage_for_insert(query_obj))
        elif 'create table' in query_obj:
            lineage.extend(build_lineage_for_create_table(query_obj))
    return lineage

def main():
    parsed_json = load_json('sql_to_json.json')
    lineage = build_lineage(parsed_json)
    for src, tgt, trans in lineage:
        print(f"({src}, {tgt}, {trans})")

if __name__ == "__main__":
    main()