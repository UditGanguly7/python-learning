# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as input from the user.
marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# Check for total percentage
total_marks = (100 * (marks1 + marks2 + marks3)) / 300

if(total_marks>=40):
    print("You are pass:", total_marks) 
  
else:
    print("You are fail, try again next year:", total_marks)  