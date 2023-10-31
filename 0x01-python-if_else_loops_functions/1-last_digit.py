#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = -(-number % 10)
else:
    last_digit = number % 10
if last_digit == 0:
    second_string = "and is 0"
elif last_digit < 6:
    second_string = "and is less than 6 and not 0"
else:
    second_string = "and is greater than 5"
print("Last digit of", number, "is", last_digit, second_string)
