import matplotlib.pyplot as plt
import seaborn as sns
import os

# Automatically create folder (only once)
charts_dir = os.path.join(os.path.dirname(__file__), "charts")
os.makedirs(charts_dir, exist_ok=True)

def line_plot(df):
    plt.figure()
    plt.plot(df["Day"], df["Sales"], marker="o")
    plt.title("Sales Trend Over Days")
    plt.xlabel("Day")
    plt.ylabel("Sales")

    plt.savefig(os.path.join(charts_dir, "line_plot.png"), dpi=300)
    plt.show()


def bar_chart(df):
    plt.figure()
    sns.barplot(x=df["Day"], y=df["Sales"])
    plt.title("Sales Comparison by Day")
    plt.xlabel("Day")
    plt.ylabel("Sales")

    plt.savefig(os.path.join(charts_dir, "bar_chart.png"), dpi=300)
    plt.show()


def scatter_plot(df):
    plt.figure()
    plt.scatter(df["Visitors"], df["Sales"])
    plt.title("Visitors vs Sales")
    plt.xlabel("Visitors")
    plt.ylabel("Sales")

    plt.savefig(os.path.join(charts_dir, "scatter_plot.png"), dpi=300)
    plt.show()
