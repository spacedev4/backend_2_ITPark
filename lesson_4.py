# with open('pi.txt') as fayl:
#     pi = fayl.read()
#
# print(pi)
# print(type(pi))
#
# fayl = open("data/pi.txt")
# pi = fayl.read()
#
# pi = pi.rstrip()
# pi = pi.replace('\n', '')
# pi = float(pi)
#
# print(pi)
# print(type(pi))
#
# fayl.close()
# filename = 'data/students.txt'
# # with open(filename) as file:
# #     for line in file:
# #         print(f"Salom, {line}")
#
# with open(filename) as file:
#     students = file.readlines()
#
# students = [student.rstrip() for student in students]
# print(students)
#
# filenomi = 'teachers.txt'
# with open(filenomi, 'w') as fayl:
#     fayl.write('Bazarbayev Baxtiyor')
#
# faylnomi = 'new_file.txt'
# ism = 'Olimjon Hasanov '
# tyil = 2004
# with open(faylnomi, 'w') as fayl:
#     fayl.write(ism+'\n')
#     fayl.write(str(tyil)+'\n')
#
# with open(faylnomi, 'a') as fayl:
#     fayl.write('Alijon Valiyev\n')
#     fayl.write(str('2000'))

import pickle

talaba1 = {'ism':'hasan', 'familiya':'husanov', "tyil":2003, 'kurs':2}
talaba2 = {'ism':'alijon', 'familiya':'valiyev', "tyil":2004, 'kurs':1}

with open('info', 'wb') as file:
    pickle.dump(talaba1, file)
    pickle.dump(talaba2, file)

with open('info', 'rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)

print(talaba1)
print(talaba2)