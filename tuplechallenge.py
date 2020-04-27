# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).


#answer
# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# print(imelda)
#
# title, artist, year, tracks = imelda # unpacking the tuple now that the tracks are in
# print(title)
# print(artist)
# print(year)
# for song in tracks:
#     print("\t", song)

# tuples that contain lists within them. Tuple is immutable but the list inside it is mutable
imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")]) #list that contains tuples

print(imelda)

imelda[3].append((5, "All For You"))  # this will append a tuple to the end of the tuples in the list

title, artist, year, tracks = imelda # unpacking the tuple now that the tracks are in
tracks.append((6, "Eternity")) # appends another tuple to the list of tuples
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))

