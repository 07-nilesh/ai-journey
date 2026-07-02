import os

class DataProcessor:
    def __init__(self, filename):
        self.filename = filename

    @property
    def file_extension(self):
        # Automatically detects if it's .csv, .json, etc.
        return os.path.splitext(self.filename)[1]

    def process(self):
        print(f"Generic: Opening {self.filename} for inspection...")

class CSVProcessor(DataProcessor): # Inheriting from DataProcessor
    def __init__(self, filename, delimiter=','):
        # super() calls the Parent's __init__ method
        super().__init__(filename) 
        self.delimiter = delimiter

    def process(self):
        # This OVERRIDES the parent's process method
        print(f"CSV-Specific: Parsing rows in {self.filename} using '{self.delimiter}'...")

# 1. Create the object
my_tool = CSVProcessor('training_data.csv', delimiter='|')

# 2. Access INHERITED data
print(f"Extension detected: {my_tool.file_extension}") 

# 3. Use OVERRIDDEN logic
my_tool.process()