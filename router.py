from intent_router import detect_intent
from sql_generator import generate_sql
from chatbot import ask_business_analyst
from database.queries import execute_query


def process_prompt(prompt, dashboard_df, summary, conn):

    intent = detect_intent(prompt)

    if intent == "sql":

        sql = generate_sql(
            prompt,
            list(dashboard_df.columns)
        )

        result = execute_query(
            conn,
            sql
        )

        return {
            "type": "sql",
            "sql": sql,
            "result": result,
            "chart": True
             }

    answer = ask_business_analyst(
        dashboard_df,
        summary,
        prompt
    )

    return {
        "type": "analysis",
        "answer": answer
    }