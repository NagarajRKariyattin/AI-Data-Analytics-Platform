import streamlit as st
from src.visualization.charts import  *
from src.ai.sql_generator import generate_sql
from src.ai.executor import execute_sql
from src.ai.validator import validate_sql
from src.export.export_excel import export_to_excel
from src.dashboard.components.history import (
    initialize_history,
    add_query,
    show_history
)
from src.ai.insights import generate_insights
from src.schema.schema_detector import get_schema
from src.ui.upload_ui import upload_section
from src.visualization.charts import render_auto_chart
from src.dashboard.kpi import get_dataset_info, detect_business_kpis
from src.ai.suggested_questions import generate_suggested_questions
from src.ai.dataset_summary import generate_dataset_summary
from src.dashboard.filters import apply_filters
from src.visualization.charts import generate_dashboard_charts
from src.ui.theme import setup_page
from src.ui.styles import load_css
from src.ui.cards import app_header
from src.styles.theme import apply_theme
from src.styles.components import section_title, info_card
apply_theme()
setup_page()
load_css()
app_header()
initialize_history()
show_history() 
if "selected_query" not in st.session_state:
    st.session_state.selected_query = ""
st.divider()

uploaded_df, table_name = upload_section()
# Apply filters
if uploaded_df is not None:
    filtered_df = apply_filters(uploaded_df)
else:
    filtered_df = None

# Dynamic Dataset Overview
if filtered_df is not None:

    dataset_info = get_dataset_info(filtered_df)
    business_kpis = detect_business_kpis(filtered_df)

    section_title("📊", "Dataset Overview")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        info_card("Rows", dataset_info["rows"])
    with col2:
        info_card("Columns", dataset_info["columns"])
    with col3:
        info_card("Numeric Columns", dataset_info["numeric"])
    with col4:
        info_card("Categorical Columns", dataset_info["categorical"])
    with col5:
        info_card("Missing Values", dataset_info["missing"])
     

    if business_kpis:
        section_title("📈", "Business KPIs")

        cols = st.columns(len(business_kpis))

        for col, (key, value) in zip(cols, business_kpis.items()):

            if isinstance(value, float):
                value = f"{value:,.2f}"

            elif isinstance(value, int):
                value = f"{value:,}"

            with col:
                info_card(key, value)

        summary = generate_dataset_summary(
            filtered_df,
            dataset_info,
            business_kpis
        )
        st.subheader("📋 Dataset Summary")
        st.info(summary)
        generate_dashboard_charts(filtered_df)
# AI Suggested Questions
if filtered_df is not None:

    questions = generate_suggested_questions(filtered_df)

    if questions:

        st.subheader("💡 Suggested Questions")

        for q in questions:

            if st.button(q):
                st.session_state["selected_query"] = q
                st.rerun()

        st.divider()
st.header("🤖 AI Data Analyst")

question = st.text_input(
    "Ask a question about your data:",
    key="selected_query",
    placeholder="Example: Show total sales by region"
)

if st.button("Generate Report"):

    if question:

        table_name = st.session_state.get("active_table")

        if not table_name:
            st.error("Please upload a dataset first.")
            st.stop()

        schema = get_schema(table_name)

        sql = generate_sql(
            question,
            table_name,
            schema
        )

        st.subheader("Generated SQL")
        st.code(sql, language="sql")

        # Validate SQL
        is_valid, message = validate_sql(sql, table_name)

        if not is_valid:
            st.error(f"❌ {message}")

        else:

            try:

                # Execute SQL
                df = execute_sql(sql)
                st.session_state["query_df"] = df
                st.session_state["question"] = question

                # Save query history
                add_query(question)

                # Show result

            except Exception as e:

                st.error(" Error while executing SQL.")
                st.exception(e)

if "query_df" in st.session_state:

    st.subheader("Query Result")
    st.dataframe(st.session_state["query_df"], use_container_width=True)
    csv = st.session_state["query_df"].to_csv(index=False)

    st.download_button(
    label="⬇ Download CSV",
    data=csv,
    file_name="query_result.csv",
    mime="text/csv"
    )
    excel_file = export_to_excel(st.session_state["query_df"])

    st.download_button(
    label="⬇ Download Excel",
    data=excel_file,
    file_name="query_result.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    
    fig = render_auto_chart(st.session_state["query_df"])

    if fig:
        st.subheader("📊 Visualization")
        st.pyplot(fig)

    if st.button("✨ Generate AI Insights"):

        with st.spinner("Analyzing data..."):

            insights = generate_insights(
                st.session_state["query_df"],
                st.session_state["question"]
            )

        st.subheader("🤖 AI Business Insights")
        st.success(insights)
 
