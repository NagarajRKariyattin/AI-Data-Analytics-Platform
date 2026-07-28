import pandas as pd
import plotly.express as px


def generate_chart(result):

    if result.empty:
        return None

    numeric_cols = result.select_dtypes(
        include="number"
    ).columns.tolist()

    categorical_cols = result.select_dtypes(
        exclude="number"
    ).columns.tolist()

    date_cols = [
        col for col in result.columns
        if "date" in col.lower()
        or "month" in col.lower()
        or "year" in col.lower()
    ]

    # Line Chart
    if len(date_cols) == 1 and len(numeric_cols) == 1:

        result[date_cols[0]] = pd.to_datetime(
            result[date_cols[0]]
        )

        result = result.sort_values(date_cols[0])

        return px.line(
            result,
            x=date_cols[0],
            y=numeric_cols[0],
            markers=True,
            title=f"{numeric_cols[0]} Trend"
        )

    # Pie / Bar
    elif len(categorical_cols) == 1 and len(numeric_cols) == 1:

        if result.shape[0] <= 6:

            return px.pie(
                result,
                names=categorical_cols[0],
                values=numeric_cols[0],
                title=f"{numeric_cols[0]} Distribution"
            )

        return px.bar(
            result,
            x=categorical_cols[0],
            y=numeric_cols[0],
            text=numeric_cols[0],
            title=f"{numeric_cols[0]} by {categorical_cols[0]}"
        )

    # Scatter
    elif len(numeric_cols) >= 2:

        return px.scatter(
            result,
            x=numeric_cols[0],
            y=numeric_cols[1],
            title=f"{numeric_cols[1]} vs {numeric_cols[0]}"
        )

    return None