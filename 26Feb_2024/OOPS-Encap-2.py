class Bank:



    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self,amount):
        self.balance += amount

    def _withdraw(self,amount):
        self.balance -= amount

    def __show_balance(self):
        print("Your Balance",self.balance)

    def if_you_are_auth(self,flag):
        if flag:
            self.__show_balance()
        else:
            print("Not allowed")

    def do_with_bank_manager(self,amount):
        self._withdraw(amount=amount)




o1 = Bank()
o1.deposit(1000)
o1.do_with_bank_manager(500)
o1.if_you_are_auth(True)

o1.public_fn() # you can access even private variables using the functions,this is kind of a leniency provided by python


# To access private and protected method we need a function with the parameter having a flag,when flag is true
# that variables can be accessed only then