# ITS TIME TO COUNT THE CHICKENS
print("I will now count my chickens:")

# COUNT THE HENS AND THE ROOSTERS
print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)

# NOW COUNT THE EGGS
print("Now I will count the eggs:")

# SIMPLE ARITHMETIC USING THE MATHS SYMBOLS
print(float(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6))

# PRINTS THE STATEMENT AS A COMMENT COS ITS ALL IN A QUOTES
print("Is it true that 3 + 2 < 5 - 7?")

# PRINTS BOOLEAN VALUES
print(3 + 2 < 5 - 7)

# SIMPLE ARITHMETIC
print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

# PRINTS STATEMENT
print("Oh, that's why it's False.")
print("How about some more.")

# PRINTS BOOLEAN VALUES
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)



# a program that calculates the area of a circle
import math

def calculate_area(radius):
    area = math.pi * radius * radius
    return area

def main():
    radius = float(input("Enter the radius of the circle: "))

    area = calculate_area(radius)

    print("The area of the circle is:", area)

if __name__ == "__main__":
    main()


pie = int(3.142)
radius = int(input("Enter the radius of a circle: "))
area = pie * radius * radius
print(f"{area}, is the area of the circle.")