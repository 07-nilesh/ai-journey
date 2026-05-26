#current study time in hours
study_hrs = 2
#this is how much extra time need to get more marks
time_slope = 0.01

#function which calculates score
def get_exam_score(hrs):
    return (hrs **2)

#score before extra study
score_before = get_exam_score(study_hrs)
print(f"Score before extra study: {score_before:.4f}")
#score after extra study
score_after = get_exam_score(study_hrs + time_slope)
print(f"Score after extra study: {score_after:.4f}")

#rate of change of score with respect to time (derivative)
score_slope = (score_after - score_before) / time_slope
print(f"Approximate derivative (score slope): {score_slope:.4f}")

# varition 1
#current study time in hours
study_hrs = 2
#this is how much extra time need to get more marks
time_slope = 0.01

#function which calculates score were 1hr=5marks
def get_exam_score(hrs):
    return (hrs * 5)

#score before extra study
score_before = get_exam_score(study_hrs)
print(f"Score before extra study: {score_before:.4f}")
#score after extra study
score_after = get_exam_score(study_hrs + time_slope)
print(f"Score after extra study: {score_after:.4f}")

#rate of change of score with respect to time (derivative)
score_slope = (score_after - score_before) / time_slope
print(f"Approximate derivative (score slope): {score_slope:.4f}")

# varition 2
#current study time in hours
study_hrs = [1,2,3,4,5]
#this is how much extra time need to get more marks
time_slope = 5.00

#function which calculates score 
def get_exam_score(hrs):
    return (hrs **2)

#score before extra study
for hr in study_hrs:
    score_before = get_exam_score(hr)
    print(f"Score before extra study for {hr} hrs: {score_before:.4f}")
    #score after extra study
score_after = get_exam_score(hr + time_slope)
print(f"Score after extra study for {hr} hrs: {score_after:.4f}")

    #rate of change of score with respect to time (derivative)
score_slope = (score_after - score_before) / time_slope
print(f"Approximate derivative (score slope) for {hr} hrs: {score_slope:.4f}\n")

