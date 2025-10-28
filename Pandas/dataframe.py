import pandas as pd 

data={
    'name':["Mega manan","didi","bella"],
    'age':[16,21,29],
    'section':['A','B','A'],
    'isGod':[True,False,False]
}

df=pd.DataFrame(data)

print(df.head())
print("------------------")
print(df.tail())
print("------------------")
print(df.info())
print("------------------")
print(df.describe())
print("------------------")
# print(df.columns())
# print("------------------")
# print(df.shape())
print("------------------")
df['marks']=[98,90,91]
print(df)


# iloc function
print(df.iloc[1])


# for converting dataset or data in csv file 
df.to_csv('firstcsv')

# for converting into html
df.to_html('firsthtml')

# for converting into json
df.to_json('firstjson.json')

# for pritning specific value from head or tail of dataframe we
# use parameter values
print("***********************")
print(df.head(1))
print("*******************")
print(df.tail(3))



# reading other csv file
newdata=pd.read_csv('firstcsv.csv')
print("------------------------")
print(newdata)


import numpy as np
ser1=pd.Series(np.random.rand(10))
print(ser1.head(5))
print("---------------------------------------------------")
newdf=pd.DataFrame(np.random.rand(30,5),index=np.arange(30))
print(newdf.head())


