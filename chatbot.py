from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def ask_business_analyst(summary, question):

    prompt = f"""
You are an expert Senior Business Analyst.

You are helping users analyze their uploaded dataset.

Dataset Summary:

{summary}

User Question:

{question}

Instructions:

- Answer ONLY using the dataset summary.
- Be professional.
- Explain your reasoning.
- If the information isn't available, clearly say so.
- Give business recommendations whenever appropriate.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",   # or your working model
        contents=prompt,
    )

    return response.text