# List

my_list = [1,2,3]
my_list_2 = [1, True,"Pramod"]

#indexing

print("Element at index 0:",my_list[0])

#changing an element
my_list[1] = 20
print("List after changing index at 1", my_list)

# appending- add the value at the end
my_list.append(4)
print("List after appending",my_list)

# extend - add a list to the list
my_list.extend([5,6])
print("List after extending",my_list)

#insert- kind of like replace,here we replace the object at the given index with the one given
my_list.insert(1,'a')
print("List aftre insert operation",my_list)

#remove
my_list.remove('a')
print("list after removing 'a'",my_list)

# copy
my_list_copy = my_list.copy()
print(my_list_copy)

# clear
# my_list.clear()
print("after clearing",my_list)

# sort
my_list_copy.sort()
print(my_list_copy)

#reverse

my_list_copy.reverse()
print(my_list_copy)

# squares

squares = [1,4,9,16]
print(squares[-1])
print(squares[-2])
print(squares[-3])

# how to check if list is empty

my_list = []
if not list:
    print("Empty")
else:
    print("Not empty")

# pop- deleting that index value

squares = [1,4,9,16]
print(squares.pop(2))