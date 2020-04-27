# Experiment with different ranges and slices to get a feel for how they work.
# Remember that you can print the range as well as iterating through it to print
# its values, to check that your ranges are what you expected.
# You may also want to include things like.
#
o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
for i in p:
    print(i)

# and see if you can work out what will be printed before running the program. If you are unsure, use a
# for loop to print out the values of o to see why p returns what it does.

#practice 1

c = range(0, 50, 5)
print(c)
for i in c:
    print(i)

# practice 2
c = range(0, 50, 5)
print(c)
f = c[::1]
for i in f:
    print(i)

# practice 3 - what changes?
c = range(0, 50, 5)
print(c)
f = c[::1]
for i in f:
    print(i)
# it prints the same as practice 2

# practice 4
c = range(0, 50, 5)
print(c)
f = c[::2]
for i in f:
    print(i)
# It prints from 0 - 40 in increments of 10

# practice 5
c = range(0, 50, 5)
print(c)
f = c[::3]
for i in f:
    print(i)
# It prints from 0 - 45 in increments of 15

# practice 6
c = range(0, 50, 5)
print(c)
f = c[::4]
for i in f:
    print(i)
# It prints from 0 - 40 in increments of 20 i.e. 0 20 40

# practice 5
c = range(0, 50, 5)
print(c)
f = c[::5]
for i in f:
    print(i)
# It prints 0 and 25 but not 50(which would be the next one) because it is up to but NOT including 50

# at a basic level it is taking the steps in the range(5 in these cases) and multiplying it by the last number in slice [] to give the step values
