import numpy as np


# Function to calculate mean, var, std dev. etc.


def calculate(values):
    if len(values) != 9:
        raise ValueError("List must contain nine numbers.")
    # Numpy array (matrix)
    x = np.array(values)
    x.shape = (3, 3)

    # Sum of columns (0) and sum of rows (1), total sum
    sum_0 = list(x.sum(axis=0))
    sum_1 = list(x.sum(axis=1))
    sum_2 = x.sum()

    mean_0 = list(x.mean(axis=0))
    mean_1 = list(x.mean(axis=1))
    mean_2 = x.mean()

    var_0 = list(x.var(axis=0))
    var_1 = list(x.var(axis=1))
    var_2 = x.var()

    std_0 = list(x.std(axis=0))
    std_1 = list(x.std(axis=1))
    std_2 = x.std()

    max_0 = list(x.max(axis=0))
    max_1 = list(x.max(axis=1))
    max_2 = x.max()

    min_0 = list(x.min(axis=0))
    min_1 = list(x.min(axis=1))
    min_2 = x.min()

    # Output dictionary
    output = {
        "mean": [mean_0, mean_1, mean_2],
        "variance": [var_0, var_1, var_2],
        "standard deviation": [std_0, std_1, std_2],
        "max": [max_0, max_1, max_2],
        "min": [min_0, min_1, min_2],
        "sum": [sum_0, sum_1, sum_2]}

    return output

