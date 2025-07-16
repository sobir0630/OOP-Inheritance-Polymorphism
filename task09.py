class Notification:
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    def send(self):
        return "Xabar yuborish usuli aniqlanmagan."


class EmailNotification(Notification):
    def send(self):
        return f"📧 Email yuborildi: '{self.message}' → {self.recipient}"


class SMSNotification(Notification):
    def send(self):
        return f"📱 SMS yuborildi: '{self.message}' → {self.recipient}"


email = EmailNotification("ali@example.com", "Parolingiz muvaffaqiyatli o‘zgartirildi.")
sms = SMSNotification("+998901234567", "Hisobingizdan 200,000 so‘m yechildi.")

print(email.send())

print(sms.send())
