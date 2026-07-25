from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def generate_sql(question, columns):

    prompt = f"""
You are an expert SQLite SQL Generator.

Database Name:
orders

Available Columns:
{', '.join(columns)}

STRICT RULES:

- Return ONLY a valid SQLite SELECT query.
- Never explain anything.
- Never answer the user's question directly.
- Never use Markdown.
- Never use ``` or ```sql.
- The response must begin with SELECT.
- Use only the table named orders.
- Only use the available columns listed above.
- If a column contains spaces, wrap it in double quotes.
- Do not invent columns.
- Do not include comments.

User Question:
{question}

SQL:
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

        sql = response.text.strip()

        sql = (
            sql.replace("```sql", "")
               .replace("```", "")
               .replace("SQL:", "")
               .strip()
        )

        return sql

    except Exception as e:

        return f"ERROR: {e}"