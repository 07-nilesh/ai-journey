import pandas as pd

# Creating a dataset of recent IPOs
data = {
    "IPO_Name": ["TechCorp", "HealthInc", "EduSoft", "GreenEnergy", "FinServe", "AutoM"],
    "Sector": ["Tech", "Health", "Tech", "Energy", "Finance", "Tech"],
    "Issue_Price": [150, 200, 120, 300, 250, 100],
    "Current_GMP": [50, 10, 80, 0, -20, 50],
    "Subscribed_Times": [12.5, 2.1, 45.0, 1.5, 0.8, 15.0]
}

df = pd.DataFrame(data)

# ---------------------------------------------------------
# 1. df.info() -> Structural Overview
# ---------------------------------------------------------
print("--- df.info() ---")
print(df.info()) 
# Look at the output: it tells you there are 6 rows, no missing values (Non-Null Count), 
# and the data types (object for text, int64/float64 for numbers).

# ---------------------------------------------------------
# 2. df.describe() -> Mathematical Overview
# ---------------------------------------------------------
print("\n--- df.describe() ---")
print(df.describe())
# Notice it automatically ignores the text columns (IPO_Name, Sector) 
# and only calculates math for Issue_Price, Current_GMP, and Subscribed_Times.

# ---------------------------------------------------------
# 3. df.value_counts() -> Tallying Categories
# ---------------------------------------------------------
print("\n--- df['Sector'].value_counts() ---")
print(df['Sector'].value_counts())
# Output shows: Tech: 3, Health: 1, Energy: 1, Finance: 1. 
# (Note: We apply this to a specific Series/Column, not usually the whole DataFrame).

# ---------------------------------------------------------
# 4. df.nunique() -> Counting Unique Items
# ---------------------------------------------------------
print("\n--- df.nunique() ---")
print(df.nunique())
# Output shows how many completely different items exist in EVERY column.
# E.g., there are 4 unique Sectors.

#2 practice
startup_data = {
    "Company": ["Zomato", "Swiggy", "Cred", "Zerodha", "Razorpay", "Meesho", "Groww"],
    "Category": ["Food", "Food", "Fintech", "Fintech", "Fintech", "E-commerce", "Fintech"],
    "Valuation_Billion": [12.5, 10.7, 6.4, 3.0, 7.5, 4.9, 3.0],
    "Profitable": [True, False, False, True, True, False, True]
}
startup_df = pd.DataFrame(startup_data)
print("\n startup belongs to each category")
print(startup_df['Category'].value_counts())
print("\n mathematical summary of the valuation")
print(startup_df['Valuation_Billion'].describe())