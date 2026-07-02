from datetime import datetime
'''
# 1. Grab the current moment
now = datetime.now()

# 2. Format for a formal report (e.g., for a gym owner)
report_format = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Database Log: {report_format}")

# 3. Format for a friendly user notification
friendly_format = now.strftime("Finished at %I:%M %p on %A")
print(f"User Message: {friendly_format}")
# Output: Finished at 06:48 PM on Sunday'''

current_time = datetime.now()
formatted_time=current_time.strftime("Today is %A, %d-%m-%Y and the time is %H:%M")
print(formatted_time)