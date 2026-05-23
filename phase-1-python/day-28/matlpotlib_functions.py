import matplotlib.pyplot as plt
import numpy as np
'''
# --- MOCK DATA ---
# 1. Continuous data
days = np.array([1, 2, 3, 4, 5])
active_users = np.array([150, 180, 210, 205, 250])

# 2. Correlation data
squat_weights = np.array([60, 65, 70, 75, 80, 85, 90])
calories_burned = np.array([300, 320, 310, 340, 400, 390, 430])

# 3. Categorical data
features = ['AI Coach', 'Diet Plan', 'Analytics']
usage_hours = [120, 85, 40]

# 4. Distribution data (Generating 1000 random user ages around 22 years old)
user_ages = np.random.normal(loc=22, scale=3, size=1000) 

# 5. Statistical data (Session times in minutes, including a crazy 180-minute outlier)
session_times = np.array([30, 45, 50, 40, 60, 45, 55, 180, 15]) 

# --- BUILDING THE DASHBOARD ---
# Create a 2x3 grid of subplots (canvas is 15x8 inches)
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(15, 8))

# 1. Line Plot (Trend over time)
axs[0, 0].plot(days, active_users, marker='o', color='blue', linestyle='--')
axs[0, 0].set_title('plt.plot(): User Growth')

# 2. Scatter Plot (Correlation)
axs[0, 1].scatter(squat_weights, calories_burned, color='red', alpha=0.7)
axs[0, 1].set_title('plt.scatter(): Squat Weight vs Calories')

# 3. Bar Chart (Categorical comparison)
axs[0, 2].bar(features, usage_hours, color='green')
axs[0, 2].set_title('plt.bar(): Feature Popularity')

# 4. Histogram (Distribution)
# 'bins=20' means we chunk the ages into 20 distinct groups
axs[1, 0].hist(user_ages, bins=20, color='purple', edgecolor='black')
axs[1, 0].set_title('plt.hist(): User Age Distribution')

# 5. Boxplot (Statistical spread & outliers)
axs[1, 1].boxplot(session_times)
axs[1, 1].set_title('plt.boxplot(): Session Lengths (Note the outlier!)')

# Hide the empty 6th subplot (bottom right) since we only have 5 plots
axs[1, 2].axis('off')

# Automatically adjust spacing so titles don't overlap
plt.tight_layout()
plt.show()

#2 practice
import matplotlib.pyplot as plt
days_to_launch = [5, 4, 3, 2, 1]
gmp_price = [40, 45, 42, 50, 65]
fig,axs = plt.subplots(nrows=1, ncols=1, figsize=(12, 5))
axs.plot(days_to_launch, gmp_price, marker='o', color='orange', linestyle='-')
axs.set_title('GMP Price Trend Before Launch')
axs.set_xlabel('Days to Launch')
axs.set_ylabel('GMP Price (in $)')
plt.tight_layout()
plt.show()

#3 practice
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [10, 20, 30]
categories = ['A', 'B']
values = [50,80]
fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))
axs[0].plot(x, y, marker='o', color='cyan', linestyle='-')
axs[0].set_title('Revenue')
axs[0].set_xlabel('Month')
axs[0].set_ylabel('Revenue (in $)')
axs[1].bar(categories, values, color='magenta')
axs[1].set_title('Signups')
axs[1].set_xlabel('Category')
axs[1].set_ylabel('Number of Signups')
plt.tight_layout()
plt.show()'''

import matplotlib.pyplot as plt

days = [1, 2, 3, 4]
active_users = [100, 150, 200, 250]
api_latency = [40, 35, 30, 25]

plt.figure(figsize=(10, 4))

# Activate subplot 1 (1 row, 2 columns, index 1)
plt.subplot(1, 2, 1) 
plt.plot(days, active_users, color='green' , linestyle=':')
plt.title('Daily Active Users')

# Activate subplot 2 (1 row, 2 columns, index 2)
plt.subplot(1, 2, 2) 
plt.plot(days, api_latency, color='red', linestyle='--')
plt.title('AI-Coach Latency (ms)')

plt.tight_layout()
plt.show()