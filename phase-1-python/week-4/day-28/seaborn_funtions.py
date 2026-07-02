import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Mock SaaS Platform Data
data = {
    'Age': [21, 24, 28, 35, 22, 25, 40, 29, 31, 23],
    'Session_Mins': [45, 60, 90, 30, 50, 75, 25, 80, 40, 55],
    'Calories': [300, 400, 600, 200, 350, 500, 180, 550, 250, 380],
    'Subscription': ['Pro', 'Free', 'Pro', 'Free', 'Pro', 'Pro', 'Free', 'Pro', 'Free', 'Free']
}
df = pd.DataFrame(data)

# Set the visual theme globally
sns.set_theme(style="darkgrid")

# Create a 2x2 grid for our specific plots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# --- Plot 1: Scatterplot ---
# Notice 'hue': it automatically colors dots blue for Pro and orange for Free!
sns.scatterplot(data=df, x='Session_Mins', y='Calories', hue='Subscription', ax=axs[0, 0], s=100)
axs[0, 0].set_title("Session Length vs Calories Burned")

# --- Plot 2: Histplot ---
# 'kde=True' draws a smooth probability curve over the bars
sns.histplot(data=df, x='Age', kde=True, color='purple', ax=axs[0, 1])
axs[0, 1].set_title("User Age Distribution")

# --- Plot 3: Boxplot ---
# We can map a category to X and a number to Y to compare groups side-by-side
sns.boxplot(data=df, x='Subscription', y='Session_Mins', ax=axs[1, 0])
axs[1, 0].set_title("Session Lengths by Tier (Spotting Outliers)")

# --- Plot 4: Heatmap ---
# We must drop the text column ('Subscription') before calculating math correlations
numeric_df = df.drop(columns=['Subscription'])
corr_matrix = numeric_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=axs[1, 1])
axs[1, 1].set_title("Feature Correlation Heatmap")

plt.tight_layout()
plt.show()

# --- Plot 5: Pairplot ---
# Pairplot creates its own Figure automatically, so we call it separately
# It plots every numeric column against every other numeric column!
sns.pairplot(df, hue='Subscription')
plt.show()