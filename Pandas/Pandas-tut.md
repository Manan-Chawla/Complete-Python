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

```py
pd.__version__
```

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

```py
print(type(df))
```

----------------------------------------------------------

**to get first 5 values from a dataframe**

```py
df.head()
```

and to get specific values from start we use index value 

```py
df.head(2)
```

----------------------------------------------------------

**to get last 5 values from a dataframe**

```py
df.tail()
```

and to get specific values from end we use index values 

```py
df.tail(3)
```

----------------------------------------------------------

**to get columns name**

```py
df.columns
```

**to get dimensional data in row and columns as format**

```py
df.shape
```

**to get information of dataframe**

```py
df.info()
```

**to get the description data of whole dataframe**

```py
df.describe()
```

----------------------------------------------------------

**to rename a columns in dataframe**

```py
df.rename(columns=['salary':'wages'),inplace=True)
```
(we use inplace in order to make changes permanent, if it's false then it wont
and for default it's always False)

----------------------------------------------------------


**to save data in csv format**

```py
df.to_csv('file_name.csv')
```


**to remove indexing from our data and saving this format we use**

```py
df.to_csv('file_name',index=False)
```


**to load data file of csv format**

```py
df.read_csv('file_name.csv')
```

----------------------------------------------------------

**to print single column**

```py
df['Column_name']
```

**to print two columns**

```py
df[['col1_name','col2_name]]
```

----------------------------------------------------------

**to select rows**

```py
df.loc[1]
```
this will return row with 1st index value


**to select row with specific value**

```py
df.loc[df.Name=='P']
```

----------------------------------------------------------

**to apply condition on rows or values**

```py
df.loc[(df.Age==12) & (df.Marks==340)]
```

----------------------------------------------------------

**to apply slicing**

```py
df.iloc[0:2]
```

iloc does not use the last value of index but on other hand loc does use this

----------------------------------------------------------

**to add new column in dataframe**

```py
df['new_col_name']=[values]
```

**to add values in existing values**

```py
df['Bonus']=df['Marks']+200
```

----------------------------------------------------------

**to add rows**

```py
df.loc[len(df)]=['K',18,590,'E',560]
```

----------------------------------------------------------

**to update values using index**

```py
df.loc[0,'Name']='I'
```

**to update values using columns**

```py
df.loc[df.Name=='N','Name']='J'
```

----------------------------------------------------------

**to delete values by index**

```py
df.drop(4)
```

**to delete column with column name**

```py
df.drop('Bonus',axis=1,inplace=True)
```

----------------------------------------------------------

**to sort values**

```py
df.sort_values('Marks')
```

by default it's in ascending order and if you want to make it descending then you have to apply this attribute
```py
df.sort_values('Marks',ascending=False)
```

----------------------------------------------------------

**working with date and time**

```py
df['DOJ']=['2024-01-02','2024-08-10','2025-10-12','2026-10-14','2026=03-12']''

df['DOJ'].dtype
# this is Object type

df['DOJ']=pd.to_datetime(df['DOJ'], errors='coerce', format='mixed')
# here we are converting into date time format
print(df['DOJ'])
```

**extracting date,month,year,day from data**

```py
df['DOJ'].dt.year  # year

df['DOJ'].dt.year  # year

df['DOJ'].dt.day  # day

df['DOJ'].dt.day_name() #day by day names
```

----------------------------------------------------------

**to handle missing values**

```py
df.isnull()
```

**to handle duplicated values**

```py
df.duplicated()
```

**to know all null values in large dataset**

```py
df.isnull().sum()
```

**to fill missing values**

```py
df.fillna(0)
```

----------------------------------------------------------

**to count values**

```py
df['Name'].value_counts()
```

**to count values using specific values**

```py
df[df['Name']=='P'].value_counts()
```

**to group the values**

```py
df.groupby('Age')['Marks'].sum()
```

**aggregrate which help to apply more condition and getting more ouput**

```py
df.groupby('Marks').agg({'Name':'mean','Name':'count'})
```


**merging and concatentaion**

```py
df1=pd.DataFrame({
    'Name':['A','B','C'],
    'Age':[19,20,22]
})
df1


df2=pd.DataFrame({
    'Name':['A','B','C'],
    'Score':[98,89,95]
})
df2

pd.concat([df1,df2],axis=0)
# it just merge dataset without any logic
# more like direct copy and paste 
# this is applying as top on top/ vertical

pd.concat([df1,df2],axis=1)
# this is applying on side on side/ horizontal

# merge also refer as join
pd.merge(df1,df2,how='inner',on='Name')

# custom merge if there are two differnt columns
pd.merge(df1,df2,how='inner',left_on='Name',right_on='Name')


----------------------------------------------------------
