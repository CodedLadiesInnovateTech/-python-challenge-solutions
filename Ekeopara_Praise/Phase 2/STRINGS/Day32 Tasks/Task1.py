'''1. Write a Python program to print the following floating numbers upto 2 decimal places with a sign. '''

x = 3.1415926
y = -12.9999
print("\nOriginal Number: ", x)
print("Formatted Number with sign: "+"{:+.2f}".format(x))
print("Original Number: ", y)
print("Formatted Number with sign: "+"{:+.2f}".format(y))
print()

#Reference: w3resource 