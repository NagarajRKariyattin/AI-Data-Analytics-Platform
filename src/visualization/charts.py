import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.express as px


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

def generate_dashboard_charts(df):
    """
    Generate multiple interactive charts for the dashboard.
    Charts automatically update based on the filtered dataframe.
    """

    if df.empty:
        st.warning("No data available for visualization.")
        return

    st.subheader("📊 Data Visualizations")

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    categorical_cols = [
        col for col in df.columns
        if col not in numeric_cols
        and not pd.api.types.is_datetime64_any_dtype(df[col])
    ]

    # ==========================
    # Row 1
    # ==========================

    col1, col2 = st.columns(2)

    # Bar Chart
    with col1:
        if numeric_cols and categorical_cols:

            category = categorical_cols[0]
            value = numeric_cols[0]

            chart_data = (
                df.groupby(category)[value]
                .mean()
                .reset_index()
            )

            fig = px.bar(
                chart_data,
                x=category,
                y=value,
                title=f"Average {value} by {category}"
            )

            st.plotly_chart(fig, use_container_width=True)

    # Pie Chart
    with col2:
        if categorical_cols:

            category = categorical_cols[0]

            chart_data = (
                df[category]
                .value_counts()
                .reset_index()
            )

            chart_data.columns = [category, "Count"]

            fig = px.pie(
                chart_data,
                names=category,
                values="Count",
                title=f"{category} Distribution"
            )

            st.plotly_chart(fig, use_container_width=True)

    # ==========================
    # Row 2
    # ==========================

    col3, col4 = st.columns(2)

    # Histogram
    with col3:
        if numeric_cols:

            value = numeric_cols[0]

            fig = px.histogram(
                df,
                x=value,
                nbins=20,
                title=f"{value} Distribution"
            )

            st.plotly_chart(fig, use_container_width=True)

    # Box Plot
    with col4:
        if numeric_cols:

            value = numeric_cols[0]

            fig = px.box(
                df,
                y=value,
                title=f"{value} Spread"
            )

            st.plotly_chart(fig, use_container_width=True)

    # ==========================
    # Scatter Plot
    # ==========================

    if len(numeric_cols) >= 2:

        fig = px.scatter(
            df,
            x=numeric_cols[0],
            y=numeric_cols[1],
            title=f"{numeric_cols[0]} vs {numeric_cols[1]}"
        )

        st.plotly_chart(fig, use_container_width=True)