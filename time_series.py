import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date")
df.index = pd.to_datetime(df.index)

# Clean data
df = df.loc[(df["value"] >= df["value"].quantile(0.025)) &
            (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    df_line = df.copy()
    fig, ax = plt.subplots()
    plt.plot(df_line.index, df_line["value"])
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["month"] = df_bar.index.month
    df_bar["year"] = df_bar.index.year

    # Draw bar plot
    fig, ax = plt.subplots()
    sns.barplot(x="year", y="value", data=df_bar, hue="month", ci=None)
    plt.legend(labels=["January", "February", "March", "April", "May", "June", "July", "August",
                       "September", "October", "November", "December"])
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2)
    boxplot1 = sns.boxplot(x="year", y="value", data=df_box, ax=ax[0])
    boxplot1.set(xlabel="Year", ylabel="Page Views", title="Year-wise Box Plot (Trend)")

    order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    boxplot2 = sns.boxplot(x="month", y="value", data=df_box, order=order, ax=ax[1])
    boxplot2.set(xlabel="Month", ylabel="Page Views", title="Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
