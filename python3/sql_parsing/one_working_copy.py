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
        alias_map[from_clause] = from_clause
    elif isinstance(from_clause, dict):
        # Single join or table with alias
        # Example: {"value": "table", "name": "alias"}
        if 'value' in from_clause:
            table_name = from_clause['value']
            alias = from_clause.get('name', table_name)
            alias_map[alias] = table_name
        else:
            # Possibly join dict
            for key, val in from_clause.items():
                if key.endswith('join') and isinstance(val, dict):
                    alias_map.update(extract_source_tables(val))
    elif isinstance(from_clause, list):
        for item in from_clause:
            if isinstance(item, dict):
                # Join or table with alias
                if 'value' in item:
                    table_name = item['value']
                    alias = item.get('name', table_name)
                    alias_map[alias] = table_name
                else:
                    # Join dict
                    for key, val in item.items():
                        if key.endswith('join') and isinstance(val, dict):
                            alias_map.update(extract_source_tables(val))
            elif isinstance(item, str):
                alias_map[item] = item
    return alias_map

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
        # Check for known transformation keys
        for key, val in value.items():
            if key in ('literal', 'current_timestamp'):
                # No source column
                continue
            elif isinstance(val, list):
                for item in val:
                    columns.extend(extract_columns_from_value(item))
            else:
                columns.extend(extract_columns_from_value(val))
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
        else:
            return col
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

def process_select_item(
    sel_item: Union[Dict[str, Any], str], 
    source_tables: Dict[str, str],
    target_table: str,
    target_col: str = None
) -> List[Tuple[str, str, str]]:
    """
    Process a single select item and generate lineage entries.
    """
    lineage = []
    src_cols = []
    transformation = ""
    
    # Determine source columns and transformation
    if isinstance(sel_item, dict):
        val = sel_item.get('value')
        if val is not None:
            src_cols = extract_columns_from_value(val)
            if isinstance(val, dict):
                try:
                    transformation = format(val)
                except Exception:
                    transformation = json.dumps(val)
            elif isinstance(val, str):
                transformation = ""
        else:
            src_cols = []
    elif isinstance(sel_item, str):
        src_cols = [sel_item]
        transformation = ""
    
    # Use source column name if target column is not provided
    if target_col is None and isinstance(sel_item, dict):
        target_col = sel_item.get('name')
        if target_col is None:
            val = sel_item.get('value')
            if isinstance(val, str):
                target_col = val
    
    for src_col in src_cols:
        src_col_norm = normalize_column(src_col)
        if '.' in src_col_norm:
            alias, col = src_col_norm.split('.', 1)
            table = source_tables.get(alias, alias)
        else:
            col = src_col_norm
            if len(source_tables) == 1:
                table = list(source_tables.values())[0]
            else:
                found_table = None
                for alias_key, table_name in source_tables.items():
                    if col in table_name:
                        found_table = table_name
                        break
                if found_table:
                    table = found_table
                else:
                    table = "unknown_table"
        
        source_full = f"{table}.{col}"
        tgt_col_replaced = target_col.split('.', 1)[-1] if target_col and '.' in target_col else target_col
        target_full = f"{target_table}.{tgt_col_replaced}" if tgt_col_replaced else f"{target_table}.unknown_column"
        transformation_replaced = replace_aliases_with_tables_in_transformation(transformation, source_tables)
        lineage.append((source_full, target_full, transformation_replaced))
    
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
    source_tables = {}
    
    if 'from' in select_query:
        source_tables = extract_source_tables(select_query['from'])
    
    select_items = select_query.get('select', [])
    
    for idx, sel_item in enumerate(select_items):
        tgt_col = None
        if target_columns and idx < len(target_columns):
            tgt_col = target_columns[idx]
        
        item_lineage = process_select_item(sel_item, source_tables, target_table, tgt_col)
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

    explicit_target_columns = 'columns' in query_obj and isinstance(query_obj['columns'], list)
    target_columns = []
    if explicit_target_columns:
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