prob_A = float(input("Enter the probability of event A (between 0 and 1): "))
prob_not_A = 1 - prob_A
prob_evidence_given_A = float(input("Enter the probability of evidence given event A (between 0 and 1): "))
prob_evidence_given_not_A = float(input("Enter the probability of evidence given not event A (between 0 and 1): "))
prob_evidence = (prob_evidence_given_A * prob_A) + (prob_evidence_given_not_A * prob_not_A)
prob_A_given_evidence = (prob_evidence_given_A * prob_A) / prob_evidence
print(f"The probability of event A given the evidence is: {prob_A_given_evidence:.2f}")
