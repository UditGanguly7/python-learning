# Write a python program using function to convert Celsius to Fahrenheit.
def f_to_c(f):
    return (f - 32) * 5/9

f = int(input("Enter temperature in Fahrenheit: "))
 #print(f_to_c(f)) or can also be written in this way
# print(f"{f_to_c(f)} °C")  or can be written in this way

c = f_to_c(f) 
print(f"{round(c, 2)}°C") 