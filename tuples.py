# t = "a", "b", "c"
# print(t) # this returns/prints as tuple i.e. ('a', 'b', 'c')
#
# print("a", "b", "c") # this just prints a b c
# print(("a", "b", "c")) # this prints a tuple again i.e ('a', 'b', 'c')

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company" "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011, (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
metallica = "Ride the Lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

#metallica[0] = "Master of Puppets" # throughs an error as tuples are immutable
# imelda = imelda[0], "Imelda May", imelda[2]
# print(imelda)
#
# metallica2 = ["Ride the Lightning", "Metallica", 1984]
# # print(metallica2)
# # metallica2[0] = "Master of Puppets"
# # print(metallica2)
# print(metallica2)
#
# title, artist, year = imelda # this is called unpacking the tuple
# print(title)
# print(artist)
# print(year)
#
# metallica2.append("Rock")
#
# title, artist, year = metallica2
# print(title)
# print(artist)
# print(year)
#
# imelda.append("Jazz")
#
# print(imelda)
# # title, artist, year, tracks = imelda # unpacking the tuple now that the tracks are in
# print(title)
# print(artist)
# print(year)
# print(tracks)

# this prints More Mayhem
# Emilda May
# 2011
# ((1, 'Pulling the rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz'))

print(imelda)
title, artist, year, track1, track2, track3, track4 = imelda # unpacking the tuple now that the tracks are in
print(title)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)
print(track4)
