def log_workout(user_name, *exercises, **details):
    print(f"User: {user_name}")
    
    # args are packed into a tuple
    print(f"Exercises performed: {exercises}")
    
    # kwargs are packed into a dictionary
    if "gym_location" in details:
        print(f"Workout took place at: {details['gym_location']}")
    
    for key, value in details.items():
        print(f"Meta Info - {key}: {value}")

# Calling the function
log_workout("Nilesh", "Bench Press", "Squats", "Deadlift", 
            gym_location="Indore Fitness", duration="45 mins", mood="Energized")