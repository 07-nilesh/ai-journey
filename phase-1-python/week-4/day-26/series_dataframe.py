import pandas as pd
import numpy as np

# ---------------------------------------------------------
# 1. Creating a Series from a List
# ---------------------------------------------------------
bench_press_list = [80, 100, 120, 60]

# We can manually set the index (e.g., User IDs)
bench_series = pd.Series(bench_press_list, index=['U1', 'U2', 'U3', 'U4'])
print("--- Pandas Series ---")
print(bench_series)
print("\n")

# ---------------------------------------------------------
# 2. Creating a DataFrame from a Dictionary (Most Common)
# ---------------------------------------------------------
# The keys become column names, the lists become the rows
spotter_dict = {
    "Name": ["Mohit", "Nilesh", "Rahul", "Aman"],
    "Bench_PR": [100, 110, 85, 90],
    "Squat_PR": [140, 150, 120, 130]
}

df_from_dict = pd.DataFrame(spotter_dict)
print("--- DataFrame from Dictionary ---")
print(df_from_dict)
print("\n")

# ---------------------------------------------------------
# 3. Creating a DataFrame from a List of Lists
# ---------------------------------------------------------
# Here, each inner list represents a single ROW
user_data_lists = [
    ["Mohit", "Push"],
    ["Nilesh", "Pull"],
    ["Rahul", "Legs"]
]

# We have to explicitly name the columns when using lists
df_from_list = pd.DataFrame(user_data_lists, columns=["Name", "Current_Split"])
print("--- DataFrame from List of Lists ---")
print(df_from_list)
print("\n")

# ---------------------------------------------------------
# 4. Creating a DataFrame from a NumPy Array
# ---------------------------------------------------------
# Generate some random usage stats (e.g., hours logged per week for 3 users across 2 weeks)
numpy_data = np.random.randint(3, 10, size=(3, 2)) 

df_from_numpy = pd.DataFrame(numpy_data, columns=["Week_1_Hours", "Week_2_Hours"])
print("--- DataFrame from NumPy Array ---")
print(df_from_numpy)

#2 practice
upcoming_ipos={"IPO_Name":["TechCorp", "HealthInc", "EduSoft"],
               "Issue_Price":[15, 20, 10],
               "Current_GMP":[5, 3, 2]}
ipo_df=pd.DataFrame(upcoming_ipos)
print("\n--- Upcoming IPOs DataFrame ---")  
print(ipo_df)
