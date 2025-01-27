# data_analysis.py
import pandas as pd

# Sample data for analysis
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Basic data analysis: Mean salary
mean_salary = df['Salary'].mean()
print(f"The average salary is: {mean_salary}")
