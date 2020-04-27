# my_list = list(range(10))
# print(my_list)
#
# even = list(range(0, 10, 2)) # remember the first is the start, 2nd is the last and third is the steps it takes
# odd = list(range(1, 10, 2))
#
# print(even)
# print(odd)
# my_string = "abcdefghijklmnopqrstuvwxyz"
# print(my_string.index('e')) # prints out the index number 4
# print(my_string[4]) # prints out the letter e
#
# small_decimals = range(0, 10)
# print(small_decimals)  # prints range(0, 10)
#
# print(small_decimals.index(3)) # prints 3
#
# odd = range(1, 10000, 2)
# print(odd) # prints range(1, 1000, 2)
#
# print(odd[985]) # prints the 985 number which is 1971
#
# sevens = range(7, 1000000, 7)
# x = int(input("Please enter a positive number less than one million: "))
# if x in sevens:
#     print("{} is dividible by seven".format(x))
#
# print(small_decimals)
#
# my_range = small_decimals[::2]
# print(my_range)
# print(my_range.index(4))
decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print("=" * 40)

for i in range(3, 40, 3):
    print(i)

print(my_range == range(3, 40, 3))

