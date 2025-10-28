import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("data.csv")
#printing first 5 values
print(df.head())

# getting column as the x and y axis
name=df["name"]
age=df["age"]

# ploting over graph
plt.title("NAME AND AGE GRAPH ")
plt.xlabel("NAME")
plt.ylabel("AGE")
plt.plot(name,age,color="red",marker="*")

# show is used to represent the graph
plt.show()

