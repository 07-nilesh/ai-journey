import json

def load_ai_config(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            
            # 1. Handle Empty Data
            if not content:
                print(f"⚠️ Warning: '{file_path}' is empty!")
                return None
            
            # 2. Handle Wrong Format (trying to parse JSON)
            data = json.loads(content)
            return data

    # 3. Handle Missing File
    except FileNotFoundError:
        print(f"❌ Error: Cannot find the file at {file_path}. Check your folder structure!")
    except json.JSONDecodeError:
        print(f"❌ Error: Format mismatch! '{file_path}' is not a valid JSON.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
    
    return None

# Testing the graceful exit
config = load_ai_config("my_startup_config.json")