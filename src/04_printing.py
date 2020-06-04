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
# requires a string on the left-hand side and a value or a tuple of values or a mapping obj on the right-hand side
# print('x is %x, y is %y, z is {z}' %

# Use the 'format' string method to print the same thing
string = "x is {fx}, y is {fy}, z is {zy}".format(fx=x, fy=y, zy=z)
print(string)

# Finally, print the same thing using an f-string
print(f'x is {x}, y is {y}, z is {z}')
