import pandas as pd



# series : it's like a single column
data1=[10,20,30,40,50]
# pd stands for pandas as we give it alias name pd
# series function use to create series of that list or array
# it will return dtype in the end always
s=pd.Series(data1)
print(s)



# dataframe :  it's like table with rows and column
# return data in the form of table

data={
    'name':["manan","bella","didi"],
    'age':[16,21,29]
}


df=pd.DataFrame(data)
print(df.head())

print(df.describe())




# Some basic function 
# df.head()---> it will show first 5 rows
# df.tail()---> it will show last 5 rows
# df.info()---> summary of data
# df.describe()---> statistical summary
# df.columns()---> show column names only
# df.shape()---> show rows and columns


# it will return name's columne with dtype
print(df['name'])
# for access multiple columns 
print(df[['name','age']])

# by index number we can access 

# it will access index with 0
print(df.loc[0])
# it will access index with 1
print(df.iloc[1])


# for adding new columns
df['score']=[90,98,99]
print(df)