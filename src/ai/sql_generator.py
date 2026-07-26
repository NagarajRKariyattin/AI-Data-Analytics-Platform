import requests

from src.ai.query_router import get_predefined_sql

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "qwen2.5:3b"


def generate_sql(user_question, table_name, schema):
    """
    Generate SQL using Ollama based on the uploaded table schema.
    """

    # Convert schema list into text for the prompt
    schema_text = "\n".join(
        [f"{col['name']} ({col['type']})" for col in schema]
    )

    # Use predefined SQL only for Superstore
    if table_name.lower() == "superstore":
        predefined_sql = get_predefined_sql(user_question)
        if predefined_sql:
            return predefined_sql

    prompt = f"""
You are an expert PostgreSQL SQL generator.

Table Name:
{table_name}

Columns:
{schema_text}

Rules:
1. Generate ONLY PostgreSQL SQL.
2. Use ONLY the columns listed above.
3. Return ONLY the SQL query.
4. Do NOT explain anything.
5. Do NOT use markdown.
6. Use PostgreSQL syntax only.

Question:
{user_question}

SQL:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    sql = response.json()["response"].strip()

    # Remove markdown if returned by the model
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql