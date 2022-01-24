import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    plt.scatter(data=df, x="Year", y="CSIRO Adjusted Sea Level")

    # Create first line of best fit
    first_line = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_vals1 = range(1880, 2050)
    y_vals1 = x_vals1*first_line.slope + first_line.intercept
    plt.plot(x_vals1, y_vals1)

    # Create second line of best fit
    df_second = df.loc[df["Year"] >= 2000]
    second_line = linregress(df_second["Year"], df_second["CSIRO Adjusted Sea Level"])
    x_vals2 = range(2000, 2050)
    y_vals2 = x_vals2*second_line.slope + second_line.intercept
    plt.plot(x_vals2, y_vals2)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.xticks(ticks=[1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    plt.show()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


draw_plot()
