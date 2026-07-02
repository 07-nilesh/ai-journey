import random
hrs_study = [1,2,3,4,5,6,7,8,9,10]
exam_scores = [45,50,58,65,70,74,80,85,88,95]

def train_test_split(X, y, test_size=0.2):
    combined_data =list(zip(X, y))
    random.shuffle(combined_data)

    x_shuffled, y_shuffled = zip(*combined_data)
    x_shuffled, y_shuffled = list(x_shuffled), list(y_shuffled)

    total_records = len(x_shuffled)
    tests_count = int(total_records * test_size)
    split_index = total_records - tests_count

    x_train, y_train = x_shuffled[:split_index], y_shuffled[:split_index]
    x_test, y_test = x_shuffled[split_index:], y_shuffled[split_index:]

    return x_train, x_test, y_train, y_test
def index_split(X,y,test_size=0.2):
    range_of_indices = list(range(len(X)))
    random.shuffle(range_of_indices)
    train_indices = range_of_indices[:int(len(X)*(1-test_size))]
    test_indices = range_of_indices[int(len(X)*(1-test_size)):]
    x_train = [X[i] for i in train_indices]
    y_train = [y[i] for i in train_indices]
    x_test = [X[i] for i in test_indices]
    y_test = [y[i] for i in test_indices]

    return x_train, x_test, y_train, y_test

x_train, x_test, y_train, y_test = index_split(hrs_study, exam_scores, test_size=1.5)

print("Training features:", x_train)
print("Testing features:", x_test)
print("Training labels:", y_train)
print("Testing labels:", y_test)