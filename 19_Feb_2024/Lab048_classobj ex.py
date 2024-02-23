# class Cal:
#     def sum(self,a,b):
#         return a+b
#
#     def minus(self,c,d):
#         return c-d
#
# a = Cal()
# print(a.sum(10,20))
# print(a.minus(10,5))


# Multiple params

class mul_param:


    def print_information(self,firstname,lastname,age):
        print("Name and age is",firstname,lastname,age)

obj = mul_param()
print(obj.print_information("Amit","Sharma",39))

# To access args we dont need self keyword, we only need it for class variables
