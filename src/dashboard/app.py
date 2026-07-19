import streamlit as st
#from src.database.queries import sales_by_region
from src.database.queries import (
    total_sales,
    total_profit,
    total_orders,
    total_customers,
    total_products
)
from src.visualization.charts import  *
from src.database.queries import *
from src.ai.sql_generator import generate_sql
from src.ai.executor import execute_sql

st.set_page_config(
    page_title="AI Data Analytics Platform",
    layout="wide"
)

st.title("📊 AI Data Analytics Platform")
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

st.header("🤖 AI Data Analyst")

question = st.text_input(
    "Ask a question about your data:",
    placeholder="Example: Show total sales by region"
)

if st.button("Generate Report"):

    if question:
        try:
            sql = generate_sql(question)

            st.subheader("Generated SQL")
            st.code(sql, language="sql")

            df = execute_sql(sql)

            st.subheader("Query Result")
            st.dataframe(df, use_container_width=True)

        except Exception as e:
           st.error("❌ The AI generated an invalid SQL query.")
           st.exception(e)
 
fig = plot_bar_chart(
    sales_region_df,
    "Region",
    #"Sales",
    "total_sales",
    "Sales by Region",
    "Region",
    "Sales"
)
st.subheader(" Sales by Region")
#st.pyplot(region_fig)
st.pyplot(fig)
sales_category_df = sales_by_category()
fig= plot_pie_chart(
        sales_category_df,
        #sales_category,
        "Category",
        "total_sales",
        "Sales by Category"
    )
st.subheader("Sales by Category")
st.pyplot(fig)
monthly_df = monthly_sales()
st.write(monthly_df)
st.write(monthly_df.shape)

fig=  plot_line_chart(
        monthly_df,
        "month",
        "total_sales",
        "Monthly Sales Trend",
        "Month",
        "Sales"
    )
st.subheader("Monthly Sales Trend")
st.pyplot(fig)

top_customer_df = top_customers()
fig=  plot_horizontal_bar_chart(
        top_customer_df,
        "Customer Name",
        "total_sales",
        "Top Customers",
        "Customer",
        "Sales"
    )
st.subheader("Top 10 Customers")
st.pyplot(fig)
