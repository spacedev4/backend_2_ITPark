class Avto:
    def __init__(self, model, rang, korobka, narh, kilometr=0):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometr = kilometr

    def get_info(self):
        return f"{self.rang} {self.model}, {self.korobka} korobka, narhi: {self.narh}$, yurgan masofasi: {self.kilometr} km"

    def update_km(self, yangi_km):
        self.kilometr = yangi_km

class Avtosalon:
    def __init__(self, salon_nomi, manzili):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.avtolar = []

    def add_avto(self, avto):
        self.avtolar.append(avto)

    def get_avtolar_info(self):
        return [avto.get_info() for avto in self.avtolar]

avto1 = Avto("Nexia 3", "Oq", "Mexanika", 9000)
avto2 = Avto("Malibu 2", "Qora", "Avtomat", 28000, 5000)

salon = Avtosalon("GM Uzbekistan", "Toshkent sh.")
salon.add_avto(avto1)
salon.add_avto(avto2)

print(f"{salon.salon_nomi} dagi avtomobillar:")
for info in salon.get_avtolar_info():
    print(info)

print("\nAvto klassining xususiyatlari va metodlari")
print(dir(avto1))

print("\nAvto obyektining xususiyatlari")
print(avto1.__dict__)

print("\nString (str) klassining metodlari:")
print(dir(str))