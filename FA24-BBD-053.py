#Muhammed Wasif Zawar         FA24-BBD-053



#Question1
#Create a function named greet_with_time that takes a name as input and prints a greeting message along with the current time
print("Date Time Function:")
import datetime
def greet_with_time(name):
    current_time = datetime.datetime.now()
    print(f"Hello,{name}! The current time is {current_time}.")
greet_with_time("Mozzam")




#Question2
#Write a function called calculate_average that takes three numbers as input and returns their average.
print("\nFunction with Multiple Parameters:")
def calculate_average(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    return average
result = calculate_average(10, 20, 30)
print(f"The average is: {result}")




#Question3
#Define a function calculate_discount that takes a price and a discount percentage as input. Set a default discount percentage of 10%.
print("\nDefault Argument:")
def calculate_discount(price, discount_percentage=10):
    discounted_price = price - (price * discount_percentage / 100)
    return discounted_price
original_price = 1000
discounted_price = calculate_discount(original_price)
print(f"The discounted price is: {discounted_price}")
discounted_price_custom = calculate_discount(original_price, 20)
print(f"The discounted price with a 20% discount is: {discounted_price_custom}")



#Question4
#Create a function print_info that takes a name, age, and city as keyword arguments.
print("\nKeyword Arguments:")
def print_info(*, name, age, city):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
print_info(name="Mozzam", age=19, city="Lahore")




#Question5
#Write a function find_max that can take any number of arguments and returns the maximum value.
print("\nVariable-Length Arguments:")
def find_max(*args):
    if not args:
        return None
    return max(args)
max_value = find_max(10, 20, 30, 5, 40)
print(f"The maximum value is: {max_value}")
no_value = find_max()
print(f"The result with no arguments is: {no_value}")




#Question6
#Implement a recursive function to calculate the factorial of a number.
print("\nRecursive Function:")
def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1)  
print(factorial(8))  




#Question7
#Define a function apply_function that takes a function and a list of numbers as input. Apply the function to each number in the list and return a new list with the results.
print("\nFunction as an Argument:")
def apply_function(func, numbers):
    return [func(num) for num in numbers]
def square(x):
    return x * x
nums = [1, 2, 3, 4, 5]
squared_nums = apply_function(square, nums)
print(squared_nums)  




#Question8
#Create a lambda function to square a number.
print("\nLambda Functions:")
square = lambda x: x * x
result = square(5)
print(result)  




#Question9
#Write a function apply_operation that takes a function and a list of numbers. Apply the function to each number and return a new list.
print("\nHigher-Order Functions:")
#Higher-order Function
def apply_operation(func, numbers):
    return [func(num) for num in numbers]
result = apply_operation(lambda x: x ** 2, [1, 2, 3, 4])
print(result)  




#Question10
#Implement a decorator to measure the execution time of a function.
print("\nFunction Decorators:")
import time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs)  
        end_time = time.time()  
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper
@measure_time
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total
result = example_function(1000000)
print(f"Result: {result}")
