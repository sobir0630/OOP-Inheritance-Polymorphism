class Appliance:
    def turn_on(self):
        return "Moslama yoqildi."

    def turn_off(self):
        return "Moslama ochirildi."

class TV(Appliance):
    def turn_on(self):
        return " TV yoqildi: Endi siz sevimli shoularingizni tomosha qilishingiz mumkin."

    def turn_off(self):
        return " TV ochirildi: Elektrni tejash boshlandi."

class Fridge(Appliance):
    def turn_on(self):
        return " Muzlatkich ishga tushdi: Mahsulotlar sovitilmoqda."

    def turn_off(self):
        return " Muzlatkich ochirildi: Sovutilish toxtatildi."

tv = TV()
fridge = Fridge()


print(tv.turn_on())
print(tv.turn_off())

print(fridge.turn_on())
print(fridge.turn_off())
