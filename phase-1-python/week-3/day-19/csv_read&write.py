import csv

# --- PART 1: WRITING DATA ---
data = [
    ["Name", "Exercise", "Weight"], # Header
    ["Nilesh", "Squats", "100kg"],
    ["Mohit", "Bench Press", "80kg"]
]

with open('gym_log.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data) # Writes all rows at once
    print("✅ File 'gym_log.csv' created successfully!")

# --- PART 2: READING DATA ---
print("\n--- Reading the Ledger ---")
with open('gym_log.csv', mode='r') as file:
    reader = csv.reader(file)
    header = next(reader) # Skip the header row
    for row in reader:
        # 'row' is just a list!
        if row[0]=="Nilesh":
            print(f"User: {row[0]} | Task: {row[1]} | Load: {row[2]}")