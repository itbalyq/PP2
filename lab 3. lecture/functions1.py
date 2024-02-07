def calculate_factorial(num):
    if num == 0:
        return 1
    return num * calculate_factorial(num-1)

result = calculate_factorial(5)
print(f"The factorial of 5 is: {result}")
