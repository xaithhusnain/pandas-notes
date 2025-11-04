import numpy as np 
import pandas as pd 

data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Store': ['S1', 'S1', 'S2', 'S2', 'S1', 'S2', 'S2', 'S1'],
    'Sales': [100, 200, 150, 250, 120, 180, 200, 300],
    'Quantity': [10, 15, 12, 18, 8, 20, 15, 25],
    'Date': pd.date_range('2023-01-01', periods=8)
}
df = pd.DataFrame(data)
print(df)

#Group by category and cal sum the sales
# when we use gruopby() is dose not create a df it create an object

ct = df.groupby("Category")["Sales"].sum()
print(ct)

'''
for i, v in ct:
    print(i)
    print(v)

'''

#Group by Store and cal sum the sales
ct = df.groupby("Store")["Sales"].sum()
print(ct)

# #Group by multiples column 
ct = df.groupby(["Category","Store"])["Sales"].sum()
print(ct)