# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list.

# henrik = "henrik larsson"
#
# my_iterator = iter(henrik)
#
# for my_iterator in iter(henrik):
#     print((my_iterator))
# I have doen the same as his previous example. Could have used the celtic_defence = ["Julien", Ajer".....]

# tim's solution and example

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

my_iterator = iter(my_list)

for i in range(0, len(my_list)):
    next_item = next(my_iterator)
    print(next_item)

# you would in practice use my version or the below

for i in my_list:
    print(i)

