#!/usr/bin/python3
for i in range(100):
    if 0 <= i <= 98:
        print(f"{i:02}, ", end="")
    elif i == 99:
        print(f"{i:02}")
