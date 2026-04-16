# class Shaxs:
#     def __init__(self, ism, familiya, passport, tyil):
#         self.ism=ism
#         self.familiya=familiya
#         self.passport=passport
#         self.tyil=tyil
#
#     def get_info(self):
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport: {self.passport}, {self.tyil}-yilda tug'ilgan"
#         return info
#
#     def get_age(self, yil):
#         return yil - self.tyil
#
# class Talaba(Shaxs):
#     def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam=idraqam
#         self.bosqich = 1
#         self.manzil=manzil
#
#     def get_id(self):
#         return self.idraqam
#
#     def get_bosqich(self):
#         return self.bosqich
#
#     def get_info(self):
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.get_id()}"
#
# inson = Shaxs("Hasan", "Alimov", "FB001122", 1995)
#
#
# # print(inson.get_info())
# # print(talaba.get_info())
# # print(talaba.get_age(2026))
# # print(talaba.get_id())
# # print(talaba.get_bosqich())
#
# class Manzil:
#     def __init__(self, uy, kocha, tuman, viloyat):
#         self.uy=uy
#         self.kocha=kocha
#         self.tuman=tuman
#         self.viloyat=viloyat
#
#     def get_manzil(self):
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#         manzil += f"{self.kocha} ko'chasi, {self.uy} uy"
#         return manzil
#
# talaba_manzi = Manzil(12, 'Olmazor', "Bog'bon", 'Samarqand')
# talaba = Talaba("Valijon", 'Aliyev', "FA112299", 2000, 2345678987, talaba_manzi)
#
# print(talaba.manzil.get_manzil())
# print(talaba.manzil.tuman)





from uuid import uuid4

class Avto:
    __num_avto = 0
    def __init__(self, make, model, rang, yil, narh, km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

# avto1 = Avto("GM","Malibu", "Qora", 2020, 40000, 100000)
#
# print(avto1.get_km())
# print(avto1.get_id())
#
# avto1.add_km(1500)
# print(avto1.get_km())

avto1 = Avto("GM", "Malibu", 'Qora', 2020, 40000)
avto2 = Avto("GM", 'Lacetti', 'Oq', 2020, 20000)
avto3 = Avto("Toyota", "Carolla", "Silver", 2018, 4500)
print(avto1.get_num_avto())