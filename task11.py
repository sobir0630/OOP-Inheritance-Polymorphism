class Product:
    def __init__(self, name):
        self.name = name

    def get_delivery_method(self):
        return "Yetkazib berish usuli aniqlanmagan."

    def download(self):
        return "⛔ Yuklab olish mumkin emas."


class PhysicalProduct(Product):
    def get_delivery_method(self):
        return f"📦 '{self.name}' kur'er orqali yoki pochta bilan yetkaziladi."

    def download(self):
        return "⛔ Jismoniy mahsulotni yuklab olib bo‘lmaydi."


class DigitalProduct(Product):
    def get_delivery_method(self):
        return f"📧 '{self.name}' elektron pochta yoki havola orqali yuboriladi."

    def download(self):
        return f"⬇️ '{self.name}' yuklab olinmoqda..."


# Test qilish
book = PhysicalProduct("Python kitobi")
ebook = DigitalProduct("Python PDF")

print(book.get_delivery_method())   
print(book.download())              

print(ebook.get_delivery_method())  
print(ebook.download())             
