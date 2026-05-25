prob_success =0.05
prob_yc_given_success = 0.28
prob_overall =0.02

prob_success_given_yc = (prob_yc_given_success * prob_success) / prob_overall
print(f"The probability of a startup being successful given that it is funded by Y Combinator is: {prob_success_given_yc:.2f}")

# variation 1
prob_disease = 0.01
prob_test_positive_given_disease = 0.99
prob_overall_test_positive = 0.05

prob_disease_given_test_positive = (prob_test_positive_given_disease * prob_disease) / prob_overall_test_positive
print(f"The probability of having the disease given a positive test result is: {prob_disease_given_test_positive:.2f}") 

# variation 2
prob_spam = 0.20
prob_not_spam = 0.80
prob_contains_word_urgent_given_spam = 1.0
prob_contains_word_urgent_given_not_spam = 0.00
prob_contains_word_urgent = (prob_contains_word_urgent_given_spam * prob_spam) + (prob_contains_word_urgent_given_not_spam * prob_not_spam)
prob_spam_given_contains_word_urgent = (prob_contains_word_urgent_given_spam * prob_spam) / prob_contains_word_urgent
print(f"The probability that an email is spam given that it contains the word 'urgent' is: {prob_spam_given_contains_word_urgent:.2f}")
