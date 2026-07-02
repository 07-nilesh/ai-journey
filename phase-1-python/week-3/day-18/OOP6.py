class AIModel:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    # --- THE GETTER ---
    @property
    def model_id(self):
        """Returns a formatted ID string."""
        return f"{self.name}_v{self.version}"

    # --- THE SETTER ---
    @model_id.setter
    def model_id(self, new_id):
        """Parses an ID string back into name and version."""
        # Logic: Split 'GPT_v4' into ['GPT', '4']
        name_part, version_part = new_id.split('_v')
        self.name = name_part
        self.version = version_part

    # --- THE DELETER ---
    @model_id.deleter
    def model_id(self):
        print("Model ID deleted. Resetting values...")
        self.name = None
        self.version = None

# Testing the flow
model_1 = AIModel("BERT", 1)
print(model_1.model_id)  # Output: BERT_v1

model_1.model_id = "Llama_v3" # Triggers SETTER
print(model_1.name)          # Output: Llama

del model_1.model_id         # Triggers DELETER