import pandas as pd

df1 = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie']
}, index=[1, 2, 3])

# Second DataFrame
df2 = pd.DataFrame({
    'score': [85, 90, 75]
}, index=[2, 3, 4])

print(df1)
print(df2)

j = df1.join(df2)
print(j)

j = df2.join(df1)
print(j)

j = df1.join(df2,how="outer")
print(j)



