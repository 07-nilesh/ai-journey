import os  # Built-in module to interact with your computer's operating system
from dotenv import load_dotenv  # Importing function to read the .env file

# Step 1: Look for a .env file in the current folder and load its variables
load_dotenv()

# Step 2: Grab our specific secret pass key from the environment using os.getenv
secret_api_key = os.getenv("INDORE_WEATHER_KEY")
if secret_api_key is None:
    raise ValueError("❌ Error: INDORE_WEATHER_KEY not found in environment!")

# Step 3: Print out the secret to verify it loaded successfully
# (Note: In a real startup product, never print your real secret keys!)
print(f"Successfully loaded key from locker: {secret_api_key}")

# variation 1
target_city = os.getenv("TARGET_CITY")
if target_city is None:
    raise ValueError("❌ Error: TARGET_CITY not found in environment!")
print(f"Tracking weather for city: {target_city}")

# variation 2
import requests
get_url = f"https://api.openweathermap.org/data/2.5/weather?q={target_city}&appid={secret_api_key}&units=metric"
response = requests.get(get_url)
print(response.json())

import os
from dotenv import load_dotenv
load_dotenv()
threshold = os.getenv("MODEL_THRESHOLD")
print(type(threshold))