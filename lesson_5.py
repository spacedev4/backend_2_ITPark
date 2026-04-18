# import json
#
# x = 10
# x_json = json.dumps(x)
# print(x_json)
# print(type(x_json))
#
# ism = 'jonibek'
# ism_json = json.dumps(ism)
# print(ism_json)
# print(type(ism_json))
#
# sonlar = [12, 45, 23, 67]
# sonlar_json = json.dumps(sonlar)
# print(sonlar_json)
# print(type(sonlar_json))
#
# import json
#
# bemor = {
#     'ism':'Alijon Valiyev',
#     'yosh':30,
#     "oila":True,
#     'farzandlar': ("Ahmad", 'Bonu'),
#     'allergiya':None,
#     'dorilar': [
#         {'nomi': "Analgin", 'miqdori': 0.5},
#         {'nomi': "Panadol", 'miqdori': 1.2}
#     ]
# }
#
# bemor_json = json.dumps(bemor, indent=2)
# print(bemor_json)
#
# with open('bemor.json', 'w') as f:
#     json.dump(bemor, f)
#
# sonlar = [12, 45, 23, 67]
# sonlar_json = json.dumps(sonlar)
#
# sonlar = json.loads(sonlar_json)
# bemor = json.loads(bemor_json)
# print(bemor)
# print(type(bemor))
# print(sonlar)
# print(type(sonlar))
#
# import json
#
# filename = 'bemor.json'
# with open(filename) as f:
#     bemor = json.load(f)
#
# print(bemor)
# print(type(bemor))
#
#
# data = {
#     "address_components": [
#         {
#             "long_name": "Tinchlik Street",
#             "short_name": "Tinchlik Street",
#             "types": [
#                 "political",
#                 "sublocality",
#                 "sublocality_level_1"
#             ]
#         },
#         {
#             "long_name": "Khorezm",
#             "short_name": "Khorezm",
#             "types": [
#                 "locality",
#                 "political"
#             ]
#         },
#         {
#             "long_name": "Khorezm Region",
#             "short_name": "Khorezm Region",
#             "types": [
#                 "administrative_area_level_1",
#                 "political"
#             ]
#         },
#         {
#             "long_name": "Uzbekistan",
#             "short_name": "UZ",
#             "types": [
#                 "country",
#                 "political"
#             ]
#         }
#     ],
#     "formatted_address": "Tinchlik Street, Khorezm, Urgench",
#     "geometry": {
#         "bounds": {
#             "northeast": {
#                 "lat": 41.3954567,
#                 "lng": 69.269883
#             },
#             "southwest": {
#                 "lat": 41.3249733,
#                 "lng": 69.16497629999999
#             }
#         },
#         "location": {
#             "lat": 41.55860870120288,
#             "lng": 60.6218083747805
#         },
#         "location_type": "APPROXIMATE",
#         "viewport": {
#             "northeast": {
#                 "lat": 41.3954567,
#                 "lng": 69.269883
#             },
#             "southwest": {
#                 "lat": 41.3249733,
#                 "lng": 69.16497629999999
#             }
#         }
#     },
#     "place_id": "ChIJ195FnkeMrjgR3nkapKKdk7A",
#     "types": [
#         "political",
#         "sublocality",
#         "sublocality_level_1"
#     ]
# }
#
# kenglik = data['geometry']['location']['lat']
# uzunlik = data['geometry']['location']['lng']
#
# print(kenglik, uzunlik)
#
# yosh = input('Yoshingizni kiriting')
# try:
#     yosh = int(yosh)
# except:
#     print('Butun son kiritmadingiz')
# else:
#     print(f"Siz {2026-yosh} yilda tug'ilgansiz")
#
# x,y=5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print('0 ga bolib bolmaydi')
#
# user = {"username":"jonibekdev",
#         'status':'admin',
#         'email':'jonibekuralov5152@gmail.com',
#         'phone':'998937564455'}
#
# key='tel'
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     print("Bunday kalit mavjud emas")
#
#
# filename = 'data.txt'
# try:
#
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print("Bunday fayl mavjudd emas")

n = input("Butun son kiriting: ")
try:
    n = int(n)
    x=20/n
except ValueError:
    print("Butun son kiritmadingiz")
except ZeroDivisionError:
    print("0 ga bo'lib bo'lmaydi")
else:
    print(f"x={x}")

while True:
    yosh = input("Yoshingizni kiriting; ")
    if yosh.isdigit():
        yosh = int(yosh)
        break

print(f"Siz {2026-yosh} yilda tug'ilgansiz")