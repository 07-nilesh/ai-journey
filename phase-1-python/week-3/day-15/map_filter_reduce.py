tasks=[120, 450, 90, 600, 210, 80, 550]

# Uses map to convert those remaining tasks from milliseconds to seconds (divide by 1000)
tasks_in_seconds = list(map(lambda x: x/1000, tasks))
print(f"Tasks in seconds: {tasks_in_seconds} ")

#Uses filter to keep only tasks that take more than 200ms
long_tasks= list(filter(lambda x:x>200, tasks ))
print(f"Long tasks: {long_tasks}")

#Uses reduce to calculate the total time taken by all tasks
from functools import reduce
total_time = reduce(lambda x, y: x + y, tasks)  
print(f"Total time taken by all tasks: {total_time} ms")
print(list(map(lambda x: x * 2, filter(lambda x: x > 10, [5, 12, 8, 20]))))