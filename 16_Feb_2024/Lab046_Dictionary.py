# Dict - unordered collection of data in key value format
# key  value

# name = "Pramod"
# #
# my_dict = {}
#
# phone_book = {"batman":91 , "superman":92}
# print(phone_book["batman"])
#
# dict1 = {'a':1,'b':2 , 'a':3}
# print(dict1) # in case of duplicates ,latest value is kept
#
# keys = dict1.keys()
# values = dict1.values()
#
# my_dict = {'a':1, 'b':2, 'c': 3}
# val = my_dict.pop('a')
# print(val)

#
# flowers = {'a':'lily', 'b':'lotus'}
# print(len(flowers))
#
# for k,v in flowers.items():
#     print(k,v)


# originally  dict is not ordered
# to make it ordered use ordered dict function

from collections import OrderedDict

od = OrderedDict()
od['a'] = 45
od['b'] = 43
od['c'] = 89


print(od)
