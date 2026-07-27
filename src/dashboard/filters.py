import streamlit as st


def apply_filters(df):
    """
    Apply interactive filters to the uploaded dataset.
    """

    filtered_df = df.copy()

    categorical_cols = filtered_df.select_dtypes(
        include=["object", "category"]
    ).columns

    st.sidebar.header("🎛 Filters")

    for col in categorical_cols:

        values = ["All"] + sorted(
            filtered_df[col].dropna().unique().tolist()
        )

        selected = st.sidebar.selectbox(
            col.replace("_", " ").title(),
            values
        )

        if selected != "All":
            filtered_df = filtered_df[
                filtered_df[col] == selected
            ]

    return filtered_df