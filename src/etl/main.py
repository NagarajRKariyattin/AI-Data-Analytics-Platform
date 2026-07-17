from src.etl.extract import extract_data
from src.etl.profiler import profile_data
from src.etl.transform import transform_data

from src.database.loader import load_dataframe
from src.database.queries import  *
from src.visualization.charts import *

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
'''
def show_business_reports():
    #top_customer = top_customers()
    print("\n==========   TOTAL 10 CUSTOMERS BY SALES ==========")
    print(top_customers())
    
    sales_region_df = sales_by_region()
    print("\n==========   TOTAL SALES BY REGION==========")
    print(sales_region_df)
    
    sales_by_categorys =sales_by_category()
    print("\n==========   TOTAL SALES BY CATEGORY==========")
    #print(sales_by_category())
    print(sales_by_categorys)


    print("\n==========   TOTAL SALES BY SUB-CATEGORY==========")
    print(sales_by_sub_category())

    monthly_sale= monthly_sales()
    print("\n==========   MONTHLY SALES==========")
    print(monthly_sale)


   # return sales_by_categorys
    return sales_region_df

'''
def show_business_reports():
    reports = {
        "sales_region": sales_by_region(),
        "sales_category": sales_by_category(),
        "monthly_sales": monthly_sales(),
        "top_customers": top_customers(),
        "sub_category": sales_by_sub_category()
    }

    return reports

def show_visualizations(reports):
     #sales_region_df = sales_by_region()

     # plot_sales_by_region(sales_region_df)
     plot_bar_chart(
         reports["sales_region"],
        x_column="Region",
        y_column="total_sales",
        title="Sales by Region",
        x_label="Region",
        y_label="Total Sales"
     )
     
     
     
     plot_horizontal_bar_chart(
        reports["top_customers"],
        x_column="Customer Name",
        y_column= "total_sales",
        title ="Top Customers",
        x_label="Customer",
        y_label="Total Sales"
        )
    
     plot_pie_chart(
         reports["sales_category"], 
        labels_column= "Category", 
        values_column="total_sales", 
        title="sales by category"
        )
         
    
     plot_line_chart(
         reports[monthly_sale],
         x_column="month", 
         y_column="total_sales",
         title="Monthly sales trend",
         x_label="Month",
         y_label="total sales"
         )
         
    
    




def main():

    df = extract_data()

    profile_data(df)

    cleaned_df = transform_data(df)

    table_name = "superstore"

    load_dataframe(cleaned_df, table_name)
    
    show_kpi_dashboard()
   # sales_region_df = show_business_reports()
    #sales_by_categorys = show_business_reports()
   # monthlysales=show_business_reports()
    reports = show_business_reports()
    show_visualizations(reports)
     






if __name__ == "__main__":
    main()