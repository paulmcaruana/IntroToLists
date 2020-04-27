# list_1 = []
# list_2 = list()
#
# print("list 1: {}".format(list_1))
# print("list 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal")
#
# print(list("The lists are equal"))
# # the above prints ['T', 'h', 'e', ' ', 'l', 'i', 's', 't', 's', ' ', 'a', 'r', 'e', ' ', 'e', 'q', 'u', 'a', 'l']

# even = [2, 4, 6, 8]
#
# another_even = list(even)
#
# print(another_even == even)  # asks if the contents of the lists are the same
# print(another_even is even)  # asks if they are the same list
#
# another_even.sort(reverse=True)
# print(even)
#
# # prints [8, 6, 4, 2]

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = [even, odd]
# print(numbers)
# # prints out [[2, 4, 6, 8], [1, 3, 5, 7, 9]]

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)

# the above prints
# [2, 4, 6, 8]
# 2
# 4
# 6
# 8
# [1, 3, 5, 7, 9]
# 1
# 3
# 5
# 7
# 9