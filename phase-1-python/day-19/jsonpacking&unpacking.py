import json

# Our Python Data (The Plate)
gym_config = {
    "startup_name": "SPOTTER",
    "location": "Indore",
    "active_users": 150,
    "features": ["AI Coaching", "PPL Tracking"]
}

# --- PACKING (Serialization) ---

# 1. dumps: Turning it into a string to print or send to an API
json_string = json.dumps(gym_config, indent=4) # indent makes it look pretty!
print("JSON as a String:")
print(json_string)

# 2. dump: Saving it into a file for later
with open("config.json", "w") as f:
    json.dump(gym_config, f, indent=4)
    print("\n✅ gym_config saved to config.json")


# --- UNPACKING (Deserialization) ---

# 3. load: Reading directly from the file
with open("config.json", "r") as f:
    data_from_file = json.load(f)
    print(f"\nUnpacked from file: {data_from_file['startup_name']} is based in {data_from_file['location']}")

# 4. loads: Reading from a string variable
parsed_data = json.loads(json_string)
print(f"Unpacked from string: active_users is {parsed_data['active_users']}")