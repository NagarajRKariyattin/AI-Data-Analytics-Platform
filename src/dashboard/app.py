import streamlit as st
#from src.database.queries import sales_by_region
from src.visualization.charts import  *
from src.database.queries import *
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
from src.upload.upload_csv import load_csv
from src.database.upload_table import upload_dataframe
from src.schema.schema_detector import get_schema
from src.database.table_manager import get_table_names
st.set_page_config(
    page_title="AI Data Analytics Platform",
    layout="wide"
)

st.title("📊 AI Data Analytics Platform")
initialize_history()
show_history() 
if "selected_query" not in st.session_state:
    st.session_state.selected_query = ""
col1, col2, col3, col4, col5 = st.columns(5)

sales = total_sales().iloc[0, 0]
profit = total_profit().iloc[0, 0]
orders = total_orders().iloc[0, 0]
customers = total_customers().iloc[0, 0]
products = total_products().iloc[0, 0]

with col1:
    st.metric("Total Sales", f"${sales:,.2f}")

with col2:
    st.metric("Total Profit", f"${profit:,.2f}")

with col3:
    st.metric("Orders", f"{orders:,}")

with col4:
    st.metric("Customers", f"{customers:,}")

with col5:
    st.metric("Products", f"{products:,}")
sales_region_df = sales_by_region()
#st.write(sales_region_df)
#st.write(sales_region_df.columns)

# Stop execution here temporarily
#st.stop()

st.divider()
st.header("📂 Upload Dataset")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)
if uploaded_file is not None:

    uploaded_df = load_csv(uploaded_file)

    st.success("✅ Dataset uploaded successfully!")

    st.write("### Preview")
    st.dataframe(uploaded_df.head())
    st.write("### Dataset Information")

    st.write(f"Rows: {uploaded_df.shape[0]}")
    st.write(f"Columns: {uploaded_df.shape[1]}")

    st.write("### Column Names")
    st.write(uploaded_df.columns.tolist())
    dtype_df = uploaded_df.dtypes.astype(str).reset_index()
    dtype_df.columns = ["Column", "Data Type"]

    st.dataframe(dtype_df)

    """st.write("### Data Types")
    st.dataframe(uploaded_df.dtypes.reset_index().rename(
        columns={"index": "Column", 0: "Data Type"}
    ))"""

    st.subheader("Upload Dataset to PostgreSQL")

    tables = get_table_names()

    table_name = st.selectbox(
        "Select Table",
        tables,
        key="table_name"
    )
    if st.button("Upload to PostgreSQL"):

        upload_dataframe(uploaded_df, table_name)

        st.success(f"✅ '{table_name}' uploaded successfully!")
    schema = get_schema(table_name)

    st.subheader("Detected Schema")

    st.table(schema)

st.header("🤖 AI Data Analyst")

question = st.text_input(
    "Ask a question about your data:",
    value=st.session_state.get("selected_query", ""),
    placeholder="Example: Show total sales by region"
)

if st.button("Generate Report"):

    if question:

        table_name = st.session_state.get("table_name")

        if not table_name:
            st.error("Please select a table.")
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
        is_valid, message = validate_sql(sql)

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
 
