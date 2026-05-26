#target
actual_value =80.0
#predicted value
predicted_value = 85.0
#calculate loss using mean squared error
loss = (predicted_value - actual_value) ** 2
print(f"Loss (Mean Squared Error): {loss:.4f}")
#calculate derivative of loss with respect to predicted value
loss_derivative = 2 * (predicted_value - actual_value)
print(f"Derivative of Loss with respect to predicted value: {loss_derivative:.4f}")
print(f"Action: If gradient is positive ({loss_derivative}), change prediction by moving LEFT.")

#variation 1
#target
actual_value =80.0
#predicted value
predicted_value = 70.0
#calculate loss using mean squared error
loss = (predicted_value - actual_value) ** 2
print(f"Loss (Mean Squared Error): {loss:.4f}")
#calculate derivative of loss with respect to predicted value
loss_derivative = 2 * (predicted_value - actual_value)
print(f"Derivative of Loss with respect to predicted value: {loss_derivative:.4f}")
print(f"Action: If gradient is positive ({loss_derivative}), change prediction by moving LEFT.")

#variation 2
#target
actual_value =80.0
#predicted value
predicted_value = 95.0
#calculate loss using mean squared error
learning_rate = 0.1
loss = (predicted_value - actual_value) ** 2
print(f"Loss (Mean Squared Error): {loss:.4f}")
#calculate derivative of loss with respect to predicted value
loss_derivative = 2 * (predicted_value - actual_value)
print(f"Derivative of Loss with respect to predicted value: {loss_derivative:.4f}")
print(f"Action: If gradient is positive ({loss_derivative}), change prediction by moving LEFT.")

#update prediction using gradient descent
new_prediction = predicted_value - (learning_rate * loss_derivative)
print(f"Updated Prediction after applying gradient descent: {new_prediction:.4f}")