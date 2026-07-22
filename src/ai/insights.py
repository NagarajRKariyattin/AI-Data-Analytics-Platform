import requests
import json


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:latest"


def generate_insights(df, question):
    """
    Generate business insights from a DataFrame using Ollama.
    """

    if df.empty:
        return "No data available for analysis."

    # Convert only first few rows to text
    table = df.head(10).round(2).to_csv(index=False)

    prompt = f"""
You are a Senior Business Data Analyst.

The user asked:
{question}

The SQL query returned this data:

{table}

Analyze the data and respond in the following format:

## Executive Summary
(2-3 sentences summarizing the results)

## Key Insights
- Give exactly 3 insights with numbers where possible.
- Mention trends and comparisons.
- Highlight the highest and lowest values.

## Business Recommendations
- Give 2 practical recommendations.
- Focus on improving business performance.

Keep the response under 150 words.
Do not mention SQL, databases, or technical details.
Write in professional business language.
"""

    request_body = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(
        OLLAMA_URL,
        headers={"Content-Type": "application/json"},
        json=request_body,
        timeout=60
        )

        print(response.status_code)
        print(response.text)

        response.raise_for_status()

        result = response.json()

        return result.get("response", "No insights generated.")

    except Exception as e:
        print(e)
        return str(e)

