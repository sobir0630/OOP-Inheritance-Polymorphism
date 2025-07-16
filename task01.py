class animals:
    def speak(self):
        return "some sound"
    
class dog(animals):
    def speak(self):
        return "woow"
    
class cat(animals):
    def speak(self):
        return "miaw"
    
dog = dog()
cat = cat()

print(dog.speak())
print(cat.speak())