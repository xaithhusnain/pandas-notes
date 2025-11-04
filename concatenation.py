import pandas as pd

df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2'],
    'C': ['C0', 'C1', 'C2']
})

df2 = pd.DataFrame({
    'A': ['A3', 'A4', 'A5'],
    'B': ['B3', 'B4', 'B5'],
    'C': ['C3', 'C4', 'C5']
})

conct = pd.concat([df1,df2])
print(conct)

conct = pd.concat([df1,df2],axis=1)
print(conct)

conct = pd.concat([df1,df2],axis=0)
print(conct)