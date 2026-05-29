import random

dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def k_fold_split(data, k=5):
    indices=list(range(len(data)))
    print("Original Indices:", indices)
    random.shuffle(indices)

    fold_size = len(data) // k
    for fold in range(k):
        start_index = fold * fold_size
        end_index = start_index + fold_size if fold != k - 1 else len(data)
        test_indices = indices[start_index:end_index]
        train_indices = indices[:start_index] + indices[end_index:]
        train_data = [data[i] for i in train_indices]
        test_data = [data[i] for i in test_indices] 
        print(f"Fold {fold + 1}:")
        print("Train Indices:", train_indices)
        print("Test Indices:", test_indices)
        print("Train Data:", train_data)
        print("Test Data:", test_data)
k_fold_split(dataset, k=5)