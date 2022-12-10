""" 
. Consider a problem related to test the claim of a company manufacturing motorcycles. The company claims that its motorcycles give an average mileage of 60km/liter. For testing the claim of the company, an analyst randomly selects 24 motorcycles of the company and records their mileage. The data so obtain is given in Mileage.csv. Assuming that the mileage of the motorcycles is normally distributed, Formulate the null and alternative hypothesis. Use suitable test for testing the claim of the company at 5% level of significance."""


import pandas as pd
import numpy as np

import scipy . stats as stats

d = pd.read("File Path")
d


T, P = stats.ttest_1samp(d["Milenage"], 60)
T, P

round(4.807211107069967e-27)

if P < 00.25:
    print("Reject")
else:
    print("Accept")


""" Q2. In a packaging plant, a machine packs cartons with jars. It is supposed that a new machine would pack faster on the average than the machine currently used. To test the hyposthesis, the time it takes for each to pack ten cartons are recorded. The result in seconds is as follows:
New Machine	Old Machine
42.1	42.7
41	43.6
41.3	43.8
41.8	43.3
42.4	42.5
42.8	43.5
43.2	43.1
42.3	41.7
41.8	44
42.7	44.1 
"""


df = pd.read_csv("File Path")
df

NM = df["New Machine"].var()
NM

OM = df["Old Machine"].var()
OM

t, p = stats.ttest_ind(a=df["New Machine"],
                       b=df["Old Machine"], equal_var=False)
t, p

if p < 0.05:
    print("Reject")
else:
    print("Accept")
