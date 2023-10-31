#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = -number % 10
    last_digit *= -1
else:
    last_digit = number % 10
if last_digit == 0:
    second_string = f"and is 0"
elif last_digit < 6:
    second_string = f"and is less then 6 and not 0"
elif last_digit > 5:
    second_string = f"and is greater then 5"
# print(f"last digit of {number:d} is {last_digit:d} {second_string:d}")
print("Last digit of", number, "is", last_digit, second_string)
