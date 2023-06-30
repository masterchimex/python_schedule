from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()


from sys import argv
from os.path import exists

script, from_file, to_file = argv

# Open the input file and read its contents
with open(from_file, 'r') as in_file:
    indata = in_file.read()

# Check if the output file already exists
file_exists = exists(to_file)

# Open the output file and write the contents
with open(to_file, 'w') as out_file:
    out_file.write(indata)

# Provide feedback to the user
print(f"File '{from_file}' copied to '{to_file}'.")
if file_exists:
    print("Note: The output file already existed and has been overwritten.")


""" the out_file.close() statement is used to explicitly close the output file after writing to it. Closing a file is an important step to ensure that any pending writes are flushed, and system resources associated with the file are released.

In Python, when a file is opened using the open() function, it is good practice to close the file when you are done working with it. Closing the file explicitly allows you to control the timing of the file closure and ensures that any buffered data is written to disk.

While it is true that Python will automatically close the file when the program execution finishes, it's still recommended to close the file explicitly to free up resources as soon as they are no longer needed. This practice becomes more critical when working with a large number of files or in scenarios where files need to be accessed by other processes.

In some cases, failing to close a file explicitly may not cause immediate issues, but it can lead to resource leaks or unexpected behavior in more complex programs. Therefore, it is considered a best practice to close files explicitly after you are done working with them, even though Python provides some automatic cleanup mechanisms.
"""