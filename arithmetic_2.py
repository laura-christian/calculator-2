"""Math functions for calculator allowing for multiple inputs"""

def add(array):
    return reduce(lambda x,y: x+y, array)

def subtract(array):
    return reduce(lambda x,y: x-y, array)

def multiply(array):
    return reduce(lambda x,y: x*y, array)

def divide(array):
    return reduce(lambda x,y: x/y, array)


