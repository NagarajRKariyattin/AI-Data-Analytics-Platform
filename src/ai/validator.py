import re
from src.ai.schema import VALID_COLUMNS

def validate_columns(sql_query):
    """
    Check whether quoted column names exist in the schema.
    """

    columns = re.findall(r'"([^"]+)"', sql_query)

    for column in columns:
        if column not in VALID_COLUMNS:
            return False, f"Unknown column: {column}"

    return True, "Columns are valid."

def validate_sql(sql_query, table_name):

    if not sql_query:
        return False, "SQL query is empty."

    sql = sql_query.strip().upper()

    if not sql.startswith("SELECT"):
        return False, "Only SELECT queries are allowed."

    blocked = [
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER",
        "TRUNCATE",
        "CREATE",
    ]

    for keyword in blocked:
        if keyword in sql:
            return False, f"Blocked SQL keyword detected: {keyword}"

    if sql_query.count(";") > 1:
        return False, "Multiple SQL statements are not allowed."

    # Ensure the query uses the selected table
    if table_name.upper() not in sql:
        return False, f"Query must use the '{table_name}' table."

    valid_columns, message = validate_columns(sql_query)

    if not valid_columns:
        return False, message

    return True, "SQL is valid."

