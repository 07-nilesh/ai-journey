import pandas as pd

# Creating our SPOTTER dataset
spotter_data = {
    "User": ["Mohit", "Nilesh", "Rahul", "Aman", "Priya", "Neha"],
    "City": ["Indore", "Bhopal", "Indore", "Bhopal", "Indore", "Bhopal"],
    "Workout_Split": ["Push", "Pull", "Legs", "Push", "Pull", "Legs"],
    "Calories_Burned": [450, 500, 600, 400, 550, 650]
}

df = pd.DataFrame(spotter_data)

# ---------------------------------------------------------
# 1. Grouping by a SINGLE Column
# ---------------------------------------------------------
print("--- Average Calories Burned per City ---")
# 1. Split by 'City'
# 2. Select the 'Calories_Burned' column to do math on
# 3. Apply the .mean() function
city_avg = df.groupby('City')['Calories_Burned'].mean()
print(city_avg)
print("\n")

# ---------------------------------------------------------
# 2. Grouping by MULTIPLE Columns
# ---------------------------------------------------------
print("--- Max Calories Burned per City AND Workout Split ---")
# When grouping by multiple columns, pass them as a LIST inside the brackets
# This creates a "MultiIndex" (a hierarchy of groups)
city_split_max = df.groupby(['City', 'Workout_Split'])['Calories_Burned'].max()
print(city_split_max)

#2 practice
import pandas as pd

delivery_data = {
    "Order_ID": [101, 102, 103, 104, 105, 106],
    "Restaurant_Type": ["Cafe", "Dhaba", "Cafe", "Fast Food", "Dhaba", "Fast Food"],
    "Delivery_Partner": ["Zomato", "Swiggy", "Swiggy", "Zomato", "Zomato", "Swiggy"],
    "Bill_Amount": [450, 800, 300, 250, 950, 350]
}
df_orders = pd.DataFrame(delivery_data)
total_bill =df_orders.groupby(['Delivery_Partner'])['Bill_Amount'].sum()
print(total_bill)
avg_bill = df_orders.groupby(['Restaurant_Type','Delivery_Partner'])['Bill_Amount'].mean()
print(avg_bill)