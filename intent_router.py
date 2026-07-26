def detect_intent(question):

    question = question.lower()

    sql_keywords = [
        "show",
        "list",
        "top",
        "bottom",
        "highest",
        "lowest",
        "count",
        "sum",
        "total",
        "average",
        "avg",
        "group",
        "sales",
        "profit",
        "customer",
        "category",
        "state",
        "city",
        "order",
        "how many",
        "which",
        "compare",
        "display"
    ]

    for keyword in sql_keywords:
        if keyword in question:
            return "sql"

    return "analysis"
    