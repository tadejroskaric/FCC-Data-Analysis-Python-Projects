import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby("race").count()
    race_count = pd.Series(data=race_count["age"], index=race_count.index).sort_values(ascending=False)

    # What is the average age of men?
    men = df.loc[df["sex"] == "Male"]
    men_age = men["age"]
    average_age_men = round(men_age.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bach = df.loc[df["education"] == "Bachelors"]
    percentage_bachelors = round(len(bach) / len(df) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    bach = df.loc[df["education"] == "Bachelors"]
    master = df.loc[df["education"] == "Masters"]
    doctor = df.loc[df["education"] == "Doctorate"]
    advanced_educ = bach + master + doctor
    advanced_educ_rich = advanced_educ.loc[df["salary"] == ">50K"]
    advanced_educ_rich_percentage = round(len(advanced_educ_rich) / len(advanced_educ) * 100, 1)

    # What percentage of people without advanced education make more than 50K?
    more_than_50k = df.loc[df["salary"] == ">50K"]
    more_than_50k_normal_percentage = (len(more_than_50k) - len(advanced_educ_rich)) / (len(df) - len(advanced_educ)) * 100
    more_than_50k_normal_percentage = round(more_than_50k_normal_percentage, 1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    higher_education = advanced_educ
    lower_education = len(df) - advanced_educ

    # percentage with salary >50K
    higher_education_rich = advanced_educ_rich_percentage
    lower_education_rich = more_than_50k_normal_percentage

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    hours_weekly = df["hours-per-week"]
    min_work_hours = hours_weekly.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df["hours-per-week"] == min_work_hours]
    num_min_workers_rich = num_min_workers.loc[df["salary"] == ">50K"]
    rich_percentage = len(num_min_workers_rich) / len(num_min_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    country = df.groupby("native-country").count()
    country = pd.Series(data=country["age"], index=country.index)

    salary = df.loc[df["salary"] == ">50K"]
    country_rich = salary.groupby("native-country").count()
    country_rich = pd.Series(data=country_rich["age"], index=country_rich.index)

    highest_earning_country_percentage = round((country_rich / country) * 100, 1).sort_values(ascending=False)
    highest_earning_country = highest_earning_country_percentage.idxmax()
    highest_earning_country_percentage = highest_earning_country_percentage.max()

    # Identify the most popular occupation for those who earn >50K in India.
    salary = df.loc[df["salary"] == ">50K"]
    country = salary.loc[df["native-country"] == "India"]
    job = country["occupation"]
    top_IN_occupation = job.describe().top

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

