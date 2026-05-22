import pandas as pd

# 1. Create Left Table (indexed by User_ID)
users = pd.DataFrame({
    'Name': ['Mohit', 'Nilesh', 'Rahul'],
    'City': ['Indore', 'Bhopal', 'Pune']
}, index=[1, 2, 3]) # Setting the index explicitly!

# 2. Create Right Table (indexed by User_ID)
# Notice User 4 (Aman) is here, but User 1 (Mohit) is missing!
streaks = pd.DataFrame({
    'Current_Streak': [15, 5, 20]
}, index=[2, 3, 4]) 

print("--- LEFT JOIN (Default) ---")
# Keeps all users (1, 2, 3). Mohit will get NaN for his streak.
left_join = users.join(streaks, how='left')
print(left_join)
print("\n")

print("--- INNER JOIN ---")
# Only keeps users in BOTH tables (2, 3). Mohit and Aman are dropped.
inner_join = users.join(streaks, how='inner')
print(inner_join)

#2 practice
import pandas as pd

# Creating our tables with Student_ID as the index
midterm_scores = pd.DataFrame({
    'Midterm_Physics': [88, 75, 92]
}, index=['S101', 'S102', 'S103'])

final_scores = pd.DataFrame({
    'Final_Physics': [85, 90, 78]
}, index=['S102', 'S103', 'S104'])

allscores = midterm_scores.join(final_scores, how='outer')
print("--- OUTER JOIN ---")
print(allscores)

left_join_scores = midterm_scores.join(final_scores, how='left')
print("\n--- LEFT JOIN ---")    
print(left_join_scores)

inner_join_scores = midterm_scores.join(final_scores, how='inner')
print("\n--- INNER JOIN ---")
print(inner_join_scores)

right_join_scores = midterm_scores.join(final_scores, how='right')
print("\n--- RIGHT JOIN ---")
print(right_join_scores)