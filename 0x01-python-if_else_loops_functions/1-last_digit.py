#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = abs(number) % 10

if number < 0:
    sign = -1
else:
    sign = 1
lastd = (abs(number) % 10) * sign

if lastd > 5:
    print(f"Last digit of {number} is {lastd} and is greater than 5")
elif lastd == 0:
    print(f"Last digit of {number} is and is 0")
elif lastd < 6 and lastd != 0:
    print(f"Last digit of {number} is {lastd} and is less than 6 and not 0")
