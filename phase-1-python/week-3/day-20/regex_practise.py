import re
'''
note = "Today I did 3 sets of 12 reps at 60kg and then 10 reps at 65kg"

# Template: \d+ means "one or more digits", followed by "kg"
pattern = r"(\d+)kg"

# 1. Using findall to get all weights
weights = re.findall(pattern, note)
print(f"Weights extracted: {weights}") 
# Output: ['60', '65']

# 2. Using sub to anonymize data (Replace kg values with 'XX')
hidden_data = re.sub(pattern, "XXkg", note)
print(f"Anonymized: {hidden_data}")'''
filenames=["img_001.jpg", "img_002.png", "notes.txt", "img_003.jpg"]
for filename in filenames:
    data=re.search(r"^img_.*\.jpg$",filename)
    if data:
        print(f"Found a match: {data.group()}")
    else:
        print(f"No match for: {filename}")