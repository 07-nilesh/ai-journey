import pandas as pd

workout_data = {
    'User': ['Mohit', 'Nilesh', 'Rahul', 'Aman'],
    'Split_Code': ['P1', 'P2', 'L1', 'P1'],
    'Calories': [450, 600, 300, 800],
    'Duration_Mins': [45, 60, 30, 90]
}

df = pd.DataFrame(workout_data)

# ---------------------------------------------------------
# 1. Using .map() with a Dictionary
# ---------------------------------------------------------
print("--- Using .map() for direct substitution ---")
# We want to translate the Split_Code into readable text
split_dictionary = {'P1': 'Push', 'P2': 'Pull', 'L1': 'Legs'}

# We map the dictionary to the column
df['Split_Name'] = df['Split_Code'].map(split_dictionary)
print(df[['User', 'Split_Code', 'Split_Name']])
print("\n")


# ---------------------------------------------------------
# 2. Using .apply() with a Lambda Function (Single Column)
# ---------------------------------------------------------
print("--- Using .apply() with a lambda function ---")
# We want to flag workouts over 500 calories as "Intense"
df['Intensity'] = df['Calories'].apply(lambda x: 'Intense' if x > 500 else 'Normal')
print(df[['User', 'Calories', 'Intensity']])
print("\n")


# ---------------------------------------------------------
# 3. Using .apply() across MULTIPLE Columns (axis=1)
# ---------------------------------------------------------
print("--- Using .apply(axis=1) across the whole row ---")
# We want to calculate the Calories Burned Per Minute
# By using axis=1, 'row' becomes a variable holding the entire row's data
df['Cal_Per_Min'] = df.apply(lambda row: row['Calories'] / row['Duration_Mins'], axis=1)

# Formatting it to 2 decimal places for cleanliness
df['Cal_Per_Min'] = df['Cal_Per_Min'].round(2)
print(df[['User', 'Calories', 'Duration_Mins', 'Cal_Per_Min']])

#2 practice
import pandas as pd

delivery_data = {
    'Order_ID': [101, 102, 103, 104],
    'Status_Code': ['D', 'P', 'C', 'D'],
    'Distance_Km': [2.5, 8.0, 1.2, 6.5]
}
df_deliveries = pd.DataFrame(delivery_data)

status_dict = {'D': 'Delivered', 'P': 'Pending', 'C': 'Cancelled'}
df_deliveries['Status'] = df_deliveries['Status_Code'].map(status_dict)
print(df_deliveries[['Order_ID', 'Status_Code', 'Status']])

df_deliveries['Distance_fee'] = df_deliveries.apply(lambda row: 50 if row['Distance_Km'] >= 5 else 20, axis=1)
print(df_deliveries[['Order_ID', 'Distance_Km', 'Distance_fee']])