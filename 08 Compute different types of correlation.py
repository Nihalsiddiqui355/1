import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

AP = pd.read_csv("File Path")
AP

# (a)	Find the correlation between number of passengers and promotional budget using Pearson correlation coefficient.
PP = stats.pearson(AP["Passenger"], AP["Promotion_Budget"])
PP

plt.scatter(AP["Passenger"], AP["Promotion_Budget"])

# (b)	Find the correlation between number of passengers and Holiday week using Spearman's rank correlation coefficient
ph = stats.spearmanr(AP["Passenger"], AP["Holiday_week"])
ph
plt.scatter(AP["Passenger"], AP["Holiday_week"])


# (c)  Find the correlation between number of passengers and Bad Weather Indicator.

tt = stats.spearmanr(AP["Passenger"], AP["Bad_Weather_Ind"])

plt.scatter(AP["Passenger"], AP["Bad_Weather_Ind"])
