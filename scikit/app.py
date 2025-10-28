# **linear regression code**
from sklearn.linear_model import LinearRegression
import numpy as np

X=np.array([
    [10],
    [20],
    [30],
    [40],
    [50] 
])

y=np.array([100,200,300,400,500])

model=LinearRegression()

model.fit(X,y)
print("predict marks : ",model.predict([[68]]))

