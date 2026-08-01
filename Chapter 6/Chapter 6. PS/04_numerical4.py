# Write a program to find whether a given username contains less than 10 characters or not. If it contains less than 10 characters, then print a message "Valid username" otherwise print "Invalid username".
username = input("Enter your username: ")

if(len(username)<10):
    print("Valid username contains less than 10 characters")
else: 
    print("Invalid username contains more than or equal to 10 characters") 