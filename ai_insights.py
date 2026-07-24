from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def generate_ai_insights(summary):

    prompt = f"""
You are a Senior Business Analyst.

Analyze the following dataset summary.

Return your response using Markdown.

Include:
- Executive Summary
- Key Business Insights
- Risks
- Opportunities
- Recommendations

Dataset Summary:
{summary}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )
        return response.text

    except Exception as e:
        return f"❌ Gemini Error:\n\n{e}"