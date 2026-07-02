def outer_function(msg):
    print("Outer function called with message:", msg)
    def inner_function():
        print(msg)
    return inner_function  #python creates a closure here, inner_function retains access to msg
hi_func = outer_function("Hi")  # This will call the outer function and return the inner function, which is assigned to hi_func
bye_func = outer_function("Bye")    
print(hi_func()) 
bye_func()