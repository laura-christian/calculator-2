"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def prefix_calculator():
    while True:
        # choices = "q + - * / square cube pow mod"
        input_strings = raw_input(">>")
        tokenize = input_strings.split(" ")
        operator = tokenize[0]
        nums = [int(x) for x in tokenize[1:]]

        if operator == "q" :
            print "You will exit"
            break
        elif operator == "+":
            total = add(nums[0], nums[1])
            print total
        elif operator == "-":
            difference = subtract(nums[0], nums[1])
            print difference
        elif operator == "*":
            product = multiply(nums[0], nums[1])
            print product
        elif operator == "/":
            quotient = divide(nums[0], nums[1])
            print quotient
        elif operator == "square":
            squared = square(nums[0], nums[1])
            print squared