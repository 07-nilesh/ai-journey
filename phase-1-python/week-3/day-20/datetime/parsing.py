from datetime import datetime
'''
# 1. The raw text data
raw_date_str = "2026-05-10"

# 2. Parsing: String -> Datetime Object
# Pattern: Year-Month-Day
parsed_moment = datetime.strptime(raw_date_str, "%Y-%m-%d")

print(f"Original Text: {raw_date_str}")
print(f"Smart Object: {parsed_moment}")
print(f"The year specifically is: {parsed_moment.year}")
'''
raw_data="10/May/2026"
parsed_date=datetime.strptime(raw_data,"%d/%B/%Y")
print(f"Original Text: {raw_data}")
print(f"Parsed Date Object: {parsed_date}")
print(type(parsed_date))