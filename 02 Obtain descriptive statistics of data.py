""" 
Q1. Import Income_data.csv
(a)	Print mean of capital gain.
(b)	Print median of capital gain.
(c)	Print percentiles of capital gain.
"""
import pandas as pd
import numpy as np

data = pd.read_csv("//PATH")

data["capital-gain"].mean()

data["capital-gain"].median()

np.percentile(data["capital-gain"], [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

np.percentile(data["hours-per-week"],
              [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

"""
Q2. Import Dataset:  Online Retail.csv
(a)	What is the variance and s.d of “UnitPrice” ?
(b)	What is the variance and s.d of “Quantity”?
"""
R = pd.read_csv("OnlineRetail.csv")  # File Path here
np.var(R["UnitPrice"])
np.std(R["UnitPrice"])

np.var(R["Quantity"])
np.std(R["Quantity"])

# Q3 Profit details of two companies A & B for last 14 Quarters. Which company is more consistent?

groupA = np.array([43, 44, 0, 25, 35, -8, 13, -10, -8, 32, 11, -8, 21])
groupB = np.array([17, 15, 12, 17, 15, 18, 12, 13, 18, 18, 14, 14])

print(np.var(groupA))
print(np.var(groupB))


""" 
Q4 Import GDP.csv
(i) Compute the mean and standard deviation for Albania, Bulgaria, Croatia, and Czech Republic.
(ii) Compute the mean and standard deviation for Hungary, Poland, Romania, and Bosnia/Herzegovina.
(iii) Use a coefficient of variation to compare the two standard deviations.
"""

d = pd.read_csv("D:GDP.csv")  # path file
print(d)
D1 = d.loc[0:3]
print(D1)

np.mean(D1["Per_Capital_GDP"])
np.std(D1["Per_Capital_GDP"])

D2 = d.loc[4:7]
print(D2)

np.mean(D2["Per_Capital_GDP"])
np.std(D2["Per_Capital_GDP"])

print(np.std(D1["Per_Capital_GDP"])/np.mean(D1["Per_Capital_GDP"]))

print(np.std(D2["Per_Capital_GDP"])/np.mean(D2["Per_Capital_GDP"]))

""" 
Q5 Import port.csv
(i) Construct a box-and-whisker plot for these data.
(ii) Discuss the shape of the distribution from the plot.
(iii) Are there outliers?
"""

p = pd.read_csv("port.csv")
p.boxplot()

""" 
Q6.Import the Data https://raw.githubusercontent.com/gedeck/practical-statistics-for-data-scientists/master/data/state.csv 
(i) Compute the mean, 10% trimmed mean, and median for the population.
(ii) Compute the average murder rate for the country.
(iii) Compute the standard deviation, interquartile range (IQR), and the median absolution deviation from the median of the population.
(iv) Display 5th, 25th, 50th, 75th, 95th percentile of the murder rate by state.
(v) Use Boxplot to visualize the distribution of data. Write down your observations.
"""
S = pd.read_csv("https://raw.githubusercontent.com/gedeck/practical-statistics-for-data-scientists/master/data/state.csv")

S["Population"].mean()
S["Population"].median()

stats.trim_mean(S.Population, 0.1)

S["Murder.Rate"].mean()
np.average(S["Murder.Rate"], weights=S["Population"])

S["Murder.Rate"].std()

q1 = np.percentile(S["Population"], 25)
q1()

# q2 = np.percentile(S["Population"], 50)
q3 = np.percentile(S["Population"], 70)

Iqr = q3-q1
Iqr

mad = abs(S["Murder.Rate"], [5,25,50,6,75,95])

S.boxplot()
