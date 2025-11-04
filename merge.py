import numpy as np
import pandas as pd


employees = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['John', 'Anna', 'Peter', 'Linda', 'Bob'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR']
})

# DataFrame 2: Salary information
salaries = pd.DataFrame({
    'employee_id': [1, 2, 3, 6, 7],
    'salary': [60000, 80000, 65000, 70000, 90000],
    'bonus': [5000, 10000, 7000, 8000, 12000]
})

merged = pd.merge(employees,salaries, on='employee_id',how="inner")
print(merged)

merged = pd.merge(employees,salaries, on='employee_id',how="outer")
print(merged)

merged = pd.merge(employees,salaries, on='employee_id',how="left")
print(merged)

merged = pd.merge(employees,salaries, on='employee_id',how="right")
print(merged)
