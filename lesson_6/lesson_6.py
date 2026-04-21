# import datetime as dt
#
# hozir = dt.datetime.now()
# print(hozir)
#
# print(hozir.date())
#
# print(hozir.time())
#
# print(hozir.hour)
#
# print(hozir.minute)
#
# print(hozir.second)
#
#
# bugun = dt.datetime.today()
# print(f"Bugungi sana: {bugun}")
#
# ertaga = dt.date(2026, 4, 19)
#
# print(f"Ertangi sana: {ertaga}")
#
# vaqtHozir = hozir.time()
# print(f"Hozir soat: {vaqtHozir}")
#
# vaqtKeyin = dt.time(23,45,80)
# print(vaqtKeyin)
#
#
# bugun = dt.date.today()
# birthday = dt.date(2026, 7, 12)
# farq = birthday-bugun
# print(farq)
# print(f"Tug'ilgan kuingizgacha {farq.days} kun koldi")
#
# vaqt = hozir.strftime("%H:%M:%S")
# print(f"Hozirgi vaqt: {vaqt}")
#
# sana = hozir.strftime("%d-%m-%Y")
# print(f'Bugunki sana: {sana}')
#
# sana_vaqt = hozir.strftime("%d/%m/%y, %h:%m")
#
# import re
#
# word1 = "темир"
# word2 = "томир"
# word3 = "тулпор"
#
# andoza = "^т...р"
#
# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))
#
# from uzwords import words
# andoza = "^т...р$"
#
# matches = []
# for word in words:
#     if re.match(andoza, word):
#         matches.append(word)
#
# print(matches)
#
# import re
# matn = "bu matnda mail pochtalari bor bbazarbayev127@gmail.com bazarbayev127@gmail.com"
#
# andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# email = re.findall(andoza, matn)
# print(email)

import re

andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg = "Yangi parol kiriting"
msg += '(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf'
msg += "1 ta son va 1 ta maxsus belgi bo'lishi kerak"

while True:
    password = input(msg)
    if re.match(andoza, password):
        print("Maxfiy so'z kabul kilindi")
        break
    else:
        print(f"Maxfiy so'z talabga javob bermadi")