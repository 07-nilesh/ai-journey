from datetime import datetime, timedelta

# DATA: Imagine this comes from your app's database as a string
raw_entry_log = "2026-05-10 08:30:00" 

# STEP 1: PARSING (String -> Object)
# We tell Python: Year-Month-Day Hour:Minute:Second
start_time = datetime.strptime(raw_entry_log, "%Y-%m-%d %H:%M:%S")

# STEP 2: TIMEDELTA (Doing Math)
# Let's say the user did a heavy 'Leg Day' for 1 hour and 15 minutes
workout_duration = timedelta(hours=1, minutes=15)
end_time = start_time + workout_duration

# STEP 3: FORMATTING (Object -> Pretty String)
# We want to show this to our user in Indore in a friendly way
print(f"Workout Started: {start_time.strftime('%I:%M %p')}")
print(f"Workout Ended:   {end_time.strftime('%I:%M %p')}")
print(f"Date:            {end_time.strftime('%A, %d %b %Y')}")