import pandas as pd
import numpy as np

# 1. Load the dataset
df = pd.read_csv('startup_funding.csv')

# --- THE CLEANING PROCESS ---

# Step A: Convert everything to a string first (just in case), then replace commas with nothing
df['Amount in USD'] = df['Amount in USD'].astype(str).str.replace(',', '')

# Step B: Some startups refuse to tell their funding amount, so the CSV might 
# literally say "undisclosed" or have random text. 
# We use pd.to_numeric with 'coerce'. This forces everything into a float. 
# If it finds a word like "undisclosed", it turns it into 'NaN' (Not a Number/Blank).
df['Amount in USD'] = pd.to_numeric(df['Amount in USD'], errors='coerce')

# --- THE STATS PROCESS ---

# Step C: Drop the blanks (NaNs) just for our math calculation
clean_funding = df['Amount in USD'].dropna()

# Step D: Run the magic describe function!
# We use apply(lambda x: '%.2f' % x) just to stop Pandas from using scientific 
# notation (like 1.5e+06) so it's easier for you to read.
print(clean_funding.describe().apply(lambda x: '%.2f' % x))

print("-" * 20)
print(f"Skewness: {clean_funding.skew():.2f}")