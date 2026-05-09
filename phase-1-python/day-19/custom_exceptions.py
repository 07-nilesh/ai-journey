'''
# 1. Define the custom exception by inheriting from Exception
class DataValidationError(Exception):
    """Exception raised for errors in the input data format."""
    def __init__(self, message="Data is not formatted correctly for Indore AI standards"):
        self.message = message
        super().__init__(self.message)

# 2. How to use it in your code
def check_gym_data(weight):
    if weight <= 0:
        # We "raise" our custom error manually
        raise DataValidationError(f"Invalid Weight: {weight}kg. Weight must be positive!")
    else:
        print(f"Adding {weight}kg to your workout log.")

# 3. Handling it
try:
    check_gym_data(-10)
except DataValidationError as e:
    print(f"Caught a custom error: {e}")'''
class FileFormatError(Exception):
    def __init__(self, message="Unsupported file format. Please use .csv or .json"):
        self.message = message
        super().__init__(self.message)

def data_check(filename):
    clean_filename= filename.lower()
    if not (clean_filename.endswith('.csv') or clean_filename.endswith('.json')):
        raise FileFormatError(f"Invalid file: {filename}. Only .csv and .json are accepted.")
    return f"File {filename} is valid for processing."


try:
    result=data_check("data.csv")
    print(result)
    my_data = data_check("data.txt")
except FileFormatError as e:
    print(f"Caught a custom error: {e}")