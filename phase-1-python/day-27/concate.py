import pandas as pd

# Table 1: January Workouts
jan_data = pd.DataFrame({
    'User': ['Mohit', 'Nilesh'],
    'Calories': [500, 600]
})

# Table 2: February Workouts
feb_data = pd.DataFrame({
    'User': ['Rahul', 'Aman'],
    'Calories': [450, 550]
})

print("--- VERTICAL CONCAT (axis=0) ---")
# Stacking February below January. 
# notice ignore_index=True gives us a clean 0, 1, 2, 3 index!
combined_months = pd.concat([jan_data, feb_data], axis=0, ignore_index=True)
print(combined_months)
print("\n")

# Table 3: Extra User Demographics (Same number of rows)
demo_data = pd.DataFrame({
    'Age': [24, 26, 22, 25],
    'City': ['Indore', 'Bhopal', 'Pune', 'Delhi']
})

print("--- HORIZONTAL CONCAT (axis=1) ---")
# Gluing the demographics right next to our combined workout table
final_master = pd.concat([combined_months, demo_data], axis=1)
print(final_master)

#2 practice
import pandas as pd

# Your startup's inventory
my_inventory = pd.DataFrame({
    'Product_ID': ['P101', 'P102'],
    'Item_Name': ['Wireless Mouse', 'Mechanical Keyboard'],
    'Stock': [150, 85]
})

# The acquired company's inventory
acquired_inventory = pd.DataFrame({
    'Product_ID': ['A999', 'A998'],
    'Item_Name': ['Webcam', 'Microphone'],
    'Stock': [40, 120]
})
master_inventory = pd.concat([my_inventory, acquired_inventory], axis=0, ignore_index=True)
print(master_inventory)