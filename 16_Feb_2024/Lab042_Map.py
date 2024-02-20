#Map() is a function

#
# def square_of_a_number(num):
#     return num ** 2
#
# numbers  = [1,2,3,4]
#
# sq = list(map(square_of_a_number,numbers)) # map(fun name,list)
# print(sq)

import math

def sq_root(num):
    return math.sqrt(num)
my_list = [1,2,3,4]

sq_of_all = list(map(sq_root,my_list))
print(sq_of_all)




