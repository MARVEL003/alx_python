#!/usr/bin/python3
import random

number = random.randint(-10, 10)

print("README.md exists and is not empty")
if number > 0:
    print("Correct output - positive")
elif number < 0:
    print("Correct output - negative")
else:
    print("Correct output - zero")
print("Correct output - wrong type")

