class Shaxs:
    __odamlar_soni = 0

    def __init__(self, ism, login):
        self.__ism = ism
        self.__login = login
        Shaxs.__odamlar_soni += 1

    def get_ism(self):
        return self.__ism

    def set_ism(self, yangi_ism):
        self.__ism = yangi_ism

    @classmethod
    def get_odamlar_soni(cls):
        return f"Jami odamlar soni: {cls.__odamlar_soni}"

    def get_info(self):
        return f"Ism: {self.__ism}, Login: {self.__login}"


class Talaba(Shaxs):
    __talabalar_soni = 0

    def __init__(self, ism, familiya, login):
        super().__init__(ism, login)
        self.__familiya = familiya
        self.__fanlar = []
        Talaba.__talabalar_soni += 1

    @classmethod
    def get_talabalar_soni(cls):
        return f"Jami talabalar soni: {cls.__talabalar_soni}"

    def fanga_yozil(self, fan_obyekti):
        self.__fanlar.append(fan_obyekti)

    def get_fanlar(self):
        return [f.nomi for f in self.__fanlar]

    def remove_fan(self, fan_nomi):
        for f in self.__fanlar:
            if f.nomi == fan_nomi:
                self.__fanlar.remove(f)
                return f"{fan_nomi} o'chirildi."
        return "Siz bu fanga yozilmagansiz"


class Fan:
    def __init__(self, nomi):
        self.nomi = nomi



t1 = Talaba("Ivan", "Ivanov", "ivan77")
t2 = Talaba("Asilbek", "Abduvokhidov", "asil01")

print(t1.get_ism())
t1.set_ism("Vanya")
print(t1.get_ism())

print(Shaxs.get_odamlar_soni())
print(Talaba.get_talabalar_soni())