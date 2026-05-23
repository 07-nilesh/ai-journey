import matplotlib.pyplot as plt
'''
# 1. The Data
weeks = [1, 2, 3, 4]
deadlift_kg = [140, 145, 150, 155]
squat_kg = [120, 122.5, 127.5, 130]

# 2. Canvas Size (figsize)
fig, ax = plt.subplots(figsize=(10, 6))

# 3. Plotting with Color, Linestyle, and Labels (for the legend)
ax.plot(weeks, deadlift_kg, color='#E63946', linestyle='-', linewidth=2, marker='o', label='Deadlift')
ax.plot(weeks, squat_kg, color='#1D3557', linestyle='--', linewidth=2, marker='s', label='Squat')

# 4. Text Context (Title & Labels)
ax.set_title("Athlete 1RM Progression: Block 1", fontsize=16, fontweight='bold')
ax.set_xlabel("Training Week", fontsize=12)
ax.set_ylabel("Weight lifted (kg)", fontsize=12)

# 5. Background Grid (making it subtle with 'alpha' and 'linestyle')
ax.grid(True, linestyle=':', alpha=1)

# 6. The Legend (loc tells it where to anchor the box)
ax.legend(loc='upper right')

# 7. Render
plt.tight_layout()
plt.show()'''

#2 practice
import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr']
users = [500, 600, 550, 700]
premium = [100, 150, 200, 350]
fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(months, users, color='red', linestyle='--', marker='o', label='free tier users')
ax.plot(months, premium, color='green', linestyle='-', marker='s', label='Premium Users')
ax.set_title('User Growth Over First 4 Months', fontsize=14, fontweight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Number of Users', fontsize=12)
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend(loc='upper left')
plt.tight_layout()
plt.show()