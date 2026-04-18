# 1 vzifa

import json

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json = json.dumps(data)
print(data_json)

# 2 vazifa

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba = json.loads(talaba_json)
print(f"{talaba['ism']} {talaba['familiya']}")

# 3 vazifa

with open('data.json', 'w') as f:
    json.dump(data, f)

with open('talaba.json', 'w') as f:
    json.dump(talaba, f)

# 4 vazifa

with open('students.json', 'r') as fayl:
    malumot = json.load(fayl)

for talaba in malumot['student']:
    ism = talaba['name']
    familiya = talaba['lastname']
    kurs = talaba['year']
    fakultet = talaba['faculty']

    print(f"{ism} {familiya}, {kurs}-kurs, {fakultet} talabasi")

# 5 vazifa

with open('python.json', 'r') as file:
    data = json.load(file)

pages = data['query']['pages']

for page_id, page in pages.items():
    print("Sarlavha:", page['title'])
    print("\nQisqasi:\n", page['extract'])