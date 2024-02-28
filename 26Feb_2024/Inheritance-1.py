class Fat: #super,parent class
    __private_villa = "GOA"

    def drive_car(self):
        print("Has Car")

    def bhkflat(self):
        print("Has flat")

    def private_villa_access(self,is_son):
        print(self.__private_villa)


class son(Fat): # subclass,child class ,child inherits everything from parent except private methods and variables in which case we need to use encapsulation
    #to use that
        pass



Pra = son()
Pra.bhkflat()
Pra.drive_car()
Pra.private_villa_access(True)



