'''
study_hrs =5.0 # Number of hours studied
actual_score = 80.0 # Assuming a simple linear relationship: score = 10 * study_hrs

currrent_weight =12.0 # Initial weight (slope)
lr = 0.02 # Learning rate

for step in range(4):
    print(f"\n---cycle {step+1}--- ")
    predicted_score = currrent_weight * study_hrs
    loss = (predicted_score - actual_score) ** 2
    print(f"Predicted Score: {predicted_score:.2f}, Loss: {loss:.2f}")
    gradient = 2 * (predicted_score - actual_score) * study_hrs
    currrent_weight -= lr * gradient
    print(f"Updated Weight: {currrent_weight:.4f}")

#variation 1
study_hrs =5.0 # Number of hours studied
actual_score = 80.0 # Assuming a simple linear relationship: score = 10 * study_hrs

currrent_weight =12.0 # Initial weight (slope)
current_bias = 5.0 # Initial bias (intercept)
lr = 0.02 # Learning rate

for step in range(4):
    print(f"\n---cycle {step+1}--- ")
    predicted_score = currrent_weight * study_hrs + current_bias
    loss = (predicted_score - actual_score) ** 2
    print(f"Predicted Score: {predicted_score:.2f}, Loss: {loss:.2f}")
    gradient = 2 * (predicted_score - actual_score) * study_hrs
    currrent_weight -= lr * gradient
    print(f"Updated Weight: {currrent_weight:.4f}")
    
'''
#variation 2

study_hrs_list =[2.0,4.0,5.0] # Number of hours studied
actual_score = [40.,70.0,80.0] # Assuming a simple linear relationship: score = 10 * study_hrs

currrent_weight =12.0 # Initial weight (slope)
lr = 0.02 # Learning rate

for batch in range(3):
    total_batch_gradient = 0.0
    print(f"\n---Batch {batch+1}--- ")
    for step in range(len(study_hrs_list)):
        print(f"\n---cycle {step+1}--- ")
        predicted_score = currrent_weight * study_hrs_list[step]
        loss = (predicted_score - actual_score[step]) ** 2
        print(f"Predicted Score: {predicted_score:.2f}, Loss: {loss:.2f}")
        gradient = 2 * (predicted_score - actual_score[step]) * study_hrs_list[step]
        total_batch_gradient += gradient
    avg_batch_gradient = total_batch_gradient / len(study_hrs_list)
    currrent_weight -= lr * avg_batch_gradient
    print(f"Updated Weight after Batch: {currrent_weight:.4f}")
    
