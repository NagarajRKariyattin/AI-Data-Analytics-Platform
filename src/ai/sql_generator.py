import requests

from src.ai.prompt import DATABASE_SCHEMA
from src.ai.query_router import get_predefined_sql

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "llama3.2:latest"


def generate_sql(user_question):
    predefined_sql = get_predefined_sql(user_question)

    if predefined_sql:
        return predefined_sql

    prompt = f"""
{DATABASE_SCHEMA}

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

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql
'''
if __name__ == "__main__":
    question = "Show total sales by region"
    sql = generate_sql(question)
    print(sql)
    '''