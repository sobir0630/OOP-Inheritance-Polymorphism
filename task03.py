class User:
    def access_level(self):
        return "Foydalanuvchi darajasi noma'lum."

class Admin(User):
    def access_level(self):
        return "Toliq huquqli admin: barcha tizimga kirish mumkin."

class Guest(User):
    def access_level(self):
        return "Mehmon foydalanuvchi: faqat korish huquqi mavjud."

admin = Admin()
guest = Guest()


print(admin.access_level())  
print(guest.access_level())  
