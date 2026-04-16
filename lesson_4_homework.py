# 1 vazifa

tugilgan_sana = '12072011'
with open('pi_million_digits.txt', 'r') as f:
    if tugilgan_sana in f.read():
        print(tugilgan_sana, 'pi-ni ichida bor')
    else:
        print(tugilgan_sana, 'pi-ni ichida yoq')

# 2 vazifa

import pickle

with open('pi_million_digits.txt', 'r') as file:
    pi_text = file.read().strip()

pi_float = float(pi_text)

with open('pi_float.pkl', 'wb') as f:
    pickle.dump(pi_float, f)

# 3 vazifa

filename = 'user_data.txt'

while True:
    data = input("kirgizmoqchi bolgan matnni yozing (chiqib ketish uchun 'exit' deb yozing: ")

    if data.lower() == 'exit':
        break

    with open(filename, 'a') as file:
        file.write(data + '\n')