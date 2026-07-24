import pandas as pd


def generate_summary(df):

    summary = {}

    summary["Total Rows"] = len(df)
    summary["Total Columns"] = len(df.columns)

    summary["Columns"] = list(df.columns)

    summary["Missing Values"] = df.isna().sum().to_dict()

    # ===============================
    # Sales
    # ===============================

    if "Sales" in df.columns:
        summary["Total Sales"] = round(df["Sales"].sum(), 2)
        summary["Average Sales"] = round(df["Sales"].mean(), 2)

    # ===============================
    # Profit
    # ===============================

    if "Profit" in df.columns:
        summary["Total Profit"] = round(df["Profit"].sum(), 2)
        summary["Average Profit"] = round(df["Profit"].mean(), 2)

    # ===============================
    # Category Analysis
    # ===============================

    if {"Category", "Sales"}.issubset(df.columns):

        summary["Sales by Category"] = (
            df.groupby("Category")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .to_dict()
        )

    if {"Category", "Profit"}.issubset(df.columns):

        summary["Profit by Category"] = (
            df.groupby("Category")["Profit"]
            .sum()
            .sort_values(ascending=False)
            .to_dict()
        )

    # ===============================
    # State Analysis
    # ===============================

    if {"State", "Sales"}.issubset(df.columns):

        summary["Top States by Sales"] = (
            df.groupby("State")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .to_dict()
        )

    # ===============================
    # Products
    # ===============================

    if {"Product Name", "Sales"}.issubset(df.columns):

        summary["Top Products"] = (
            df.groupby("Product Name")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .to_dict()
        )

    # ===============================
    # Segment
    # ===============================

    if {"Segment", "Sales"}.issubset(df.columns):

        summary["Sales by Segment"] = (
            df.groupby("Segment")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .to_dict()
        )

    return summary