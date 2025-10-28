# from sklearn.linear_model import LinearRegression
# import numpy as np


# X = np.array([
#     [1, 22],
#     [2, 25],
#     [3, 28],
#     [4, 30],
#     [5, 35]
# ])


# y = np.array([25, 45, 65, 75, 110])


# model = LinearRegression()

# model.fit(X, y)

# print("Predicted Salary (in 1000s):", model.predict([[6, 40]]))

# print("Coefficients (m1, m2):", model.coef_)
# print("Intercept (c):", model.intercept_)


# import matplotlib.pyplot as plt

# y_pred = model.predict(X)

# plt.scatter(y, y_pred, color="blue")
# plt.xlabel("Actual Salary")
# plt.ylabel("Predicted Salary")
# plt.title("Actual vs Predicted Salary")
# plt.show()  




import sklearn
from sklearn.linear_model import LinearRegression 
from sklearn.datasets import load_iris
# loading iris data set
iris=load_iris()
X,y=load_iris(return_X_y=True)
model=LinearRegression()
model.fit(X,y)
print(model.predict(X))


from sklearn.neighbors import KNeighborsRegressor
mod=KNeighborsRegressor()

# to make close prediction we use KNeighborsRegressor function 
mod.fit(X,y)
print(mod.predict(X))

import pandas as pd 

from sklearn.datasets import fetch_openml
df=fetch_openml('titanic', version=1, as_frame=True)['data']
print(df)
