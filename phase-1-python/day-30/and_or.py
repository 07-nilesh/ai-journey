prob_A=0.20
prob_B=0.05
prob_A_and_B=0.02
prob_A_or_prob_B = prob_A + prob_B - prob_A_and_B
print(f"The probability of A or B happening is: {prob_A_or_prob_B:.2f}")

# variation 1
prob_rolling_1 =0.166
prob_rolling_6 =0.166
prob_rolling_1_and_6 = 0.0
prob_rolling_1_or_6 = prob_rolling_1 + prob_rolling_6 - prob_rolling_1_and_6
print(f"The probability of rolling a 1 or a 6 on a die is: {prob_rolling_1_or_6:.2f}")

# variation 2
prob_action_or_comedy = 0.80
prob_action = 0.90
prob_comedy = 0.90
prob_action_and_comedy = prob_action + prob_comedy - prob_action_or_comedy
print(f"The probability of a movie being both action and comedy is: {prob_action_and_comedy:.2f}")
