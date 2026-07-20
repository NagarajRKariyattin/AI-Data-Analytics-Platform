def get_predefined_sql(question):
    question = question.lower().strip()

    # Total Products
    if (
        "total products" in question
        or "number of products" in question
        or "count of products" in question
    ):
        return """
        SELECT COUNT(DISTINCT "Product ID") AS total_products
        FROM superstore;
        """

    # Total Customers
    if (
        "total customers" in question
        or "number of customers" in question
    ):
        return """
        SELECT COUNT(DISTINCT "Customer ID") AS total_customers
        FROM superstore;
        """

    # Total Orders
    if (
        "total orders" in question
        or "number of orders" in question
    ):
        return """
        SELECT COUNT(DISTINCT "Order ID") AS total_orders
        FROM superstore;
        """

    # Total Sales
    if "total sales" in question:
        return """
        SELECT SUM("Sales") AS total_sales
        FROM employee;
        """

    # Total Profit
    if "total profit" in question:
        return """
        SELECT SUM("Profit") AS total_profit
        FROM superstore;
        """
    
    if (
    "top 5 profitable products" in question
    or "top five profitable products" in question):
        return """
        SELECT
        "Product Name",
        SUM("Profit") AS total_profit
        FROM superstore
        GROUP BY "Product Name"
        ORDER BY total_profit DESC
        LIMIT 5;
        """

    return None