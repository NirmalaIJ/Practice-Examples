##modify or extend the behavior of functions or methods, without changing their actual code
##
##A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality
##
##
##Syntax of Decorator Parameters
##def decorator_name(func):
##    def wrapper(*args, **kwargs):
##        # Add functionality before the original function call
##        result = func(*args, **kwargs)
##        # Add functionality after the original function call
##        return result
##    return wrapper
##
##
##@decorator_name
##def function_to_decorate():
##    # Original function code
##    pass


def decorator_method(func):
    def wrapper_func(*args, **kwargs):
        price = args[0]
        disc = args[1] + 0.05
        result = func(price, disc)
        print("with decorator", result)

        print("result", result)
        return result
    return wrapper_func

@decorator_method
def calculate_price(price, disc):
    finqal_price = price * (1-disc)
    print("without decorator", finqal_price)
    print(finqal_price)
    return finqal_price
print("final decorator")
print(calculate_price(1000, 0.05)    )
