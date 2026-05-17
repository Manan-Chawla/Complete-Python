# Machine Learning
Machine learning is a subdomain of computer science that focus on algorithms which helps a computer learns from data without explicit programming.

# AI
AI or Artificial Intelligence is an area of computer science, where the goal is to make computer to perform human like task or showcase human like behavior.


```py
Machine learning is subset of AI that tries to solve a specific problem and make prediction using the data.
```

# Data Science
It is field that attempt to find pattern and draw insights from data (might use ML too).


```py
All fields overlap! all may use ML
```

# Types of machine learning
1. **Supervised learning** :-
Use label input to train models and learn outputs.

2. **Unsupervised learning** :-
It does not use lavel input inorder to train models and learn outputs. 

3. **Reinforcement learning** :-
Agent learning in interactive enviorments based on rewards and penalties.

--

## **Supervised learning**
Think of it as some inputs let say 'n' inputs which enters into a model and then model train on those inputs and give us a predicition or output.
```py
For example we are taking temperature of six days and basis on that we will predict what can be the temperature of seventh day.
```

There are some features need to understand
1. **Qualitative** :- a categorical data where we have finite number of groups or categorical.
It's more like nominal data.
we use **One hot encoding** for such operation.

2. **Ordinal** :- a data where we have some inherting order system.
More like a person's age and its life span.


3. **Quantative** :- Numerical valued data , could be discrete or continuous.
like a measuring tape and some eggs.


```
ML models are so advanced and good to understand numberical based data rather than how human actually understand data
```


# **Types of predicition**
1. **classification** : which predicts discrete classes.
It have two more types:-
   1. Binary classification
   output will be like 0 and 1 or only two options
   2. Multiclass classification
   output can be more than two options

2. **Regression** :-
It predicts continous values, for example pricing of house can be changes day by day.


```
 we never take complete data in order to train any model as, it require to work on various data. So if we provide all data to model, it become a static model which works only on that data
 ```

```
So we genrally advice to took 20% of data for training and rest to keep
```


## **Validation** :-
Validation set used as a reality check during/after training to ensure model can handle unseen data.

```
The model which showcase least loss after training data, refer as best model.
For example
we have created four model and model score are as follows :- 1.3, 1.5, 0.5, 0.9
By this we have seen that third model is best as its score is least in compare to other.
```

```
we get **test set**, which is used as to check how generalizable the final chosen model is.

we can say that test set, is more like a data which our model never see, and the output will give us a value which show that how our model work even on data it never seen.
```


```py

L1 LOSS
Loss = sum(|Y(real) - y(predicted)|)


L2 LOSS
Loss = sum((y(real) - y(predicted)^2)
```


## **Metrics of Performance of Model using pictorial presentation** :-
<img src="1.png" height="300px" width="300px" style="border:2px solid red;">
