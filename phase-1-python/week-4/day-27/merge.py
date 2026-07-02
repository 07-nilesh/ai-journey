import pandas as pd

# Table 1: User Profiles
users_data = {
    "User_ID": [1, 2, 3],
    "Name": ["Mohit", "Nilesh", "Rahul"],
    "City": ["Indore", "Bhopal", "Pune"]
}
df_users = pd.DataFrame(users_data)

# Table 2: Active Subscriptions
subs_data = {
    "User_ID": [2, 1, 3],  # Notice the order is scrambled, Pandas won't care!
    "Plan": ["Pro", "Free", "Pro"],
    "Monthly_Fee": [999, 0, 999]
}
df_subs = pd.DataFrame(subs_data)

# ---------------------------------------------------------
# Merging the DataFrames
# ---------------------------------------------------------
print("--- Merged Master Table ---")

# We use the 'on' parameter to specify the shared key
master_df = pd.merge(df_users, df_subs, on='User_ID')

print(master_df)

#2 practice
import pandas as pd

# DataFrame 1
customer_data = {
    "Cust_ID": [101, 102, 103],
    "Name": ["Aman", "Priya", "Neha"],
    "Loyalty_Tier": ["Gold", "Silver", "Platinum"]
}
df_customers = pd.DataFrame(customer_data)

# DataFrame 2
purchase_data = {
    "Order_ID": [555, 556, 557],
    "Cust_ID": [103, 101, 102],
    "Item_Bought": ["Laptop", "Headphones", "Smartphone"],
    "Price": [65000, 2000, 25000]
}
df_purchases = pd.DataFrame(purchase_data)

df_combines = pd.merge(df_customers, df_purchases, on='Cust_ID')
print(df_combines)