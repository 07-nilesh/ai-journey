import pandas as pd 

# DataFrame 1: Student Scores
scores_data = { 
    'Student': ['Alice', 'Bob', 'Charlie', 'David','Eve','Frank','Grace','Heidi'],
    'Math': [85, 92, 78, 96, 88, 90, 91, 89],
    'Science': [88, 85, 82, 90, 85, 88, 92, 87],
    'English': [90, 87, 85, 88, 92, 90, 85, 91]
}
df_scores = pd.DataFrame(scores_data)
avg_scores = df_scores[['Math', 'Science', 'English']].mean(axis=1)
df_scores['Average'] = avg_scores
print("--- Student Scores with Averages ---")
print(df_scores)
top_5_students = df_scores.sort_values(by='Average', ascending=False).head(5)
print("\n--- Top 5 Students by Average Score ---")
print(top_5_students[['Student', 'Average']])