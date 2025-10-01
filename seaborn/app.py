# Searborn
"""
Searborn is an amazing library for statistical graphics plotting in python,
it provides beautiful default style and color plattes to create more attractive
graphs then matplotlib.

It aims to make visualization the central part of exploring and understanding data.

Installation : 
pip install searborn

There are some libraries that must be installed before using Seaborn. Here we will list out some basics that are a must for using Seaborn. 
Python 3.6 or higher 
numpy (>= 1.13.3) 
scipy (>= 1.0.1)
pandas (>= 0.22.0)
matplotlib (>= 2.1.2) 

"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load sample dataset
df = sns.load_dataset("tips")
print(df.head())


# sns.scatterplot(x="total_bill", y="tip", data=df)
# plt.show()


# sns.set(style="white")

# Generate a random univariate dataset
rs = np.random.RandomState(10)
d = rs.normal(size=100)

# Plot a simple histogram and kde
sns.histplot(d, kde=True, color="m")