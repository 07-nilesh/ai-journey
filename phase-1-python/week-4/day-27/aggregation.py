import pandas as pd

# Simulating a week of SPOTTER workout logs
workout_data = {
    "User": ["Mohit", "Nilesh", "Rahul", "Mohit", "Nilesh", "Rahul"],
    "Split": ["Push", "Pull", "Legs", "Push", "Pull", "Legs"],
    "Calories": [450, 500, 600, 480, 520, 590],
    "Duration_Mins": [45, 50, 60, 50, 55, 58],
    "Max_Heart_Rate": [165, 170, 180, 168, 172, 178]
}

df_workouts = pd.DataFrame(workout_data)

# ---------------------------------------------------------
# Using .agg() to perform different math on different columns
# ---------------------------------------------------------
print("--- SPOTTER Workout Summary by User ---")

# We pass a dictionary to .agg()
# Key = Column Name, Value = The math function (as a string)
user_summary = df_workouts.groupby('User').agg({
    'Calories': 'sum',            # Total calories burned
    'Duration_Mins': 'mean',      # Average workout time
    'Max_Heart_Rate': 'max'       # Absolute highest heart rate hit
})

print(user_summary)

#2 practice
import pandas as pd

delivery_data = {
    "Order_ID": [101, 102, 103, 104, 105, 106],
    "Restaurant_Type": ["Cafe", "Dhaba", "Cafe", "Fast Food", "Dhaba", "Fast Food"],
    "Delivery_Partner": ["Zomato", "Swiggy", "Swiggy", "Zomato", "Zomato", "Swiggy"],
    "Bill_Amount": [450, 800, 300, 250, 950, 350]
}
df_orders = pd.DataFrame(delivery_data)
group_summary = df_orders.groupby('Delivery_Partner').agg({
    'Bill_Amount': 'sum',
    'Order_ID': 'count'
})
print(group_summary)