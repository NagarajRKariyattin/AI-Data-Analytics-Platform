import streamlit as st
from src.database.queries import sales_by_region
'''from src.database.queries import (
    total_sales,
    total_profit,
    total_orders,
    total_customers,
    total_products
)
'''
from src.visualization.charts import plot_bar_chart
from src.database.queries import *

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
 
fig = plot_bar_chart(
    sales_region_df,
    "Region",
    #"Sales",
    "total_sales",
    "Sales by Region",
    "Region",
    "Sales"
)
st.pyplot(fig)