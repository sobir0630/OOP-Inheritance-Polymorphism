class Vehicle:
    def show_info(self):
        return "Bu transport vositasi."

class Car(Vehicle):
    def show_info(self):
        return "Bu mashina. 4 ta gildirakli, yopiq kuzovli."

class Bike(Vehicle):
    def show_info(self):
        return "Bu mototsikl. 2 ta gildirakli, tez yuradi."

car = Car()
bike = Bike()

# Natijani chiqaramiz
print(car.show_info())   
print(bike.show_info()) 
