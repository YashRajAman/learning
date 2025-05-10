
from mo_sql_parsing import parse
from typing import List, Tuple, Optional
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_fully_qualified_name(col: str, table_aliases: dict, default_db: str = None, default_table: str = None) -> str:
    """Construct a fully qualified column name (e.g., database.table.column) from parsed JSON."""
    logging.debug(f"Processing column: {col}")
    if not col:
        return ""
    parts = col.split('.')
    if len(parts) == 1:
        if default_table:
            return f"{default_table}.{col}"
        return col
    elif len(parts) == 2:
        table, column = parts
        if table in table_aliases:
            return f"{table_aliases[table]}.{column}"
        return f"{table}.{column}"
    elif len(parts) == 3:
        return col
    return col

def reconstruct_transformation(expr: dict, table_aliases: dict, default_db: str = None, default_table: str = None) -> str:
    """Reconstruct transformation expression as a string, resolving column names."""
    logging.debug(f"Reconstructing transformation: {expr}")
    if not isinstance(expr, dict):
        return str(expr)
    
    for key, value in expr.items():
        if key == 'literal':
            return f"literal({value})"
        elif key in ['concat', 'substr', 'upper', 'trim', 'cast', 'coalesce']:
            if isinstance(value, list):
                args = [reconstruct_transformation(v, table_aliases, default_db, default_table) if isinstance(v, dict) else get_fully_qualified_name(v, table_aliases, default_db, default_table) if isinstance(v, str) else str(v) for v in value]
                return f"{key}({', '.join(args)})"
            elif isinstance(value, dict):
                return f"{key}({reconstruct_transformation(value, table_aliases, default_db, default_table)})"
        elif isinstance(value, list):
            return ', '.join(reconstruct_transformation(v, table_aliases, default_db, default_table) for v in value)
        elif isinstance(value, dict):
            return reconstruct_transformation(value, table_aliases, default_db, default_table)
    return str(expr)

def extract_table_aliases(from_clause: list) -> dict:
    """Extract table aliases and their fully qualified names from the FROM clause."""
    aliases = {}
    logging.debug(f"Extracting aliases from: {from_clause}")
    for item in from_clause:
        if isinstance(item, dict):
            if 'value' in item and 'name' in item:
                value = item['value']
                alias = item['name']
                aliases[alias] = value if isinstance(value, str) else '.'.join(value)
            elif 'inner join' in item or 'left outer join' in item:
                join_type = 'inner join' if 'inner join' in item else 'left outer join'
                join = item[join_type]
                if isinstance(join, dict) and 'value' in join and 'name' in join:
                    value = join['value']
                    alias = join['name']
                    aliases[alias] = value if isinstance(value, str) else '.'.join(value)
    logging.debug(f"Table aliases: {aliases}")
    return aliases

def get_target_column_name(select_item: dict) -> str:
    """Determine the target column name from a SELECT item."""
    if 'name' in select_item:
        return select_item['name']  # Use alias, e.g., SegmentInfo
    elif 'value' in select_item and isinstance(select_item['value'], str):
        parts = select_item['value'].split('.')
        return parts[-1]  # Use column name, e.g., UserGroup from a.UserGroup
    elif 'all_columns' in select_item:
        return '*'  # Wildcard
    return 'unknown'  # Fallback for complex expressions

def extract_columns(select_clause: list, table_aliases: dict, default_db: str = None, default_table: str = None) -> List[dict]:
    """Extract columns from SELECT clause, including transformations."""
    columns = []
    logging.debug(f"Extracting columns from: {select_clause}")
    for col in select_clause:
        col_info = {}
        if isinstance(col, dict):
            if 'name' in col:
                col_info['name'] = col['name']
            if 'all_columns' in col:
                col_info['source'] = '*'
                columns.append(col_info)
                continue
            if 'value' in col:
                if isinstance(col['value'], str):
                    col_info['source'] = get_fully_qualified_name(col['value'], table_aliases, default_db, default_table)
                elif isinstance(col['value'], dict):
                    col_info['source'] = []
                    col_info['transformation'] = reconstruct_transformation(col['value'], table_aliases, default_db, default_table)
                    def extract_source_cols(expr):
                        if isinstance(expr, str):
                            if expr and not expr.startswith('literal('):
                                col_info['source'].append(get_fully_qualified_name(expr, table_aliases, default_db, default_table))
                        elif isinstance(expr, dict):
                            if 'value' in expr and isinstance(expr['value'], str):
                                col_info['source'].append(get_fully_qualified_name(expr['value'], table_aliases, default_db, default_table))
                            for v in expr.values():
                                if isinstance(v, dict):
                                    extract_source_cols(v)
                                elif isinstance(v, list):
                                    for item in v:
                                        extract_source_cols(item)
                    extract_source_cols(col['value'])
                else:
                    col_info['source'] = str(col['value'])
            columns.append(col_info)
    logging.debug(f"Extracted columns: {columns}")
    return columns

