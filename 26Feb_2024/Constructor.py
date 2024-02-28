#without constructor
import os


class Car1:

    name = None
    make = None
    model = None

    def cardetails(self,o_name,o_make,o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model
        print("starting a car with the name", self.name)
        print("starting a car with the make", self.make)
        print("starting a car with the model", self.model)


c1 = Car1()
c1.cardetails("lambo","v2","2024")

c2 = Car1()
c2.cardetails("hyundai","i20",2011)


# with constructor
# class Car:
#
#     name = None
#     make = None
#     model = None
#
#     def __init__(self,o_name,o_make,o_model):
#         self.name = o_name
#         self.make = o_make
#         self.model = o_model
#
#
#     def start_engine(self):
#         print("starting a car with the name", self.name)
#         print("starting a car with the make", self.make)
#         print("starting a car with the model", self.model)
#
#
# lambo = Car("lambo","v2","2024")
#
# lambo.start_engine()
