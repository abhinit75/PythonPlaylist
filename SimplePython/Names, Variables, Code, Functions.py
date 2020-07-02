'''
Functions do three things:
1. They name peices of code the way variables name strings and numbers
2. They take arguments the way your scripts take argv
3. Using 1 and 2, they let you make your own "mini-scripts" or "tiny commands"
'''
'''

# this one is like your scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# ok, that *args is actually pointlss, we can just do this


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument


def print_one(arg1):
    print(f"arg1: {arg1}")


# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Abhi", "P")
print_two_again("Abhi", "P")
print_one("First!")
print_none()


'''
'''
Methods of passing arguments in function

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("Man thats enough for a party!")
    print("Get a blanket.n \n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("And wde can combine the two, variables and math")
cheese_and_crackers(amount_of_crackers + 100, amount_of_crackers + 1000)
'''

'''
def sum(a, b):
    x = a + b
    print(f"The sum is {x}")


sum(25, 80)

from sys import argv

script, input_file = argv, argv
input_file = "sonnet29.txt"


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)

print("First let's print the whole file: \n")

print_all(current_file)

print_a_line("Now let's rewind, kind of like a tape")

rewind(current_file)

print("Let's print three lines")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

'''


def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a,b):
    print(f"SUBTRACTING {a} = {b}")
    return  a - b


def multiply(a, b):
    print(f'MULTIPLYING {a} * {b}')
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


