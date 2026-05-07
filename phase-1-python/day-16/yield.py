# Standard function (Memory heavy)
'''def my_range_list(n):
    result = []
    i = 0
    while i < n:
        result.append(i)
        i += 1
    return result

# Generator function (Memory efficient)
def my_range_generator(n):
    i = 0
    while i < n:
        yield i  # Pauses here and returns current i
        i += 1
print(my_range_list(5))  # Output: [0, 1, 2, 3, 4]
print(list(my_range_generator(5)))  # Output: [0, 1, 2, 3, 4]
'''
def even_infinite():
    n=0
    while True:
        yield n
        n+=2
evens=even_infinite()
print(next(evens))  
print(next(evens))
print(next(evens))
