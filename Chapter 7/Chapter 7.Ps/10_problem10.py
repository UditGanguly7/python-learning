# Write a program to print multiplication table of a given number n using for loop in reveresed order. 
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {11-i} = {n * (11-i)}") 