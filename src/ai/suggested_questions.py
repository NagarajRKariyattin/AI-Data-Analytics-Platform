def generate_suggested_questions(df):
    """
    Generate suggested questions dynamically
    based on uploaded columns.
    """

    questions = []

    columns = {col.lower(): col for col in df.columns}

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    # Average numeric columns by categorical columns
    for num in numeric_cols:
        for cat in categorical_cols:
            questions.append(
                f"Average {num.replace('_', ' ')} by {cat.replace('_', ' ')}"
            )

    # Top values
    for num in numeric_cols:
        questions.append(
            f"Top 10 records by {num.replace('_', ' ')}"
        )

    # Count by category
    for cat in categorical_cols:
        questions.append(
            f"Count by {cat.replace('_', ' ')}"
        )

    # Remove duplicates while preserving order
    questions = list(dict.fromkeys(questions))

    return questions[:10]