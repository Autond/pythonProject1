class Password:



    def __init__(self,password):
        self.public_var = "public"
        self.__password = password


    def getpassword(self,is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("Invalid password")

    def setpassword(self,password):
        if len(password)>10:
            print("password set to",password)
        else:
            print("weak password")



P = Password("123")
P.getpassword(True)
P.setpassword("123")

