# **Pandas** 

**for installation we use**

windows :- ``` pip install pandas```

linux :- ```pip3 install pandas```

google-colab :- ```!pip install pandas```

----------------------------------------------------------

**for importing we use**

```import pandas as pd```

where pd is the alias name 

----------------------------------------------------------

**for knowing the version of pandas**

```pd.__version__```

----------------------------------------------------------

**Series : more like a single columns with values**

**Dataframe : combination of rows and columns**

----------------------------------------------------------

**Creating a dataframe**

```py

df=pd.DataFrame([1,2,3,4,5],columns=['Cols'])
print(df)
```

----------------------------------------------------------

**Checking data type of dataframe**

``` print(type(df))```

----------------------------------------------------------

**to get first 5 values from a dataframe**

``` df.head()```

and to get specific values from start we use index value 

``` df.head(2)```

----------------------------------------------------------

**to get last 5 values from a dataframe**

``` df.tail()```

and to get specific values from end we use index values 

``` df.tail(3)```

----------------------------------------------------------

**to get columns name**

``` df.columns```

**to get dimensional data in row and columns as format**

```df.shape```

**to get information of dataframe**

```df.info()```

**to get the description data of whole dataframe**

``` df.describe()```

----------------------------------------------------------

**to rename a columns in dataframe**

```py
df.rename(columns=['salary':'wages'),inplace=True)
```
(we use inplace in order to make changes permanent, if it's false then it wont
and for default it's always False)

----------------------------------------------------------


**to save data in csv format**

```df.to_csv('file_name.csv')```


**to remove indexing from our data and saving this format we use**

``` df.to_csv('file_name',index=False)```


**to load data file of csv format**

``` df.read_csv('file_name.csv')```

----------------------------------------------------------

**to print single column**

```df['Column_name']```

**to print two columns**

```df[['col1_name','col2_name]]```

----------------------------------------------------------

**to select rows**

```df.loc[1]```
this will return row with 1st index value


**to select row with specific value**

``` df.loc[df.Name=='P']```

----------------------------------------------------------

**to apply condition on rows or values**

```py
df.loc[(df.Age==12) & (df.Marks==340)]
```

----------------------------------------------------------

**to apply slicing**

```df.iloc[0:2]```

iloc does not use the last value of index but on other hand loc does use this

----------------------------------------------------------

**to add new column in dataframe**

```df['new_col_name']=[values]```

**to add values in existing values**

```df['Bonus']=df['Marks']+200```

----------------------------------------------------------

**to add rows**

``` df.loc[len(df)]=['K',18,590,'E',560]```

----------------------------------------------------------

**to update values using index**

```df.loc[0,'Name']='I'```

**to update values using columns**

```df.loc[df.Name=='N','Name']='J'```

----------------------------------------------------------
