import pandas as pd

class DataProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.df = None  # Start with an empty container[cite: 2]
    
    def load(self):
        """Reads the file and stores it in the object's RAM."""
        if self.filename.endswith('.csv'):
            self.df = pd.read_csv(self.filename)
            print(f"✅ Loaded CSV: {self.filename}")
        elif self.filename.endswith('.json'):
            self.df = pd.read_json(self.filename)
            print(f"✅ Loaded JSON: {self.filename}")
        else:
            print(f"❌ Error: Unsupported file type.")

    def clean(self):
        """Removes rows with missing data (NaN)."""
        if self.df is not None:
            old_shape = self.df.shape[0]
            self.df.dropna(inplace=True) # Remove empty rows[cite: 2]
            new_shape = self.df.shape[0]
            print(f"🧹 Cleaned: Removed {old_shape - new_shape} messy rows.")
        else:
            print("⚠️ Load data first!")

    def summary(self):
        """Displays technical info about the data."""
        if self.df is not None:
            # We use dtypes (no parentheses) and shape[cite: 2]
            print(f"\n--- Summary for {self.filename} ---")
            print(f"Rows: {self.df.shape[0]}, Columns: {self.df.shape[1]}")
            print(f"Data Types:\n{self.df.dtypes}")
        else:
            print("⚠️ Load data first!")

    def __str__(self):
        return f"DataProcessor for file: {self.filename}"

# TEST IT
my_processor = DataProcessor('data.csv')
my_processor.load()
my_processor.summary()