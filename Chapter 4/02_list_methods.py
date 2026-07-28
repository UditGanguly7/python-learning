friends = ["Apple", "Orange", 5, 345.06, "Akash", "Rohan"] 
print(friends)

friends.append("Udit")    # 1
print(friends)  # Output: ['Apple', 'Orange', 5, 345.06, 'Akash', 'Rohan', 'Udit']

numbers = [3, 1, 2, 1]       
numbers.insert(1, 10)  # Insert 10 at index 1   # 2
print(numbers) # Output: [3, 10, 1, 2, 1]

numbers.remove(1)  # Remove first occurrence of 1   # 3
print(numbers) # Output: [3, 10, 2, 1]   

numbers.sort()  # Sort the list in ascending order   # 4
print(numbers) # Output: [1, 2, 3, 10] 

numbers.reverse()  # Reverse the list   # 5
print(numbers) # Output: [10, 3, 2, 1]

numbers.extend([4,5,6])  # Extend the list by appending elements from another list   # 6
print(numbers) # Output: [10, 3, 2, 1, 4, 5, 6]