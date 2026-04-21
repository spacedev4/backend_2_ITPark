import datetime as dt
import re

# 1 vazifa
bugun = dt.date.today()
for i in range(10):
    sana = bugun + dt.timedelta(days=i * 14)
    print(f"{i + 1}-sana: {sana.strftime('%d-%m-%Y')}")

# 2 vazifa
qurbon_hayit = dt.date(2026, 5, 27)
farq = qurbon_hayit - bugun
print(f"Qurbon hayitga {farq.days} kun qoldi")


# 3 vazifa
def yoshni_hisobla(yil, oy, kun):
    t_sana = dt.date(yil, oy, kun)
    hozir = dt.date.today()
    farq = hozir - t_sana

    yillar = farq.days // 365
    oylar = (farq.days % 365) // 30
    kunlar = (farq.days % 365) % 30
    return f"{yillar} yil, {oylar} oy va {kunlar} kun"


print(yoshni_hisobla(2011, 7, 12))

# 4 vazifa
andoza_tel = r"^\+998\d{9}$"
tel = input("Telefon raqamingizni kiriting: ")
if re.match(andoza_tel, tel):
    print("Togri")
else:
    print("Xato format")

# 5 vazifa
matn = "Bizning saytlar: https://google.com va http://kun.uz"
andoza_link = r"https?://[^\s]+"
linklar = re.findall(andoza_link, matn)
print(f"Topilgan linklar: {linklar}")