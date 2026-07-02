import pandas as pd

# Creating a DataFrame and setting a custom index
gym_data = {
    "Name": ["Mohit", "Nilesh", "Rahul"],
    "Bench_PR": [100, 110, 85],
    "Squat_PR": [140, 150, 120]
}

# Notice we are explicitly setting the row labels!
df = pd.DataFrame(gym_data, index=["U101", "U102", "U103"])
print("--- Full DataFrame ---")
print(df)
print("\n")

# ---------------------------------------------------------
# Using .loc (Searching by LABEL)
# ---------------------------------------------------------
print("--- Using .loc ---")
# Get Nilesh's Squat PR by using his row label ("U102") and column label ("Squat_PR")
nilesh_squat = df.loc["U102", "Squat_PR"]
print(f"Nilesh's Squat PR: {nilesh_squat}")

# ---------------------------------------------------------
# Using .iloc (Searching by POSITION)
# ---------------------------------------------------------
print("\n--- Using .iloc ---")
# Get Rahul's Bench PR. 
# Rahul is in the 3rd row (index 2). Bench_PR is the 2nd column (index 1).
rahul_bench = df.iloc[2, 1]
print(f"Rahul's Bench PR: {rahul_bench}")

#2 practice
import pandas as pd

startup_data = {
    "Company": ["Zomato", "Swiggy", "Cred", "Zerodha", "Razorpay"],
    "Category": ["Food", "Food", "Fintech", "Fintech", "Fintech"],
    "Valuation_Billion": [12.5, 10.7, 6.4, 3.0, 7.5]
}

# Creating the DataFrame and setting the Company name as the index
df_startups = pd.DataFrame(startup_data)
df_startups.set_index("Company", inplace=True)

print(df_startups)
print("\n--- Using .loc to get Zerodha Valuation ---")
zerodha_valuation = df_startups.loc["Zerodha", "Valuation_Billion"]
print(f"Zerodha's Valuation: {zerodha_valuation} Billion USD")
print("\n--- using .iloc print same data")
zerodha_valuation_1=df_startups.iloc[3,1]
print(f"Zerodha's Valuation: {zerodha_valuation_1} Billion USD")