def log_workout(user_name, duration_minutes, *exercises, **details):
    print(f"User: {user_name}")
    if len(exercises)!=0:
        avg=duration_minutes/len(exercises)
    else:
        avg=0
    print(f"Total avg time per exercise :{avg} min")
    
    # args are packed into a tuple
    print(f"Exercises performed: {exercises}")

    
    # kwargs are packed into a dictionary
    if "gym_location" in details:
        print(f"Workout took place at: {details['gym_location']}")
    
    for key, value in details.items():
        print(f"Meta Info - {key}: {value}")

# Calling the function
log_workout("Nilesh",45 , "Bench Press", "Squats", "Deadlift", 
            gym_location="Indore Fitness", mood="Energized")

