from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def ask_business_analyst(df, summary, question):
    prompt = f"""
You are an expert Senior Business Analyst.

Dataset Summary:
{summary}

Dataset Preview:
{df.head(20).to_string()}

User Question:
{question}

Instructions:
- Answer based on the dataset preview and summary.
- If the answer isn't available, clearly say so.
- Give business recommendations whenever appropriate.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
    )

    return response.text