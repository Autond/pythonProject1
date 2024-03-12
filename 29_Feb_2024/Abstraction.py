# abstraction = hiding the details and showing what is required

# Abstract base class
# Abstarct base method

# child method has to implement the unimplemented abstract method if we want to use the child method

from abc import ABC,abstractmethod


class Animal:

    def __init__(self,name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass
class Dog:
    def sound(self):
        print("Bow bow")

d = Dog()
d.sound()