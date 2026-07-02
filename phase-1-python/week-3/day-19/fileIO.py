# 1. Writing to a file
with open("ai_journal.txt", "w") as file:
    file.write("Day 19: Mastering File I/O!\n")
    file.write("Goal: Build a Startup in Indore.")

# 2. Reading from a file
try:
    with open("ai_journal.txt", "r") as file:
        content = file.read()
        print("--- File Content ---")
        print(content)
except FileNotFoundError:
    print("Arre! The file doesn't exist.")

# 3. Appending (Adding more without deleting)
with open("ai_journal.txt", "a") as file:
    file.write("\nUpdate: Just finished the first code example.")