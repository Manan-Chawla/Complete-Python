import pandas as pd

data={
    'name':['anshika','ananya','akanksha','priya','manan ji mahan'],
    'math':[89,86,89,56,200],
    'physics':[99,89,89,46,-100],
    'chemistry':[100,200,0,89,-200]
}

df=pd.DataFrame(data)
# passing data

print(df)

# total
# average
# sort

df['total']=df[['math','physics','chemistry']].sum(axis=1)
df['average']=df['total']/3

print(df)


def grades(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    else:
        return 'D'
        

df['Grades']=df['math'].apply(grades)
print(df)