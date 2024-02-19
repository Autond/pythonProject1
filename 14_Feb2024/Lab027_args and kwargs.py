# args and kwargs
#
# def print_argument(*args):  # we can give any number of arguments while calling this function
#     for i in args:
#         print(i,end=" ")
#
# print_argument(1)
# print_argument(1,2)
# print_argument(1,2,3)
#
#
# def make_pizza(*toppings):
#     print(toppings)
#
# make_pizza("Olives","onion","tomato")
# make_pizza("mushroom")



def make_pizza_base(*toppings,base):
    print(toppings,base)

neha = make_pizza_base("Olives","onion","tomato" , base="thin")
#make_pizza("mushroom")


# def make_pizza_base(*toppings,*base): this is not allowed
# multiple * args are not allowed.


