import pandas as pd

# Imagine this list has 10,000 users instead of 8
data = {'Name': ['Aman', 'Bob', 'Chetan', 'Divya', 'Esha', 'Farhan', 'Gaurav', 'Harish'],
        'Age': [22, 25, 23, 24, 28, 21, 26, 27]}

df = pd.DataFrame(data)

print("--- Default .head() (First 5 rows) ---")
print(df.head()) 

print("\n--- Custom .head(2) (First 2 rows) ---")
print(df.head(2))

print("\n--- Using .tail(3) (Last 3 rows) ---")
print(df.tail(3))