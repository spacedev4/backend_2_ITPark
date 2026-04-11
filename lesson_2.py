class Talaba:
    """Talaba nomli class yaratamiz"""

    def __init__(self, ism, familiya, tyil):
        """Talaaning xususiyatlari"""
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        self.bosqich = 1

    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"
    def set_bosqich(self, bosqich):
        """talabaning kursini yangilovchi metod"""
        self.bosqich=bosqich
    def update_bosqich(self):
        """talabaning bosqichini 1taga ko'paytirish"""
        self.bosqich += 1
    def get_name(self):
        return self.ism
    def get_lastname(self):
        return self.familiya
    def get_fullname(self):
        return f"{self.ism} {self.familiya}"
    def get_age(self, yil):
        return yil - self.tyil

class Fan:
    def __init__(self, nomi):
        self.nomi=nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_stundents(self):
        return [talaba.get_info() for talaba in self.talabalar]

    def get_students_num(self):
        return self.talabalar_soni


matematika = Fan("Oliy matematika")
talaba1 = Talaba("Alijon", 'Valiyevv', 2000)
talaba2 = Talaba("Hasan", 'Alimov', 2001)
talaba3 = Talaba("Akrom", "Boriyev", 2001)

print(talaba3.get_age(2026))

matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

print(matematika.get_students_num())
print(matematika.talabalar_soni)
mat_talabalar = matematika.get_stundents()
print(mat_talabalar)

talaba1 = Talaba("Alijon", "Valiyev", 2000)
print(talaba1.get_info())
talaba1.bosqich = 2
print(talaba1.bosqich)
print(talaba1.get_info())
talaba1.set_bosqich(3)
talaba1.update_bosqich()
talaba1.update_bosqich()
print(talaba1.get_info())

talaba1 = Talaba("Alijon", 'Valiyevv', 2000)
print(dir(Talaba))

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith("__") is False]
print(see_methods(Talaba))
print(see_methods(talaba1))