# Write a Python program to print the contents of a directory using the OS module. Search online for the function which does that.
import os

# Print the contents of the current directory
contents = os.listdir(".")

for item in contents:
    print(item)

# Write comments on the program above so that each and every line of program can be explained or understanded easily.