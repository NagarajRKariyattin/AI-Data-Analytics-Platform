from src.etl.extract import extract_data
from src.etl.profiler import profile_data
from src.etl.transform import transform_data

from src.database.loader import load_dataframe
from src.database.queries import  *

def show_kpi_dashboard():
    sales = total_sales()
    print("\n========== TOTAL SALES ==========")
    print(sales)

    profit= total_profit()
    print("\n========== TOTAL PROFIT ==========")
    print(profit)

    avg_sales = average_sales()
    print("\n==========  AVERAGE SALES ==========")
    print(avg_sales)

    total_order= total_orders()
    print("\n==========   TOTAL ORDERS ==========")
    print(total_order)

    total_customer= total_customers()
    print("\n==========   TOTAL  CUSTOMERS ==========")
    print(total_customer) 

    total_product = total_products()
    print("\n==========   TOTAL PRODUCTS ==========")
    print(total_product)

def show_business_reports():
    #top_customer = top_customers()
    print("\n==========   TOTAL 10 CUSTOMERS BY SALES ==========")
    print(top_customers())
    
    print("\n==========   TOTAL PROFIT BY REGION==========")
    print(profit_by_region())

    print("\n==========   TOTAL SALES BY CATEGORY==========")
    print(sales_by_category())

    print("\n==========   TOTAL SALES BY SUB-CATEGORY==========")
    print(sales_by_sub_category())



def main():

    df = extract_data()

    profile_data(df)

    cleaned_df = transform_data(df)

    table_name = "superstore"

    load_dataframe(cleaned_df, table_name)
    
    show_kpi_dashboard()
    show_business_reports()
     






if __name__ == "__main__":
    main()