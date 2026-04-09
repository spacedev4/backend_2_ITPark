class Foydalanuvchilar:

    def __init__(self, username, name, last_name, email, location):
        self.username = username
        self.name = name
        self.last_name = last_name
        self.email = email
        self.location = location

    def toliq_info(self):
        return (f"Foydalanuvchi: {self.username}, ismi: {self.name} {self.last_name}, "
                f"email: {self.email}, manzil: {self.location}")

    def foydalanuvchi_bilan_salomlashish(self):

        print(f"Salom, {self.name}! Xush kelibsiz!")

user1 = Foydalanuvchilar("alijon1994", "Alijon", "Valiyev", "alijon1994@gmail.com", "Toshkent")
user2 = Foydalanuvchilar("malika_99", "Malika", "Anvarova", "m_anvarova@mail.ru", "Samarqand")

print(user1.toliq_info())
user1.foydalanuvchi_bilan_salomlashish()

print()

print(user2.toliq_info())
user2.foydalanuvchi_bilan_salomlashish()