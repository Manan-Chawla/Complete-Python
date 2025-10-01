# create a data for
# shop ---> 
# product name
# product price
# product quantity
# then perform operation
# average , sum of prices
# arrange product in price ascending order

import pandas as pd

productlisting={
    'Product-Name':["Dettol","Brush","Paste","Soap","Biscuits","Toast"],
    'Product-Price':[100,200,300,400,500,600],
    'Product-Quantity':[9,8,2,3,5,4]
}

df=pd.DataFrame(productlisting)


df['Total'] = df['Product-Price'] * df['Product-Quantity']

total_price_sum = df['Product-Price'].sum()
average_price = df['Product-Price'].mean()

print("Total of all product prices:", total_price_sum)
print("Average product price:", average_price)

sorted_df = df.sort_values(by='Product-Price')
print("Products sorted by price:\n", sorted_df)
