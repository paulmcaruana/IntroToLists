# decimals = range(0,100)
# my_range = decimals[3:40:3]
# print(my_range == range(3, 40, 3))
# print(range(0, 5, 2) == range(0, 6, 2)) # this is true because of below
# print(list(range(0, 5, 2))) # prints [0, 2, 4]
# print(list(range(0, 6, 2))) # prints [0, 2, 4]
#
# r = range(0, 100)
# print(r)
#
# for i in r[::-2]: # prints backwards from 100 in steps of 2
#     print(i)
#
# print("+" * 50)
# for i in range(99, 0, -2):
#     print(i)
#
# print("+" * 50)
# print(range(0, 100)[::-2] == range(99, 0, -2))
#
# for i in range(0, 100, -2): # won't work because you can't count back from 0 to 100
#     print(i)
backstring = "egaugnal lufrewop yrev a si nohtyp"
print(backstring[::-1])

r = range(0, 10)
for i in r[::-1]:
    print(i)
