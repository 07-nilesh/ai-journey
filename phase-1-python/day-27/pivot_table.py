import pandas as pd

workout_data = {
    "City": ["Indore", "Bhopal", "Indore", "Bhopal", "Indore", "Bhopal", "Indore", "Bhopal"],
    "Workout_Split": ["Push", "Push", "Pull", "Pull", "Legs", "Legs", "Push", "Pull"],
    "Calories_Burned": [450, 420, 500, 480, 600, 580, 470, 490]
}

df_gym = pd.DataFrame(workout_data)

# ---------------------------------------------------------
# Creating a Pivot Table
# ---------------------------------------------------------
print("--- Average Calories Burned: City vs Workout Split ---")

gym_pivot = df_gym.pivot_table(
    values='Calories_Burned',  # The numbers we want inside the grid
    index='City',              # The rows
    columns='Workout_Split',   # The columns across the top
    aggfunc='mean'             # The math we want to apply (mean is default)
)

print(gym_pivot)

#2 practice
import pandas as pd

delivery_data = {
    "Order_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Restaurant_Type": ["Cafe", "Dhaba", "Cafe", "Fast Food", "Dhaba", "Fast Food", "Cafe", "Dhaba"],
    "Delivery_Partner": ["Zomato", "Swiggy", "Swiggy", "Zomato", "Zomato", "Swiggy", "Zomato", "Swiggy"],
    "Bill_Amount": [450, 800, 300, 250, 950, 350, 500, 750]
}
df_orders = pd.DataFrame(delivery_data)
pivot_table = df_orders.pivot_table(
    values='Bill_Amount',
    index='Restaurant_Type',
    columns='Delivery_Partner',
    aggfunc='sum'
)
print(pivot_table)