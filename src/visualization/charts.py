import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import FuncFormatter
import matplotlib.dates as mdates
import pandas as pd
REPORT_DIR = Path("reports/charts")
REPORT_DIR.mkdir(parents=True, exist_ok=True)
def plot_bar_chart(df, x_column, y_column, title, x_label, y_label):

    fig, ax = plt.subplots(figsize=(6, 3))

    ax.bar(df[x_column], df[y_column])
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    plt.tight_layout()
    filename = title.lower().replace(" ", "_") + ".png"

    plt.savefig(REPORT_DIR / filename)
    #plt.show()
    
    print(f"Chart saved: {REPORT_DIR / filename}")
    return fig
def plot_horizontal_bar_chart(df, x_column, y_column,title, x_label, y_label):
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.barh(df[x_column], df[y_column])
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.tight_layout()
    filename=title.lower().replace(" ","_") + ".png"
    plt.savefig(REPORT_DIR / filename)
    #plt.show()
    
    print(f"Chart saved :{REPORT_DIR /filename}")
    return fig
def plot_pie_chart(df, labels_column, values_column, title):

    fig, ax = plt.subplots(figsize=(6, 3))

    labels = df[labels_column]
    values = df[values_column]

    ax.pie(
        values,
        labels=labels
    )

    ax.set_title(title)


    filename =title.lower().replace(" ","_") + ".png"
    plt.savefig(REPORT_DIR / filename)
    #plt.show()
    print(f"Chart Saved:{REPORT_DIR /filename}")
    return fig

 
def plot_line_chart(df, x_column, y_column, title, x_label, y_label):

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(df[x_column], df[y_column], marker="o")

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    filename = title.lower().replace(" ", "_") + ".png"
    plt.savefig(REPORT_DIR / filename)

    return fig

import pandas as pd


def detect_chart_type(df):
    """
    Detect the best chart type for a query result.
    """

    if df.empty:
        return None

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    non_numeric_cols = [
        col for col in df.columns
        if col not in numeric_cols
    ]

    # Date / Month column
    for col in non_numeric_cols:
        if (
            "date" in col.lower()
            or "month" in col.lower()
            or "year" in col.lower()
        ):
            if len(numeric_cols) >= 1:
                return "line"

    # Category + Numeric
    if len(non_numeric_cols) == 1 and len(numeric_cols) == 1:

        if len(df) <= 6:
            return "pie"

        return "bar"

    # Two numeric columns
    if len(numeric_cols) == 2:
        return "scatter"

    return None
def render_auto_chart(df):

    chart = detect_chart_type(df)

    if chart == "bar":

        return plot_bar_chart(
            df,
            df.columns[0],
            df.columns[1],
            "AI Generated Chart",
            df.columns[0],
            df.columns[1]
        )

    elif chart == "pie":

        return plot_pie_chart(
            df,
            df.columns[0],
            df.columns[1],
            "AI Generated Chart"
        )

    elif chart == "line":

        return plot_line_chart(
            df,
            df.columns[0],
            df.columns[1],
            "AI Generated Chart",
            df.columns[0],
            df.columns[1]
        )

    return None



