# Tuple

# Tuple is immutable
#
my_list = [1,2,3]
# my_list[0] = 21
# print(my_list)
#
# # tuple
#
# my_tuple = (1,2,3)
# my_tuple[0] = 31
# print(my_tuple) #immutable

# convert list to tuple

# my_tup = tuple(my_list)
# print(my_tup)

# operations on tuple
# concatenation
# h1 = ("ball","bat")
# h2 = ("bad","tennis")
#
# h3 = h1 + h2
# print(h3)


# convert to list
# my_tup = (1,2,3)
# my_list = list(my_tup)
#
# print(my_list)


# tuple multiple assignment

q,w,e = (1,2,3)

# tuples within tuples
h1 = ("ball","bat")
h2 = ("bad","tennis")

h3 = (h1,h2)

print(h3) # (('ball', 'bat'), ('bad', 'tennis'))
print(h3[0][0])
print(h3[0][1])

# Search in tuple
cities = ("London","Paris","Tokyo")
print("Paris" in cities)


# tuple is a list of any data type items which cant be changed
# List is a collection of items  which can be changed and duplicated