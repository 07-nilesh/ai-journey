import json

# Removed the unnecessary tomlkit import
Required_keys = ["model_name", "version", "api_key"]

try:
    with open("config.json", "r") as f:
        config_data = json.load(f)
        
        # Validation Loop
        for key in Required_keys:
            # 1. Check if key exists
            if key not in config_data:
                # Using a standard KeyError or your custom DataValidationError!
                raise KeyError(f"Missing required key: {key}")
            
            # 2. Check if type is valid
            if not isinstance(config_data[key], (str, int, float, bool)):
                raise TypeError(f"Invalid type for key '{key}': {type(config_data[key]).__name__}")
        
        # If we reached here, the config is solid!
        print("✅ Config is valid!")
        print(f"Project: {config_data['model_name']} | Version: {config_data['version']}")

except FileNotFoundError:
    print("❌ Error: 'config.json' not found in this folder.")
except json.JSONDecodeError:
    print("❌ Error: 'config.json' has formatting errors (check your commas!).")
except (KeyError, TypeError) as e:
    print(f"❌ Validation Error: {e}")
except Exception as e:
    print(f"❌ Unexpected crash: {e}")