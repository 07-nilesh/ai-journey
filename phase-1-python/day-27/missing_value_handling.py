import pandas as pd
import numpy as np # We need numpy to artificially insert 'NaN' values

weight_data = {
    'Day': [1, 2, 3, 4, 5, 6],
    'Weight_Kg': [70.0, 70.5, np.nan, np.nan, 72.0, 72.5]
}
df_weight = pd.DataFrame(weight_data)

print("--- 1. DIAGNOSE: Count missing values ---")
print(df_weight.isna().sum()) 
print("\n")

print("--- 2. DROP: The Nuclear Option ---")
# Drops rows 2 and 3 entirely
print(df_weight.dropna())
print("\n")

print("--- 3. FILL: The Mean Value ---")
# Calculates the mean of known weights (71.25) and fills the gaps
mean_weight = df_weight['Weight_Kg'].mean()
print(df_weight.fillna(mean_weight))
print("\n")

print("--- 4. INTERPOLATE: The Smart Transition ---")
# Draws a straight mathematical line from 70.5 to 72.0
print(df_weight.interpolate())

#2 practice
import pandas as pd
import numpy as np

smartwatch_data = {
    'Minute': [1, 2, 3, 4, 5],
    'Heart_Rate': [110, 125, np.nan, np.nan, 155]
}
df_hr = pd.DataFrame(smartwatch_data)
print("--- Count missing values ---")
print(df_hr.isna().sum())
df_clean = df_hr.interpolate()
print("\n--- Interpolated Heart Rate Data ---")
print(df_clean)