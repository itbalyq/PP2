import math, time


#1
nums = [1, 2, 3, 4, 5]
output = math.prod(nums)
print(output)


#2
input_text = 'Test TExt'

upper_count = sum(1 for ch in input_text if ch.isupper())
lower_count = sum(1 for ch in input_text if ch.islower())

print(f"Upper count: {upper_count}")
print(f"Lower count: {lower_count}")


#3
text = 'Test TExt'

is_palindrome = True if text[::-1] == text else False

print(is_palindrome)


#5
tup = (True, 1, True, True)

def is_true(tup):
    return all(tup)

print(is_true(tup))


#4
num = int(input())
ms = int(input())

time.sleep(ms / 1000)
root = math.sqrt(num)
print(f"Square root of {num} after {ms} milliseconds is {root}")


