import numpy as np
import pandas as pd

data = {
    'Date': pd.date_range('2023-01-01', periods=20),
    'Product': ['A', 'B', 'C', 'D'] * 5,
    'Region': ['East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West',
               'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
    'Sales': np.random.randint(100, 1000, 20),
    'Units': np.random.randint(10, 100, 20),
    'Rep': ['John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary',
            'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice']
}

df = pd.DataFrame(data)
df['Month'] = df['Date'].dt.month_name()
df['Quarter'] = 'Q' + df['Date'].dt.quarter.astype(str)
# print(df)

PT = pd.pivot_table(df,values="Sales",index="Region",columns="Product",aggfunc="min")
# print(PT)


PT = pd.pivot_table(df,values=["Sales","Units"],index="Region",columns="Product",aggfunc="min")
print(PT)

# we can't use nothing but numbers in pivot tables bcz here is aggfunctions are done




# CROSS TABS 

CT = pd.crosstab(df["Region"],df["Product"])
CT = pd.crosstab(df["Region"],df["Rep"])
print(CT)