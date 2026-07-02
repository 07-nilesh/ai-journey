import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Instantly make all plots look professional
sns.set_theme(style="darkgrid")

# 1. Create a mock Pandas DataFrame for SPOTTER gym data
data = {
    'Workout_Duration_mins': [30, 45, 60, 40, 50, 60, 90, 20],
    'Calories_Burned': [250, 400, 550, 320, 450, 520, 800, 150],
    'Average_Heart_Rate': [110, 125, 140, 120, 130, 135, 160, 100]
}
df = pd.DataFrame(data)

# Create a 1x2 grid using our Matplotlib skills!
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# --- PLOT 1: Seaborn Regression Plot (Scatter + Trendline) ---
# We just pass the column names and the DataFrame!
sns.regplot(data=df, x='Workout_Duration_mins', y='Calories_Burned', 
            color='blue', marker='o', ax=axs[0])
axs[0].set_title("Duration vs Calories")

# --- PLOT 2: The Correlation Heatmap ---
# First, calculate the correlation matrix using Pandas
corr_matrix = df.corr()

# Now, plot it with Seaborn
# annot=True puts the actual numbers inside the colored boxes
# cmap="coolwarm" is the color palette (blue for cold/low, red for hot/high)
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=axs[1])
axs[1].set_title("Feature Correlation Heatmap")

plt.tight_layout()
plt.show() # We still use plt.show() to render!