#Functions->block of code
# return type or non return type functions
# have parameters or dont have

# no return type no parameter
def say_hello():
    print("Hello")  #define

say_hello() # call

# no return but with argument

def say_hello_arg(name):
    print("Hello",name)

say_hello_arg("Neha")


# multiple arguments
def say_hello_args(name,age):
    print("Hello",name,age)

say_hello_args("Neha",35)

# default value

def say_hello_arg_default(name="Pramod"):
    print("Hello",name)

say_hello_arg_default() #if we dont pass any value then it takes default value, if we pass any value while caaling then the
# default value will be replaced

# arg with return type

def sum_num_arg_ret(a,b):
    return a+b

print(sum_num_arg_ret(1,2))







