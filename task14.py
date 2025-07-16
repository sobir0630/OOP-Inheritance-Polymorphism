class User:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return "👤 Foydalanuvchi kimligini aniqlab bo‘lmadi."


class Applicant(User):
    def __init__(self, name, desired_position):
        super().__init__(name)
        self.desired_position = desired_position

    def introduce(self):
        return f"🙋‍♂️ Men {self.name}, '{self.desired_position}' lavozimiga ish qidirmoqdaman."


class Employer(User):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def introduce(self):
        return f"🤝 Men {self.name}, '{self.company}' kompaniyasi nomidan ish beruvchiman."

applicant = Applicant("Ali", "Backend Developer")
employer = Employer("Zaynab", "TechPro")

print(applicant.introduce())

print(employer.introduce())
