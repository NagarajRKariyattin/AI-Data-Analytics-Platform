from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def explain_result(result_df):

    prompt = f"""
You are a Senior Business Analyst.

Analyze the following SQL query result.

{result_df.to_string(index=False)}

Respond using Markdown.

Include:

## Key Finding

## Business Impact

## Recommendation

Keep your answer under 200 words.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:

        return f"Error: {e}"