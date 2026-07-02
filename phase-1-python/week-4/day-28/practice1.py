import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Muscle_Group': ['Chest', 'Back', 'Legs', 'Chest', 'Back', 'Legs'], 
    'Volume_Load_Kg': [3000, 4500, 6000, 3200, 4100, 6500], 
    'Athlete_Level': ['Adv', 'Adv', 'Adv', 'Novice', 'Novice', 'Novice']})
sns.set_theme(style="dark") # whitegrid, dark, white, ticks ,darkgrid
fig, axs = plt.subplots(1, 1, figsize=(14, 5))
sns.barplot(data=df, x='Muscle_Group', y='Volume_Load_Kg', hue='Athlete_Level', ax=axs)
axs.set_title("Volume Load by Muscle Group and Athlete Level")
plt.tight_layout()
plt.show()