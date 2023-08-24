#!/usr/bin/python3
import random

number = random.randint(-10, 10)

if number > 0:
    print("Correct output - positive")
elif number == 0:
    print("Correct output - zero")
else:
    print("Correct output - negative")
