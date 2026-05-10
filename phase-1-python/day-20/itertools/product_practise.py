import itertools

# Model settings we want to test
learning_rates = [0.01, 0.001]
batch_sizes = [32, 64]
epochs = [10, 20]

# Without product, you'd need 3 nested for-loops. 
# With product, it's one clean line:
combinations = itertools.product(learning_rates, batch_sizes, epochs)

print("Planning AI Experiments:")
for combo in combinations:
    #unpacking of tuple
    lr, batch, ep = combo
    print(f"Test -> LR: {lr}, Batch: {batch}, Epochs: {ep}")

# Output will show 8 unique combinations (2x2x2)