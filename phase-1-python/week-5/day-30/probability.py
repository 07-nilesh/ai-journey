prob_pitch_is_dusty_bowl=0.2
prob_ashwin_takes_5_wickets=0.25
prob_ashwin_takes_5_wickets_given_dusty_bowl=0.8

# Using Bayes' Theorem to find the probability that the pitch is dusty given that Ashwin takes 5 wickets
prob_dusty_bowl_given_ashwin_takes_5_wickets = (prob_ashwin_takes_5_wickets_given_dusty_bowl * prob_pitch_is_dusty_bowl) / prob_ashwin_takes_5_wickets
print(f"The probability that the pitch is dusty given that Ashwin takes 5 wickets is: {prob_dusty_bowl_given_ashwin_takes_5_wickets:.2f}")

# variation 1
prob_spam_email=0.10
prob_contains_word_lottery=0.05
prob_contains_word_lottery_given_spam=0.50

prob_spam_given_contains_word_lottery = (prob_contains_word_lottery_given_spam * prob_spam_email) / prob_contains_word_lottery
print(f"The probability that an email is spam given that it contains the word 'lottery' is: {prob_spam_given_contains_word_lottery:.2f}")

# variation 2
prob_spam=0.90
prob_not_spam=0.10
prob_contains_word_lottery_given_spam=0.00
prob_contains_word_lottery_given_not_spam=0.50
prob_contains_word_lottery = (prob_contains_word_lottery_given_spam * prob_spam) + (prob_contains_word_lottery_given_not_spam * prob_not_spam)
prob_spam_given_contains_word_lottery = (prob_contains_word_lottery_given_spam * prob_spam) / prob_contains_word_lottery
print(f"The probability that an email is spam given that it contains the word 'lottery' is: {prob_spam_given_contains_word_lottery:.2f}")