def parse_sql_mapping(sql: str) -> List[Tuple[str, str, Optional[str]]]:
    """Parse SQL query and extract (source, target, transformation) tuples."""
    mappings = []
    try:
        parsed = parse(sql)
        logging.debug(f"Parsed SQL: {parsed}")
    except Exception as e:
        logging.error(f"Failed to parse SQL: {e}")
        return mappings

    # Identify target table
    target_table = None
    target_columns = []
    source_table = None
    is_wildcard = False

    if 'insert' in parsed:
        target_table = parsed['insert']
        if 'columns' in parsed:
            target_columns = parsed['columns']
        else:
            # Infer from SELECT clause
            select_clause = parsed['query']['select']
            target_columns = [get_target_column_name(item) for item in select_clause]
    elif 'create table' in parsed:
        target_table = parsed['create table']['name']
        if 'query' in parsed['create table'] and 'select' in parsed['create table']['query']:
            select_clause = parsed['create table']['query']['select']
            target_columns = [get_target_column_name(item) for item in select_clause]
    
    if not target_table:
        logging.warning("No target table found in query")
        return mappings

    # Extract table aliases from FROM clause
    from_clause = parsed.get('query', {}).get('from', [])
    table_aliases = extract_table_aliases(from_clause)
    if from_clause and isinstance(from_clause, list) and isinstance(from_clause[0], dict):
        source_table = from_clause[0].get('value', '')

    # Extract source columns from SELECT clause
    select_clause = parsed['query']['select'] if 'query' in parsed and 'select' in parsed['query'] else []
    if select_clause and any('all_columns' in item for item in select_clause):
        is_wildcard = True
        source_fq = f"{source_table}.*" if isinstance(source_table, str) else f"{'.'.join(source_table)}.*"
        target_fq = f"{target_table}.*" if isinstance(target_table, str) else f"{'.'.join(target_table)}.*"
        mappings.append((source_fq, target_fq, None))
        logging.debug(f"Wildcard mapping: {mappings}")
        return mappings

    source_columns = extract_columns(select_clause, table_aliases)

    # Map source to target
    for idx, src_col in enumerate(source_columns):
        if idx >= len(target_columns):
            logging.warning(f"More source columns than target columns, skipping index {idx}")
            break
        target_col = target_columns[idx]
        target_fq = f"{target_table}.{target_col}" if isinstance(target_table, str) else f"{'.'.join(target_table)}.{target_col}"

        if 'transformation' in src_col:
            for src in src_col['source']:
                mappings.append((src, target_fq, src_col['transformation']))
        elif isinstance(src_col['source'], str) and not src_col['source'].startswith('literal('):
            mappings.append((src_col['source'], target_fq, None))

    logging.debug(f"Generated mappings: {mappings}")
    return mappings

def main():
    # Test queries
    queries = [
        """
        INSERT INTO Analytics.ReportData
        SELECT 
            a.UserGroup,
            a.UserID,
            b.TransactionDate,
            c.SessionEnd,
            b.CustomerID,
            substr(upper(trim(concat(a.MonthData, ' ', b.TransactionDate))), 1, 50) AS SegmentInfo,
            'Campaign Alpha' AS Campaign
        FROM Marketing.UserSegments AS a
        INNER JOIN Sales.TransactionLogs AS b
        ON a.CustomerID = b.CustomerID
        LEFT OUTER JOIN Analytics.SessionLogs AS c
        ON a.CustomerID = c.CustomerID 
        AND b.TransactionDate >= a.StartDate 
        AND b.TransactionDate <= a.EndDate
        AND b.TransactionDate <= c.SessionEnd;
        """,
        """
        INSERT INTO CorpMktg.T5
        SELECT * FROM CorpMktg.T4;
        """
    ]

    for sql in queries:
        print(f"\nProcessing query:\n{sql}")
        try:
            mappings = parse_sql_mapping(sql)
            if not mappings:
                logging.info("No mappings generated. Check the query or parser output.")
            for mapping in mappings:
                print(mapping)
        except Exception as e:
            logging.error(f"Error processing query: {e}")

if __name__ == "__main__":
    main()