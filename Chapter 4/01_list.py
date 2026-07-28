friends = ["Apple", "Orange", 5, 345.06, "Akash", "Rohan"] 

print(friends[1])   

print(friends[0])
friends[0] = "Grapes"  # Unlike Strings lists are mutable, we can change the value of a list item by referring to its index number.

print(friends[0])  # Output: Grapes 
print(friends[1:4])  # Output: ['Orange', 5, 345.06] 