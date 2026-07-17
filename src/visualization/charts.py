import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import FuncFormatter
import matplotlib.dates as mdates
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
    ax.set_xlabel(x_column)
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


def plot_line_chart(df, x_column, y_column,title,x_label,y_label):
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(df[x_column], df[y_column], marker="o")
    ax.set_title(title)
    set.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.gca().yaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f'{x/1000:.0f}K')
          )
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

    plt.xticks(rotation=45)
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    
    plt.tight_layout()
    filename=title.lower().replace(" ","_") + ".png"
    plt.savefig(REPORT_DIR / filename)
    #plt.show()
    print(f"Chart saved :{REPORT_DIR /filename}")
    return fig






