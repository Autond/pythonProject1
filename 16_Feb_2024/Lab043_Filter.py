#Filter
# Can filter the item from the list based on the logic

# return less  number of items

# number = [1,2,3,4,5,6]
# even_nos = list(filter(lambda item : item%2==0, number))
#
# print(even_nos)

#Using function
number1 = [1,2,3,4,5,6]
def e_no(num):
    return num%2==0


e_nos = list(filter(e_no,number1))

print(e_nos)

