import pandas as pd
from statistics import mode

data = {
    'name': ['John', 'Sarah', 'Michael', 'Sophia', 'James'],
    'age': [28, 24, 30, 27, 26],
    'score': [82, 91, 88, 76, 93]
}

df = pd.DataFrame(data)
print(df)
mean_age = df['age'].mean()
median_age = df['age'].median()
mode_age = mode(df['age'])
min_age = df['age'].min()
max_age = df['age'].max()

print("Summary Statistics for Age Column:")
print(f"Mean Age: {mean_age}")
print(f"Median Age: {median_age}")
print(f"Mode Age: {mode_age}")
print(f"Minimum Age: {min_age}")
print(f"Maximum Age: {max_age}")
