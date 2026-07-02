import numpy as np

np.random.seed(42)  # For reproducibility
# Generate synthetic data
n_samples = 200
x= np.random.uniform(1,10,size=(n_samples,1)) # Features (1 to 10)
noise = np.random.normal(0, 5, size=(n_samples,1)) # Noise
y=15 +(7.5 * x) + noise # Target variable with some noise
y=np.clip(y, 0, 100) # Clip values to be between 0 and 100
# Now we have our synthetic dataset (x, y) ready for analysis or modeling

# 1. linear regression with gradient descent
class LinearRegressionGD:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.theta = None  # Parameters (weights)
    
    def fit(self, X, y):
        m, n = X.shape
        # Add intercept term (bias) to X
        X_b = np.hstack([np.ones((m, 1)), X])  # Shape: (m, n+1)
        self.theta = np.zeros((n + 1, 1))  # Initialize parameters
        
        for _ in range(self.n_iterations):
            predictions = X_b @ self.theta  # Shape: (m, 1)
            errors = predictions - y.reshape(-1, 1)  # Shape: (m, 1)
            gradients = (2/m) * X_b.T @ errors  # Shape: (n+1, 1)
            self.theta -= self.learning_rate * gradients  # Update parameters
    
    def predict(self, X):
        m = X.shape[0]
        X_b = np.hstack([np.ones((m, 1)), X])  # Add intercept term
        return X_b @ self.theta  # Return predictions
# Example usage
model = LinearRegressionGD(learning_rate=0.01, n_iterations=1000)
model.fit(x, y)
predictions = model.predict(x)
print("Learned parameters (theta):", model.theta.flatten())
print("Predictions:", predictions.flatten())

#2 mean squared error and mean absolute error
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)
def mean_absolute_error(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))
mse = mean_squared_error(y, predictions)
mae = mean_absolute_error(y, predictions)
print(f"Mean Squared Error: {mse:.2f}")
print(f"Mean Absolute Error: {mae:.2f}")

#3 train-test split
def train_test_split(X, y, test_size=0.2, random_state=None):
    if random_state is not None:
        np.random.seed(random_state)
    m = X.shape[0]
    indices = np.random.permutation(m)
    test_size = int(m * test_size)
    test_indices = indices[:test_size]
    train_indices = indices[test_size:]
    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("Training set size:", X_train.shape[0])
print("Test set size:", X_test.shape[0])

#4 Normalization function(min-max scaling) 
def min_max_scaling(X):
    X_min = np.min(X, axis=0)
    X_max = np.max(X, axis=0)
    return (X - X_min) / (X_max - X_min)
X_normalized = min_max_scaling(x)
print("Normalized features (first 5 samples):\n", X_normalized[:5])
print("Original features (first 5 samples):\n", x[:5])
print("Min of original features:", np.min(x))
print("Max of original features:", np.max(x))