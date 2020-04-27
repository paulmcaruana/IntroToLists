a = b = c = d = 12
print(c) # prints 12
a, b = 12, 13
print(a, b) # prints 12 13

a, b = b, a
print("a is {}".format(a)) # prints a is 13
print("b is {}".format(b)) # prints b is 12
