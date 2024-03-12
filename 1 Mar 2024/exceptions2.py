class MyCustomException(Exception):
    def __init__(self,message):
        self.message = message
        super(). __init__(message)

balance = 100
withdraw_amount = int(input("enter withdrawal amount"))

if withdraw_amount > balance:
    raise MyCustomException("bal is low!")

else:
    print("Total after withdrawal",balance-withdraw_amount)
