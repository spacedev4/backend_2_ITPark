class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def tanishtir(self):
        print(f"{self.ism} {self.familiya} {self.tyil} yilda tug'ilganman")

    def get_name(self):
        return self.ism

    def get_lastname(self):
        return self.familiya

    def get_fullname(self):
        return f"{self.ism} {self.familiya}"

    def get_age(self, yil):
        return yil - self.tyil


talaba1 = Talaba("Alijan", 'Valiyev', 2000)
# print(talaba1.ism)
# print(talaba1.familiya)
# print(talaba1.tyil)
# talaba2 = Talaba("Olim", 'Olimov', 1995)
# talaba3 = Talaba("Husan", "Akbarov", 2004)
# talaba4 = Talaba("Husan", "Akbarov", 2004)
# print(talaba2.ism)
# print((talaba4.tanishtir()))
print(talaba1.get_name())
print(talaba1.get_lastname())
print(talaba1.get_fullname())
print(talaba1.get_age(2026))





class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def describe(self):
        pass

    def get_email(self):
        pass