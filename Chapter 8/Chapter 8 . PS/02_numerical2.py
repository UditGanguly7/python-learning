# Write a python program using function to convert celsius to fahrenheit.
def f_to_c(f):
    c = (f - 32) * 5/9

f = int(input("Enter temperature in F: "))
c = f_to_c(f) 
print(f"{f_to_c(c, 2)} Degree C")   