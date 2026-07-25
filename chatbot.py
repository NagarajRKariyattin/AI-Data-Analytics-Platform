from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def ask_business_analyst(df, summary, question):

    prompt = f"""
You are a Senior Business Analyst.

Dataset Summary:
{summary}

Dataset Preview:
{df.head(20).to_string()}

User Question:
{question}

Instructions:
- Answer only using the dataset information.
- If the answer is not available, clearly say so.
- Give business recommendations where appropriate.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:

        return f"Error: {e}"