class Character:
    def __init__(self, name):
        self.name = name

    def attack(self):
        return "⚔️ Hujum qilmoqda..."

    def defend(self):
        return "🛡️ Himoyalanmoqda..."


class Warrior(Character):
    def attack(self):
        return f"🗡️ {self.name} qilich bilan hujum qildi!"

    def defend(self):
        return f"🛡️ {self.name} qalqon bilan himoyalandi!"


class Mage(Character):
    def attack(self):
        return f"✨ {self.name} sehrli olov yubordi!"

    def defend(self):
        return f"🔮 {self.name} sehrli qalqon yaratdi!"


class Archer(Character):
    def attack(self):
        return f"🏹 {self.name} kamon bilan o‘q uzdi!"

    def defend(self):
        return f"🕊️ {self.name} chaqqonlik bilan hujumdan qochdi!"

warrior = Warrior("Temur")
mage = Mage("Zuhra")
archer = Archer("Bekzod")

print(warrior.attack()) 
print(warrior.defend())  

print(mage.attack())    
print(mage.defend())    

print(archer.attack())  
print(archer.defend())   
