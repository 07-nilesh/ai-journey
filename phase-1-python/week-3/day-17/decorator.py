def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    print("Decorator executed this when the function is decorated")
    return wrapper_function

@decorator_function
def display():
    print("Display function ran")   

@decorator_function
def display_info(name, age):
    print("Display_info ran with arguments ({}, {})".format(name, age))     

display_info("Nilesh", 22) # This will call the decorated display_info function, which will execute the wrapper function first, printing the message and then calling the original display_info function with the provided arguments.
display()