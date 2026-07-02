from collections import Counter
import re # We'll use this to clean punctuation

data = "In AI, we often get Timestamp Strings from data logs. To do any math (like calculating training duration or data freshness), we must turn that string into a Moment (Object), add/subtract Duration (Timedelta), and turn it back into a Report (String)"

# 1. Cleaning: Convert to lowercase and remove punctuation so 'Data' and 'data' aren't counted separately
clean_data = re.sub(r'[^\w\s]', '', data.lower())

# 2. Splitting: Turn the string into a LIST of words
words = clean_data.split()

# 3. Counting: Pass the list, not the string
word_count = Counter(words)

# Print the top 3 most common words
print("Top 3 words in your log:")
for word, count in word_count.most_common(3):
    print(f"{word}: {count}")