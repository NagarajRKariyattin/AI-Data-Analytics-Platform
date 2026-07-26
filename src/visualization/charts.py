import matplotlib.pyplot as plt
import pandas as pd


def detect_chart_type(df):
    """
    Detect the most suitable chart type
    based on dataframe columns.
    """

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    date_cols = df.select_dtypes(
        include=["datetime64", "datetime"]
    ).columns.tolist()

    categorical_cols = [
        col for col in df.columns
        if col not in numeric_cols + date_cols
    ]

    # Line Chart
    if len(date_cols) >= 1 and len(numeric_cols) >= 1:
        return "line"

    # Scatter Plot
    if len(numeric_cols) >= 2:
        return "scatter"

    # Pie Chart (check BEFORE Bar Chart)
    if len(categorical_cols) == 1 and len(numeric_cols) == 1:

        unique = df[categorical_cols[0]].nunique()

        # Pie chart only for a small number of categories
        if 2 <= unique <= 6:
            return "pie"

    # Bar Chart
    if len(categorical_cols) >= 1 and len(numeric_cols) >= 1:
        return "bar"

    return "table"
def render_auto_chart(df):
    """
    Automatically generate the best chart
    based on the dataframe.
    """

    chart = detect_chart_type(df)

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    date_cols = df.select_dtypes(include=["datetime64", "datetime"]).columns.tolist()

    categorical_cols = [
        col for col in df.columns
        if col not in numeric_cols + date_cols
    ]

    fig, ax = plt.subplots(figsize=(8, 5))

    if chart == "bar":

        ax.bar(df[categorical_cols[0]], df[numeric_cols[0]])

        ax.set_xlabel(categorical_cols[0])

        ax.set_ylabel(numeric_cols[0])

    elif chart == "line":

        ax.plot(
            df[date_cols[0]],
            df[numeric_cols[0]],
            marker="o"
        )

        ax.set_xlabel(date_cols[0])

        ax.set_ylabel(numeric_cols[0])

    elif chart == "scatter":

        ax.scatter(
            df[numeric_cols[0]],
            df[numeric_cols[1]]
        )

        ax.set_xlabel(numeric_cols[0])

        ax.set_ylabel(numeric_cols[1])

    elif chart == "pie":

        ax.pie(
            df[numeric_cols[0]],
            labels=df[categorical_cols[0]],
            autopct="%1.1f%%"
        )

    else:
        plt.close(fig)
        return None

    ax.set_title("AI Generated Visualization")

    plt.xticks(rotation=45)

    plt.tight_layout()

    return fig