from typing import List, Dict

# 1. Calculates the average of a list of decimal numbers
def calculate_mean(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)

# 2. Cleans a string and optionally converts to lowercase (make_lowercase is a boolean)
def clean_text(text: str, make_lowercase: bool) -> str:
    if make_lowercase:
        return text.lower().strip()
    return text.strip()

# 3. Takes a student ID (text) and a database (dictionary mapping text IDs to integer scores)
def get_student_score(student_id: str, score_database: Dict[str, int]) -> int:
    return score_database.get(student_id, 0)

numbers = [10.5, 20.3, 30.2]
print(calculate_mean(numbers))
text = "  Hello World!  "
print(clean_text(text, make_lowercase=True))
score_db = {"S001": 85, "S002": 92}
print(get_student_score("S001", score_db))