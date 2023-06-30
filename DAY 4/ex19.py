def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# calling the functions with direct values
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# calling the functions with variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# calling the functions with maths
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# calling the function by combining math and variables.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def greet_person(name, greeting):
    print(f"{greeting}, {name}!")
    print(f"{greeting}, Good Morning {name}")
    print(f"{greeting}, Long time no see my good friend {name}")
    print(f"{greeting}, how was your night {name}")
    print(f"{greeting}, where have you been my friend {name}")

# 1. Calling the function with direct values
greet_person("Alice", "Hello")

# 2. Using variables from the script
person_name = "Bob"
greet_message = "Hi there"
greet_person(person_name, greet_message)

# 3. Combining variables and direct values
greet_person("Charlie", greet_message)

# 4. Doing math inside the function call
greet_person("David", f"Good{'bye' * 2}")

# 5. Using input from the user
input_name = input("Enter your name: ")
greet_person(input_name, "Greetings")

# 6. Using a variable and direct value with math
count = 3
greet_person("Emily", f"{'Hi ' * count}there")

# 7. Mixing variables and direct values
name = "Frank"
greeting = "Hola"
greet_person(name, greeting + "!")

# 8. Combining variables and direct values with math
name = "George"
greet_person(name + "s", "Hi" * 3)

# 9. Using variables with different values
greet_person("Hannah", greet_message.upper())

# 10. Using a function return value
def get_greeting():
    return "Salutations"

greet_person("Isabella", get_greeting())
