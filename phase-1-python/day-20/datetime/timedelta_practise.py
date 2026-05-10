from datetime import datetime, timedelta
'''
# 1. Capture the start of the rest period
rest_start = datetime.now()
print(f"Rest started at: {rest_start.strftime('%H:%M:%S')}")

# 2. Define the allowed rest duration (90 seconds)
allowed_rest = timedelta(seconds=90)

# 3. Calculate exactly when they should start the next set
next_set_time = rest_start + allowed_rest

print(f"You should start your next set at: {next_set_time.strftime('%H:%M:%S')}")

# 4. Check the difference: How many days until your next payment?
today = datetime.now()
payment_due = datetime(2026, 6, 10)
diff = payment_due - today # Subtracting two datetimes gives a timedelta!

print(f"Days left until membership expires: {diff.days}")'''
current_time = datetime.now()
free_trial_end=current_time + timedelta(days=7)
print(f"Your free trial expires on: {free_trial_end.strftime('%d-%m-%Y ')}")