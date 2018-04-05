"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic_2 import *


# Your code goes here
def prefix_calculator():
    while True:
        # choices = "q + - * / square cube pow mod"
        user_input = raw_input("Enter the desired operator followed by any number of integers, each separated by a space:\n>>")
        split_input = user_input.split(" ")
        operator = user_input[0]
        nums = [float(x) for x in split_input[1:]]

        if operator == "q":
            print "You have exited the calculator!"
            return
        elif operator == "+":
            print add(nums)
        elif operator == "-":
            print subtract(nums)
        elif operator == "*":
            print multiply(nums)
        elif operator == "/":
            print divide(nums)
        elif operator == "pow":
            print power(nums)
        elif operator == "mod":
            print mod(nums)


prefix_calculator()