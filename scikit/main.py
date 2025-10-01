# Scikit-learn 
'''
It is a python programming library which is used to implement machine learning models.
It was created as a project in GSOC.
Without this library implementation of machine learning in python is quiet difficult.

We have to use some libaray with this such as numpy, pandas and matplotlib.
The major part of implementing ML logic and generating an output of it will be achieved with the help of scikit-learn
and without this it's the process will take so much time.

To install scikit-learn using pip write following command in terminal :-
pip intall scikit-learn

To check whether scikit-learn installed or not run this command in terminal :-
python -m pip show scikit-learn

Scikit-learn majorly use for following tasks within ML :-
1. Classification
Classification involves teaching a computer to categorize things

2. Regression
Regression predicting numbers based on other numbers.

3. Clustering
Clustering involves finding patterns in data and grouping similar items together.

4. Diensionality Reduction 
Dimensionality reduction helps focus on essential data parts while discarding noise. 
This is useful when dealing with a lot of data that isn't all relevant.



# Feature of scikit learn
1. classification 
It use to categorize data into groups or label.
For example : by this mail can specify which email is spam or not

2. Regression
It is used to predict continuous values, like we predict stock price or 
temperature tomorrow.

3. Clustering 
It is used to group similar things without using grouping or labeling
Like we group new articles by genre or topics automatically.

4. Model Selection
It is a tool use to choose the best model using train/test split and cross validation
Like we check on imdb to cross check movies as per our genre
'''


# let's create first code in scikitlearn

# first we are importing linearregression from scikit-learn library
# it is a algo that find best fit straing line thought data
# generally use to make predicition

from sklearn.linear_model import LinearRegression
import numpy as np

# let's create a student data or study
# X = np.array([[1],[2],[3],[4],[5]])
# # here each small list represent hours of study
# # we need to create double brackets as scikit-learn expect to use
# # 2d array

# # another data of marks obtain
# y = np.array([20, 40, 60, 80, 100])
# # here we didn't store element in 2d array
# # as it represent that if a student study for 1 hour he or she will get
# # 20 marks and so on with other hours

# # now we have to create a model
# model=LinearRegression()

# # let's train our model with x and y data
# model.fit(X, y)
# fit method takes data 
# it will find best equation
# here it's using  y=m * x + c where m is slope and c is intercepy

 
# let's print predict marks if someone studis for 8 hours

# print("Predicted Marks:", model.predict([[8]]))

import matplotlib.pyplot as plt

# # Plot original points
# plt.scatter(X, y, color='blue', label='Data Points')

# # Plot regression line
# plt.plot(X, model.predict(X), color='red', label='Best Fit Line')

# plt.xlabel("Hours Studied")
# plt.ylabel("Marks Scored")
# plt.legend()
# plt.show()


'''
workflow of scikit-learn
1. import (choosing algo)
2. Prepare Data ( X and y where X is feature and y is target )
3. Split Data ( train and test )
4. Train ( Fit the model to work on data )
5. Predict ( Use model to make predicitons )
6. Evaluate ( to check accuracy or error )
'''


# here we are importing inbuilt dataset named 'iris'
# it contains measurements of flower like petal length , width etc
# flower type are setosa, versicolor, virginica
# from sklearn.datasets import load_iris

# # here we are importing train_test_split which
# # splits data into training set and testing set 
# # so that model works properly
# from sklearn.model_selection import train_test_split

# # importing logic regression
# from sklearn.linear_model import LogisticRegression

# # let's load dataset first
# iris=load_iris()
# # this will load data

# X=iris.data  # it will load feature
# y=iris.target # it will target the flower type

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# # here 
# '''
# X_train and y_train are the training sets
# X_test and y_test are testing set
# test_size=0.2 specify that we are using
# 20% data for testing and 80% for training
# '''

# # let's train model using logicregression
# model = LogisticRegression(max_iter=2000)
# # this will run till 2000 iteration

# model.fit(X_train,y_train)

# # printing 
# print("Accuracy:", model.score(X_test, y_test))

# plt.plot(X,model.predict(X))
# plt.show()

