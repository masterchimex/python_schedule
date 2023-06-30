# ASSIGN A VALUE TO THE VARIABLE
types_of_people = 10

# FORMAT STRINGS
x = f"There are {types_of_people} types of people."

# ASSIGN VALUES TO VARIABLES
binary = "binary"
do_not = "don't"

# FORMAT STRINGS
y = f"Those who know {binary} and those who {do_not}."

# PRINT THE RESULT
print(x)
print(y)

#PRINTING USING FORMAT STRINGS
print(f"I said: {x}")
print(f"I also said: '{y}'")

# ASSIGN VALUES TO VARIABLES
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#PRINTING USING FORMAT STRINGS
print(joke_evaluation.format(hilarious))

# ASSIGN VALUES TO VARIABLES
w = "This is the left side of..."
e = "a string with a right side."

# CONCATENATING TWO STRINGS WILL GIVE YOU A LONGER STRINGS.
print(w + e)