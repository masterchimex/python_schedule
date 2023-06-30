# from sys import argv
# # read the WYSS section for how to run this
# script, first, second, third = argv

# import os

# cwd = os.getcwd() # Get the current working directory (cwd)
# files = os.listdir(cwd) # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)


def process_user_data(name, age):
    # Process user data
    print("Name:", name)
    print("Age:", age)

# Collect user data
user_data = input("Enter your name and age (separated by a comma): ")

# Unpack user data
name, age = user_data.split(",")

# Call the function with unpacked variables
process_user_data(name.strip(), age.strip())


def process_user_data(name, age, email, address):
    # Process user data
    print("Name:", name)
    print("Age:", age)
    print("Email:", email)
    print("Address:", address)

# Collect user data
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")
address = input("Enter your address: ")

# Call the function with arguments
process_user_data(name, age, email, address)


import sys

# Get input from command-line argument
arg_value = sys.argv[1] if len(sys.argv) > 1 else ""
print("Command-line argument value:", arg_value)

# Get additional input from the user
user_input = input("Enter something: ")
print("User input:", user_input)
