
# Q1. Import data from the url- "http://winterolympicsmedals.com/medals.csv"

import numpy as np
import pandas as pd
medals = pd.read_csv("http://winterolympicsmedals.com/medals.csv")

print(medals)

# (a)	Print the information of the data.
medals.info()

# (b)	Check the number of rows and columns.
medals.shape

# (c)	Check the variable formats.
medals.dtypes

# (d)	Print the count of different data types.

medals.dtypes.values_count()

# (e)	Check if there are null values. Remove the rows that contain null values.

medals.isnull()
medals.isnull().value_counts()
medals.dropna()

# (f) Check if the values in ‘sport’ are unique.
medals["Sport"].is_unique
medals["Sport"].str.contains("Skating")


# Q2. Import cs-training.csv file.

t = pd.read_csv("CS-traning.csv")
print(t)

# (a) Print the information of the data.

t.info()


# (b)	What are number of rows and columns?
t.shape

# (c)	Are there any suspicious variables
t["NumbersOfDependents"].isnull().value_count()

# Display the variable formats

t.dtypes
# e) Print the first 10 observations
t.head(10)

# (f)	What are the categorical , discrete and continuous variables?

dd = t.select_dtypes(exclude=[np.float64])
dd.shape[1]

cd = t.select_dtypes(exclude=[np.number])
cd.shape[1]

ctd = t.select_dtypes(include=[np.float64])
ctd.shape[1]

# Find the frequencies of all class variables in the data
t["DebtRatio"].value_counts()

t["NumbersOfTime60-89PastDueNotWorse"].value_counts()
t["MouthlyIncome"].value_counts()

# (g)	Are there any variables with missing values?
t.info()

# (i)	Find summary statistics for each discrete variable. Min, Max, Median, Mean, sd, Var?

t.describe()
print(t.var())

t["MonthlyIncome"].isnull().value_counts()

t["MothlyIncome"].isnull().sum()
len(t)
p = t["MonthlyIncome"].isnull().sum() / len(t)
print(p*100)

t["RevolvingUtilizationOfUnsecuredLines"].quantile(
    [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

td = t["RevolvingUtilizationOfUnsecuredLines"] > 1
td.value_counts()

a = t["MonthlyUtilization"] = t["RevolvingUtilizationOfUnsecuredLines"]

t["MonthlyUtilization"][td] = a
t["MonthlyUtilization"].quantile(
    [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])


""" (k)	Find the missing value percentage in monthly income. Create an indicator variable for missing and non-missing. Replace the missing values with median
 """

t["NullIndicator"] = 0
med = t["MonthlyIncome"].median()
med

t["MouthlyIncome"]
