import pandas as pd


def get_dataset_info(df):

    info = {}

    info["rows"] = len(df)
    info["columns"] = len(df.columns)

    info["numeric"] = len(df.select_dtypes(include="number").columns)

    info["categorical"] = len(
        df.select_dtypes(include=["object", "category"]).columns
    )

    info["datetime"] = len(
        df.select_dtypes(include=["datetime", "datetimetz"]).columns
    )

    info["missing"] = int(df.isna().sum().sum())
    info["datetime"] = len(
    df.select_dtypes(include=["datetime", "datetimetz"]).columns)

    return info
def detect_business_kpis(df):
    """
    Detect business KPIs dynamically using partial column matching.
    """

    kpis = {}

    # Lowercase mapping
    columns = {col.lower(): col for col in df.columns}

    def find_column(keywords):
        """
        Return the first column whose name contains
        any keyword.
        """
        for lower_name, original_name in columns.items():
            for keyword in keywords:
                if keyword in lower_name:
                    return original_name
        return None

    # ---------- Sales ----------
    sales_col = find_column(["sales", "sale", "sales_amount"])
    if sales_col:
        kpis["Total Sales"] = df[sales_col].sum()
        kpis["Average Sales"] = df[sales_col].mean()

    # ---------- Profit ----------
    profit_col = find_column(["profit", "net_profit", "gross_profit"])
    if profit_col:
        kpis["Total Profit"] = df[profit_col].sum()
        kpis["Average Profit"] = df[profit_col].mean()

    # ---------- Salary ----------
    salary_col = find_column(["salary", "employee_salary", "annual_salary", "basic_salary"])
    if salary_col:
        kpis["Average Salary"] = df[salary_col].mean()
        kpis["Highest Salary"] = df[salary_col].max()

    # ---------- Orders ----------
    order_col = find_column(["order_id", "order"])
    if order_col:
        kpis["Orders"] = df[order_col].nunique()

    # ---------- Customers ----------
    customer_col = find_column(["customer_id", "customer"])
    if customer_col:
        kpis["Customers"] = df[customer_col].nunique()

    # ---------- Products ----------
    product_col = find_column(["product_name", "product"])
    if product_col:
        kpis["Products"] = df[product_col].nunique()

    # ---------- Departments ----------
    department_col = find_column(["department", "dept"])
    if department_col:
        kpis["Departments"] = df[department_col].nunique()

    # ---------- Managers ----------
    manager_col = find_column(["is_manager", "manager"])

    if manager_col:

        if df[manager_col].dtype == bool:
            kpis["Managers"] = df[manager_col].sum()

        elif str(df[manager_col].dtype).startswith(("int", "float")):
            kpis["Managers"] = (df[manager_col] == 1).sum()

        else:
            kpis["Managers"] = (
                df[manager_col]
                .astype(str)
                .str.lower()
                .isin(["yes", "true", "manager"])
                .sum()
            )

    return kpis