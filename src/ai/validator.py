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

def validate_sql(sql_query):
    """
    Validate AI-generated SQL before execution.
    Returns (True, message) if valid,
    otherwise (False, error_message).
    """

    if not sql_query:
        return False, "SQL query is empty."

    sql = sql_query.strip().upper()

    # Only allow SELECT if the query dont have select it will ignore
    if not sql.startswith("SELECT"):
        return False, "Only SELECT queries are allowed."

    # Block dangerous query keywords
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

    # multiple query or lines
    if sql_query.count(";") > 1:
        return False, "Multiple SQL statements are not allowed."

    # Ensure correct table
    if "SUPERSTORE" not in sql:
        return False, "Query must use the 'superstore' table."
        valid_columns, message = validate_columns(sql_query)

        if not valid_columns:
           return False, message
    return True, "SQL is valid."

