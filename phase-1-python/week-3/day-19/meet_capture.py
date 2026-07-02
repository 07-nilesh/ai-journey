import json
user_settings = '{"theme": "dark", "notifications": true, "capture_limit": 50}'
data=json.loads(user_settings)
print(data)
for key, value in data.items():
    if key=="capture_limit" and value==50:
        data[key] = 100
#if "capture_limit" in data:
#    data["capture_limit"] = 100
print(data)
with open("settings.json", "w") as f:
    json.dump(data, f, indent=4)
    print("✅ Settings saved to settings.json")