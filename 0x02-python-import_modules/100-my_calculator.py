#!/usr/bin/python3

import calculator_1 as cal
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    if sys.argv[2] == '+':
        print("{} + {} = {}".format(num1, num2, num1 + num2))
        exit(0)
    elif sys.argv[2] == '-':
        print("{} + {} = {}".format(num1, num2, num1 - num2))
        exit(0)
    elif sys.argv[2] == '*':
        print("{} + {} = {}".format(num1, num2, num1 * num2))
        exit(0)
    elif sys.argv[2] == '/':
        print("{} + {} = {}".format(num1, num2, num1 / num2))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
