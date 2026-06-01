# We define a function to check if a student passed their exam.
# We explicitly state 'score' MUST be an integer (int).
# We explicitly state 'student_name' MUST be text (str).
# The '-> bool' tells Python this function will output a True or False (boolean).
def has_passed(score: int, student_name: str) -> bool:
    
    # This evaluates the condition and returns either True or False
    return score >= 40

# We call the function, passing an int (85) and a str ("Rahul").
result = has_passed(85, "Rahul")

# Let's see the output
print(result)

def greet_student(name: str) -> str:
    return f"Welcome to the class, {name}!"
greeting = greet_student("Nilesh")
print(greeting)

def get_top_score(scores: list[int]) -> int:
    if not scores:
        return 0  # Return 0 if the list is empty
    return max(scores)

top_score = get_top_score([85,92])  # This will cause an error since max() can't compare strings
print(top_score)

def add_numbers(a: int, b: int) -> int:
    return a + b

print(add_numbers("Hello ", "Nilesh"))

def count_students(names: list[str]) -> str:
    return len(names)
print(count_students(["Alice"]))