class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"{amount} som yechildi. Yangi balans: {self.balance}"
        else:
            return "Yetarli mablag mavjud emas."

    def get_interest(self):
        return "Foiz hisoblash aniqlanmagan."


class SavingsAccount(BankAccount):
    def get_interest(self):
        interest = self.balance * 0.05
        return f"Foiz: {interest} som (5%)"

    def withdraw(self, amount):
        if self.balance - amount < 10_000:
            return "Mablagni yechib bolmaydi. Hisobda kamida 10,000 qolishi kerak."
        return super().withdraw(amount)


class CheckingAccount(BankAccount):
    def get_interest(self):
        return "Bu hisob turiga foiz qollanilmaydi."

    def withdraw(self, amount):
        if self.balance - amount < -100_000:
            return "Overdraft limiti oshib ketdi."
        self.balance -= amount
        return f"{amount} som yechildi. Yangi balans: {self.balance}"
    
    
savings = SavingsAccount("Ali", 50_000)
checking = CheckingAccount("Vali", 20_000)

print(savings.get_interest())         
print(checking.get_interest())        

print(savings.withdraw(45_000))      
print(savings.withdraw(35_000))       

print(checking.withdraw(110_000))    
print(checking.withdraw(100_000))     
