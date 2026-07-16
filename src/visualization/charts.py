import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import FuncFormatter
import matplotlib.dates as mdates
REPORT_DIR = Path("reports/charts")
REPORT_DIR.mkdir(parents=True, exist_ok=True)
def plot_bar_chart(df, x_column, y_column, title, x_label, y_label):

    plt.figure(figsize=(8, 5))
    plt.bar(df[x_column], df[y_column])
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.tight_layout()
    filename = title.lower().replace(" ", "_") + ".png"

    plt.savefig(REPORT_DIR / filename)
    plt.show()
    print(f"Chart saved: {REPORT_DIR / filename}")

def plot_horizontal_bar_chart(df, x_column, y_column,title, x_label, y_label):
    plt.figure(figsize=(8, 5))
    plt.barh(df[x_column], df[y_column])
    plt.title(title)
    plt.xlabel(x_column)
    plt.ylabel(y_label)
    plt.tight_layout()
    filename=title.lower().replace(" ","_") + ".png"
    plt.savefig(REPORT_DIR / filename)
    plt.show()
    print(f"Chart saved :{REPORT_DIR /filename}")
def plot_pie_chart(df, labels_column, values_column, title):

    plt.figure(figsize=(8, 5))

    labels = df[labels_column]
    values = df[values_column]

    plt.pie(
        values,
        labels=labels
    )

    plt.title(title)


    filename =title.lower().replace(" ","_") + ".png"
    plt.savefig(REPORT_DIR / filename)
    plt.show()
    print(f"Chart Saved:{REPORT_DIR /filename}")

def plot_line_chart(df, x_column, y_column,title,x_label,y_label):
    plt.figure(figsize=(12, 6))
    plt.plot(df[x_column], df[y_column], marker="o")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.gca().yaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f'{x/1000:.0f}K')
          )
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    
    plt.tight_layout()
    filename=title.lower().replace(" ","_") + ".png"
    plt.savefig(REPORT_DIR / filename)
    plt.show()
    print(f"Chart saved :{REPORT_DIR /filename}")






