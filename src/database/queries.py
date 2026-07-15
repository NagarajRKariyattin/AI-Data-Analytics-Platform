from src.database.connection import get_engine
import pandas as pd
def execute_query(query):
    """
    Execute any SQL query and return a DataFrame.
    """
    engine = get_engine()
    return pd.read_sql(query, engine)


def total_sales():
    query = """
    SELECT SUM("Sales") AS total_sales
    FROM superstore;
    """
    return execute_query(query)

def total_profit():
    query = """
     select sum("Profit") as total_profit
     from superstore
    """
    return execute_query(query)

def average_sales():
    query = """
    select avg("Sales") as Average_Sales from superstore
    """
    return execute_query(query)

def total_orders():
    query = """
    select count(*) as total_orders from superstore
    """
    return execute_query(query)

def total_customers():
    query = """
    select count(distinct "Customer ID") as
    total_customers from superstore
    """
    return execute_query(query)

def total_products():
    query = """
    select count(distinct "Product ID") as
    total_products from superstore
    """
    return execute_query(query)

def top_customers():
    query = """
     SELECT
        "Customer Name",
        SUM("Sales") AS total_sales
     FROM superstore
     GROUP BY "Customer Name"
     ORDER BY total_sales DESC
     LIMIT 10;
     """
    return execute_query(query)

def profit_by_region():
    query = """
    select "Region", 
    sum("Profit") as total_profit
    from superstore
    group by "Region"
    order by total_profit desc
    """
    return execute_query(query)

def sales_by_category():
    query = """
    select "Category",
    sum("Sales") as total_sales 
    from superstore 
    group by "Category"
    order by total_sales
    """
    return execute_query(query)
def sales_by_sub_category():
    query ="""
    select "Sub-Category",
    sum("Sales") as total_sales
    from superstore
    group by "Sub-Category"
    order by total_sales
    """
    return execute_query(query)