
PREDEFINED_QUERIES = {
    (
        "total sales",
        "overall sales",
        "sales amount",
        "total revenue",
        "overall revenue",
        "revenue",
        "how much sales",
        "what is total sales",
    ): """
        SELECT SUM("Sales") AS total_sales
        FROM superstore;
    """,

    (
        "total profit",
        "overall profit",
        "net profit",
        "profit",
        "how much profit",
        "what is total profit",
    ): """
        SELECT SUM("Profit") AS total_profit
        FROM superstore;
    """,

    (
        "total customers",
        "number of customers",
        "customer count",
    ): """
        SELECT COUNT(DISTINCT "Customer ID") AS total_customers
        FROM superstore;
    """,

    (
        "total products",
        "number of products",
        "product count",
    ): """
        SELECT COUNT(DISTINCT "Product ID") AS total_products
        FROM superstore;
    """,

    (
        "total orders",
        "number of orders",
        "order count",
    ): """
        SELECT COUNT(DISTINCT "Order ID") AS total_orders
        FROM superstore;
    """,
    (
    "top 5 profitable products",
    "top five profitable products",
    "most profitable products",
    "highest profit products",
    ): """
    SELECT
        "Product Name",
        SUM("Profit") AS total_profit
    FROM superstore
    GROUP BY "Product Name"
    ORDER BY total_profit DESC
    LIMIT 5;
    """,
    (
    "top 5 products by sales",
    "top selling products",
    "best selling products",
    "highest selling products",
    ): """
    SELECT
        "Product Name",
        SUM("Sales") AS total_sales
    FROM superstore
    GROUP BY "Product Name"
    ORDER BY total_sales DESC
    LIMIT 5;
    """,

    (
    "top customers",
    "top 10 customers",
    "best customers",
    "highest paying customers",
    "customers by sales",
): """
    SELECT
        "Customer Name",
        SUM("Sales") AS total_sales
    FROM superstore
    GROUP BY "Customer Name"
    ORDER BY total_sales DESC
    LIMIT 10;
    """,
    (
    "top cities",
    "top 10 cities",
    "best cities",
    "cities by sales",
): """
    SELECT
        "City",
        SUM("Sales") AS total_sales
    FROM superstore
    GROUP BY "City"
    ORDER BY total_sales DESC
    LIMIT 10;
    """,

    (
    "top states",
    "top 10 states",
    "best states",
    "states by sales",
): """
    SELECT
        "State",
        SUM("Sales") AS total_sales
    FROM superstore
    GROUP BY "State"
    ORDER BY total_sales DESC
    LIMIT 10;
    """,

    (
    "top categories",
    "categories by sales",
    "best categories",
): """
    SELECT
        "Category",
        SUM("Sales") AS total_sales
    FROM superstore
    GROUP BY "Category"
    ORDER BY total_sales DESC;
    """,

    (
    "sales by category",
    "category wise sales",
    "sales per category",
): """
    SELECT
        "Category",
        SUM("Sales") AS total_sales
    FROM superstore
    GROUP BY "Category"
    ORDER BY total_sales DESC;
    """,
    (
    "profit by category",
    "category wise profit",
    "profit per category",
): """
    SELECT
        "Category",
        SUM("Profit") AS total_profit
    FROM superstore
    GROUP BY "Category"
    ORDER BY total_profit DESC;
    """,
    (
    "sales by region",
    "region wise sales",
    "sales per region",
): """
    SELECT
        "Region",
        SUM("Sales") AS total_sales
    FROM superstore
    GROUP BY "Region"
    ORDER BY total_sales DESC;
    """,

    (
    "profit by region",
    "region wise profit",
    "profit per region",
): """
    SELECT
        "Region",
        SUM("Profit") AS total_profit
    FROM superstore
    GROUP BY "Region"
    ORDER BY total_profit DESC;
    """,
    (
    "sales by segment",
    "segment wise sales",
    "sales per segment",
): """
    SELECT
        "Segment",
        SUM("Sales") AS total_sales
    FROM superstore
    GROUP BY "Segment"
    ORDER BY total_sales DESC;
    """,

    (
    "monthly sales",
    "sales by month",
    "month wise sales",
    "monthly revenue",
): """
    SELECT
    DATE_TRUNC('month', TO_DATE("Order Date", 'MM/DD/YYYY')) AS month,
    SUM("Sales") AS total_sales
    FROM superstore
    GROUP BY month
    ORDER BY month;
    """,

    (
    "monthly profit",
    "profit by month",
    "month wise profit",
): """
    SELECT
    DATE_TRUNC('month', TO_DATE("Order Date", 'MM/DD/YYYY')) AS month,
    SUM("Profit") AS total_profit
    FROM superstore
    GROUP BY month
    ORDER BY month;
    """,
    (
    "yearly sales",
    "sales by year",
    "annual sales",
): """
    SELECT
    DATE_TRUNC('year', TO_DATE("Order Date", 'MM/DD/YYYY')) AS year,
    SUM("Sales") AS total_sales
    FROM superstore
    GROUP BY year
    ORDER BY year;
    """,
    (
    "yearly profit",
    "profit by year",
    "annual profit",
): """
    SELECT
    DATE_TRUNC('year', TO_DATE("Order Date", 'MM/DD/YYYY')) AS year,
    SUM("Profit") AS total_profit
    FROM superstore
    GROUP BY year
    ORDER BY year;
    """,
    (
    "orders by month",
    "monthly orders",
    "order trend",
): """
    SELECT
    DATE_TRUNC('month', TO_DATE("Order Date", 'MM/DD/YYYY')) AS month,
    COUNT(DISTINCT "Order ID") AS total_orders
    FROM superstore
    GROUP BY month
    ORDER BY month;
    """,



}

def get_predefined_sql(question):
    """
    Return the SQL for the best matching predefined query.
    Chooses the longest matching keyword.
    """

    question = question.lower().strip()

    best_sql = None
    best_length = -1

    for keywords, sql in PREDEFINED_QUERIES.items():
        for keyword in keywords:
            if keyword in question and len(keyword) > best_length:
                best_sql = sql
                best_length = len(keyword)

    return best_sql
