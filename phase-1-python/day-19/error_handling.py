def load_ai_data(filename):
    try:
        print(f"--- Attempting to open {filename} ---")
        with open(filename, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        # Instead of crashing, we give a helpful message
        print("❌ Error: Arre! The data file is missing. Please check the path.")
        data = None
    except Exception as e:
        # Catching any other unexpected errors
        print(f"❌ An unexpected error occurred: {e}")
        data = None
    else:
        print("✅ Success: Data loaded perfectly!")
    finally:
        print("🧹 Operation complete. System resources are safe.")
    
    return data

# Test it
my_data = load_ai_data("day19_data.txt")