# A spam comment is defined as a text containing following keywords:
# "make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams. The program takes as input a text and checks whether the text is a spam or not.
p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Subscribe this"
p4 = "Click this"

message = input("Enter the comment: ")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam ")

else:
    print("This comment is not a spam ")  