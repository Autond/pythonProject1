class Car:
    color = None  # class variables declared as None
    model = None

    def cardetails(self):
        print("car details are ",self.color,self.model)


car_color = input("enter car color \n")  # taking user input for the class variables
car_model = input("enter car model \n")

car_obj_ref = Car()
car_obj_ref.color = car_color # creating obj reference and and assigning the user input to it
car_obj_ref.model = car_model

print(car_obj_ref.color) #printing the class variable values
print(car_obj_ref.model)

car_obj_ref.cardetails()
