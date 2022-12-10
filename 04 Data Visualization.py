import numpy as np
import pandas as pd
import matplotlib as plt

d = pd.read_csv("// File Path")
d

# (a)	Plot a histogram for the total count based on “Geography”.

d["Geography".hist(bins=3, edgecolor="black")]

# (b)	Plot a pie chart to visualize the count of people below the age of 40, between 40 to 50 and

lessthan40 = d["Age"] < 40
lessthan40.sum()

greaterthan50 = ["Age"] > 50

greaterthan50.sum()
btw40Or50 = (50 > d["Age"]) & (d["Age"] > 40)
btw40Or50.sum()

values = [lessthan40.sum(), greaterthan50.sum(), btw40Or50.sum()]
label = ['Age<40', 'Age >50 ', 'Between 40 Or 50']

plt.pie(values, label=label)
plt.show()

# (c)	Plot a box plot for customer credit score.

plt.boxpolt(d["CreditScore"])

g = (d["Gender"] == 'Male').sum()
g
h = (d["Gender"] == 'Female').sum()
h

plt.bar(["Male", "Female"], [g, h])

# (e)	Plot a scatter plot for

# a.	Credit score and age
plt.scatter(d["CreditScore"], d("Age"))
plt.show()

# b.	Number of products and estimated salary.

plt.scatter(d["NumberOfProducts"], d("EstimatedSalary"))
plt.show()

# Q2 Import A.csv file and plot a line chart for the close value and volume.
plt.plot(d["Date"], d["Close"])
plt.show()

plt.ploat(d["Date"], d["Volume"])
