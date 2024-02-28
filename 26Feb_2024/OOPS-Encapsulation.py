#encapsulation

class Car:
    name = None



    def __init__(self,o_name):
        self.name = o_name
        self._protected = "protected123" # single _ means protected variable
        self.__priveate = "private123"  # double __ means private variable


    def _protectedmethod(self):
        print("protected",self._protected) # protected method cannot be accessed outside the class


    def __privatemethod(self):
        print("privatemethod",self.__priveate) # private method cannot be accessed outside the class


    def printvars(self):
        print("protected and private +name",self._protected,self.__priveate,self.name) #protected and private var can be accessed through this method only


o1 = Car("lambo")
o1.printvars()

