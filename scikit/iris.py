import sklearn
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression

X,y=load_iris(return_X_y = True)
# it will automatically stored data in X and y 

model=LinearRegression()

model.fit(X,y)

print(model.predict(X))

import matplotlib.pyplot as plt

# plt.plot(model.predict(X))
# plt.show()

pred=model.predict(X)
plt.violinplot(pred,y)
plt.show()