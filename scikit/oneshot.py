from sklearn.datasets import load_boston

X,y=load_boston(return_X_y=True)

from sklearn.neighbors import KNeighborsRegressor

mod=KNeighborsRegressor()

mod.fit(X,y)
mod.predit(X)