
""" Q1. Consider the following three sets of data
A	71	75	65	69
B	90	80	86	84
C	72	77	76	79
Perform a one-way ANOVA to determine if the mean data is different between the three sets:
"""
import scipy . stats as stats

from scipy.stats import f_oneway

A = [71, 75, 65, 69]
B = [90, 80, 86, 84]
C = [72, 77, 76, 79]

anova = f_oneway(A, B, C)

t, p = anova
if p > 0.025:
    print("no diffrence")
else:
    print("There is difference")

""" 
Q2. We recruit 30 students to participate in a study and split them into three groups. The students in each group are randomly assigned to use one of the three exam prep programs for the next three weeks to prepare for an exam. At the end of the three weeks, all of the students take the same exam. The exam scores for each group are shown below:
 
Perform a one-way ANOVA to determine if the mean exam score is different between the three groups.

"""

S1 = [85, 86, 88, 75, 78, 94, 98, 79, 71, 80]
S2 = [91, 92, 93, 94, 85, 87, 83, 85, 82, 81]
S3 = [79, 78, 88, 94, 92, 85, 83, 85, 82, 81]

STD = f_oneway(S1, S2, S3)
T, P = STD

if P > 0.025:
    print("no diffrence")
else:
    print("There is difference")
