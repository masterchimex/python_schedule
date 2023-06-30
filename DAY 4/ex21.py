def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

# Perform calculations using the defined functions

print("Let's do some math with just functions!")

# Call the add function and assign its return value to 'age'
age = add(30, 5)

# Call the subtract function and assign its return value to 'height'
height = subtract(78, 4)

# Call the multiply function and assign its return value to 'weight'
weight = multiply(90, 2)

# Call the divide function and assign its return value to 'iq'
iq = divide(100, 2)

# Print the calculated values
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

# Perform nested calculations using the defined functions
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# Print the result of the puzzle
print("That becomes:", what, "Can you do it by hand?")


def square(x):
    print(f"SQUARING {x}")
    return x * x

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

# Calculate the value of the formula: (10^2) - (6 / 2)

# Call the square function to calculate 10^2
result1 = square(10)

# Call the divide function to calculate 6 / 2
result2 = divide(6, 2)

# Call the subtract function to calculate (10^2) - (6 / 2)
final_result = subtract(result1, result2)

print("The result of the formula is:", final_result)
