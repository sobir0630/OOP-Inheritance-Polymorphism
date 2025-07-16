class User:
    def __init__(self, name):
        self.name = name

    def get_dashboard(self):
        return "📋 Boshqaruv paneli mavjud emas."


class Student(User):
    def __init__(self, name, enrolled_courses):
        super().__init__(name)
        self.enrolled_courses = enrolled_courses

    def get_dashboard(self):
        courses = ', '.join(self.enrolled_courses)
        return f"👨‍🎓 {self.name} uchun dashboard:\n- Kurslar: {courses}"


class Instructor(User):
    def __init__(self, name, total_students, courses_created):
        super().__init__(name)
        self.total_students = total_students
        self.courses_created = courses_created

    def get_dashboard(self):
        return (f"👨‍🏫 {self.name} uchun dashboard:\n"
                f"- Yaratilgan kurslar: {', '.join(self.courses_created)}\n"
                f"- Umumiy talabalar soni: {self.total_students}")


student = Student("Ali", ["Python Asoslari", "Web Dasturlash"])
instructor = Instructor("Zaynab", 320, ["Python Asoslari", "OOP", "Django"])

print(student.get_dashboard())


print(instructor.get_dashboard())

