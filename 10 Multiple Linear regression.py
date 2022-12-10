import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn.model_selection as sel
import sklearn.lineaar_model as lin

AP= pd.read_csv("filePath")
AP

AP.drop(["Week_num"], axis=1)

y= AP["Passengers"]
y

x= AP[["Promotion_Budget", "Service_Quality_Score", "Inter_metro_flight_ratio"]]
x


xtrain, xtest, ytrain, ytest = sel.train_test_split(x,y, trst_size=0.2)
xtrain, xtest, ytrain, ytest


model = lin.LinearRegression()
model.fit(xtrain, ytrain)
model.score(xtest, ytest)