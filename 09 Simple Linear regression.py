import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn.model_selection as sel
import sklearn.lineaar_model as lin

AP = pd.read_csv("FilePath")
AP

# (a)	Draw a scatter plot between Promotion_Budget and Passengers. Is there any pattern between Promotion_Budget and Passengers? Perform linear regression for prediction of number of passengers if the Promotion Budget is estimated as Rs. 5,00,000.

plt.scatter(AP["Passengers"], AP["Promotion_Budget"])

xtrain, xtest, ytrain, ytest = sel.train_test_split(np.array(
    AP["Promotion_Budget"]).reshape(-1, 1), np.array(AP["Passengers"]).reshape(-1, 1), test_size=0.2)

model = lin.LinearRegression()
model.fit(xtrain, ytrain)
model.score(xtest, ytest)

plt.scatter(xtest, ytest)
plt.plot(xtest, model.predict(np.array(xtest).reshape(-1, 1)), color="red")


# (b)	Perform linear regression for Passengers vs Inter_metro_flight_ratio.

xtrain, xtest, ytrain, ytest = sel.train_test_split(np.array(AP["Promotion_Budget"]).reshape(
    -1, 1), np.array(AP["Inter_metro_flih=ght_ratio"]).reshape(-1, 1), test_size=0.2)

model = lin.LinearRegression()
model.fit(xtrain, ytrain)
model.score(xtest, ytest)

plt.scatter(xtest, ytest)
plt.plot(xtest, model.predict(np.array(xtest).reshape(-1, 1)), color="red")
