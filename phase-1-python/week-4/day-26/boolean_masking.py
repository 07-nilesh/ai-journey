import pandas as pd

startup_data = {
    "Company": ["Zomato", "Swiggy", "Cred", "Zerodha", "Razorpay"],
    "Category": ["Food", "Food", "Fintech", "Fintech", "Fintech"],
    "Valuation_Billion": [12.5, 10.7, 6.4, 3.0, 7.5]
}
df = pd.DataFrame(startup_data)

# ---------------------------------------------------------
# 1. Standard Boolean Masking (Single Condition)
# ---------------------------------------------------------
print("--- Valuations strictly greater than 10 Billion ---")
# Step 1: Create the mask (df['Valuation_Billion'] > 10)
# Step 2: Apply it inside df[...]
decacorns = df[df['Valuation_Billion'] > 10]
print(decacorns)
print("\n")

# ---------------------------------------------------------
# 2. Boolean Masking (Multiple Conditions)
# ---------------------------------------------------------
print("--- Fintechs worth more than 5 Billion ---")
# Notice the parentheses around each condition and the bitwise '&'
big_fintechs = df[(df['Category'] == 'Fintech') & (df['Valuation_Billion'] > 5)]
print(big_fintechs)
print("\n")

# ---------------------------------------------------------
# 3. Using .query() (The Cleaner Way)
# ---------------------------------------------------------
print("--- Using .query() for the exact same result ---")
# It reads exactly like an SQL statement or plain English!
clean_filter = df.query("Category == 'Fintech' and Valuation_Billion > 5")
print(clean_filter)

#2 practice
import pandas as pd

user_data = {
    "Username": ["Mohit", "Aman", "Rahul", "Priya", "Neha"],
    "Subscription_Type": ["Pro", "Free", "Pro", "Pro", "Free"],
    "Workouts_Logged": [45, 12, 89, 5, 22]
}
users_df = pd.DataFrame(user_data)
print(" all users who have a 'Pro' subscription AND have logged more than 20 workouts")
boolean_mask=users_df[(users_df['Subscription_Type'] == 'Pro') & (users_df['Workouts_Logged'] > 20  )]
print(boolean_mask)
print("Using the .query() method, do the exact same filter")
boolean_mask_query=users_df.query("Subscription_Type == 'Pro' and Workouts_Logged > 20")
print(boolean_mask_query)
