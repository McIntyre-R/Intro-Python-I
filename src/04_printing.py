"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("X is %2d, and y is %2.2f, Z is %16s" %(x,y,z))
# Use the 'format' string method to print the same thing
print('X is {0:2d}, and y is {1:2.2f}, Z is "{2:16s}"'.format(x,y,z))

# Finally, print the same thing using an f-string
print(f'X is{x}, and Y is {y}, Z is "{z}"')