name = 'CHUKWU A CHIEMELA'
age = 35 # not a lie
height = 84 # inches
weight = 180 # lbs
eyes = 'White'
teeth = 'White'
hair = 'Black'

# Constants for conversion
inch_to_cm = 2.54  # Conversion factor from inches to centimeters
pound_to_kg = 0.453592  # Conversion factor from pounds to kilograms

# Conversion formulas
centimeters = height * inch_to_cm
kilograms = weight * pound_to_kg

print(f"Let's talk about {name}.")
print(f"He's {centimeters} centimeters tall.")
print(f"He's {kilograms} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {centimeters}, and {kilograms} I get {total}.")