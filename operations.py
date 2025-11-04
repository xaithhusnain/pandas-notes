import numpy as np 
import pandas as pd 

df1 = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
})

# print(df1)
# print(df1.shape)
# print(df1.columns)
# print(df1.info())
# print(df1.describe())
# df1 = df1[['A','B','C']] + 10
# print(df1)




# DataFrames Applying Functions

def square(x):
    return x**2

df = df1[['A','B','C']].apply(square)
# print(df)

# df1['B'] = df1['B'].apply(square)
# print(df1)

# adding new column
# df1['D'] = df1['B'].apply(square)
# print(df1)

df1['D'] = df1['B'].apply(lambda x :x**2)
print(df1)


