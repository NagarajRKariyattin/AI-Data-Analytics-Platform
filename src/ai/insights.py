import requests
import json


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:3b"
import pandas as pd


def analyze_dataframe(df):
    """
    Analyze the dataframe and return factual statistics.
    """

    analysis = []

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    categorical_cols = [
        col for col in df.columns
        if col not in numeric_cols
    ]

    if len(categorical_cols) >= 1 and len(numeric_cols) >= 1:

        category = categorical_cols[0]
        value = numeric_cols[0]

        highest = df.loc[df[value].idxmax()]
        lowest = df.loc[df[value].idxmin()]

        analysis.append(
            f"Highest {value}: {highest[category]} ({highest[value]:,.2f})"
        )

        analysis.append(
            f"Lowest {value}: {lowest[category]} ({lowest[value]:,.2f})"
        )

        analysis.append(
            f"Average {value}: {df[value].mean():,.2f}"
        )

        analysis.append(
            f"Maximum {value}: {df[value].max():,.2f}"
        )

        analysis.append(
            f"Minimum {value}: {df[value].min():,.2f}"
        )

    return "\n".join(analysis)

def generate_insights(df, question):
    """
    Generate business insights from a DataFrame using Ollama.
    """

    if df.empty:
        return "No data available for analysis."

    # Convert only first few rows to text
    table = df.head(10).round(2).to_csv(index=False)
    facts = analyze_dataframe(df)
    prompt = f"""
You are a Senior Business Analyst.

Below are VERIFIED facts calculated from Python.

{facts}

Data Preview:

{df.head(20).to_string(index=False)}

Rules:

1. Use ONLY the verified facts above.
2. Never invent rankings.
3. Never invent numbers.
4. Never change any values.
5. If information is unavailable, clearly say so.
6. Write:

Executive Summary

Key Insights

Business Recommendations
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

