class Courier:
    def __init__(self, name):
        self.name = name

    def delivery_range(self):
        return "Yetkazib berish masofasi aniqlanmagan."

    def calculate_fee(self, distance_km):
        return "Narx hisoblash usuli yo‘q."


class BikeCourier(Courier):
    def delivery_range(self):
        return "🚴‍♂️ Maksimal 5 km radiusda xizmat ko‘rsatadi."

    def calculate_fee(self, distance_km):
        return f"{distance_km * 3000} so‘m (velosiped)"


class CarCourier(Courier):
    def delivery_range(self):
        return "🚗 Maksimal 30 km radiusda xizmat ko‘rsatadi."

    def calculate_fee(self, distance_km):
        return f"{distance_km * 5000} so‘m (mashina)"


class DroneCourier(Courier):
    def delivery_range(self):
        return "🚁 Maksimal 10 km radiusda xizmat korsatadi, tepadan uchib boradi."

    def calculate_fee(self, distance_km):
        return f"{distance_km * 8000} som (drone — tez yetkazish)"


bike = BikeCourier("Ali")
car = CarCourier("Vali")
drone = DroneCourier("DronBot")

print(bike.delivery_range())
print(bike.calculate_fee(4))  

print(car.delivery_range())
print(car.calculate_fee(10)) 

print(drone.delivery_range())
print(drone.calculate_fee(3)) 
