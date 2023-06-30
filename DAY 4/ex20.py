from sys import argv

# Get the script name and input file name from command-line arguments
script, input_file = argv

# Define a function to print the entire contents of a file
def print_all(f):
    print(f.read())

# Define a function to set the file position back to the beginning
def rewind(f):
    f.seek(0)

# Define a function to print a specific line from a file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open the input file
current_file = open(input_file)

print("First let's print the whole file:\n")


# Call the print_all function to print the contents of the file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# Call the rewind function to set the file position back to the beginning
rewind(current_file)

print("Let's print three lines:")

# Set the current line number to 1 and print the first line
current_line = 1
print_a_line(current_line, current_file)

# Increment the current line number by 1 and print the second line
current_line = current_line + 1
print_a_line(current_line, current_file)

# Increment the current line number by 1 again and print the third line
current_line = current_line + 1
print_a_line(current_line, current_file)



from sys import argv

# Get the script name and input file name from command-line arguments
script, input_file = argv

# Define a function to print the entire contents of a file
def print_all(f):
    print(f.read())

# Define a function to set the file position back to the beginning
def rewind(f):
    f.seek(0)

# Define a function to print a specific line from a file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open the input file
current_file = open(input_file)

print("First let's print the whole file:\n")

# Call the print_all function to print the contents of the file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# Call the rewind function to set the file position back to the beginning
rewind(current_file)

print("Let's print three lines:")

# Set the current line number to 1 and print the first line
current_line = 1
print_a_line(current_line, current_file)

# Increment the current line number by 1 and print the second line
current_line += 1
print_a_line(current_line, current_file)

# Increment the current line number by 1 again and print the third line
current_line += 1
print_a_line(current_line, current_file)
