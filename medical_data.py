import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
meters = df["height"] / 100
BMI_value = df["weight"] / meters ** 2
BMI = pd.Series(data=BMI_value)
df["overweight"] = BMI.apply(lambda x: 1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad.
# If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = df["cholesterol"].apply(lambda x: 1 if x > 1 else 0)
df["gluc"] = df["gluc"].apply(lambda x: 1 if x > 1 else 0)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just
    # the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"], id_vars="cardio")

    # Group and reformat the data to split it by 'cardio'.
    # Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.

    df_cat = pd.DataFrame(df_cat.groupby(['variable', 'value', 'cardio'])["variable"].count())
    df_cat = df_cat.rename(columns={"variable": "total"})
    df_cat = df_cat.reset_index()

    # Draw the catplot with 'sns.catplot()'
    sns.catplot(x="variable", y="total", col="cardio", hue="value", data=df_cat, kind="bar")

    # Do not modify the next two lines
    plt.savefig('catplot.png')
    return plt.gcf()


# Draw Heat Map
def draw_heat_map():

    # Clean the data
    df_heat = df
    df_heat = df_heat.loc[df['ap_lo'] <= df['ap_hi']]
    df_heat = df_heat.loc[df['height'] >= df['height'].quantile(0.025)]
    df_heat = df_heat.loc[df["height"] <= df["height"].quantile(0.975)]
    df_heat = df_heat.loc[df["weight"] >= df["weight"].quantile(0.025)]
    df_heat = df_heat.loc[df["weight"] <= df["weight"].quantile(0.975)]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with
    sns.heatmap(corr, annot=True, mask=mask, fmt=".1f")

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
