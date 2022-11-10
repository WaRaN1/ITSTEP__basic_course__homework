import os.path
from easygui import *

    #1

# Маємо текстовий файл. Створіть новий файл, прибравши з нього всі неприйнятні слова. Список неприйнятних
# слів міститься в іншому файлі


# path1 = os.path.join("data_base", "Txt1.txt")
# path2 = os.path.join("data_base", "Txt2.txt")
# path3 = os.path.join("data_base", "Txt3.txt")
#
# file1 = open(path1, "r")
# file_1 = file1.read().split("\n")
# file2 = open(path2, "r")
# file_2 = file2.read().split()
# file3 = open(path3, "w")
#
# rez = ""
#
# new_file_2 = []
# for element in file_2:               # Щоб змінений текст зберіг розділові знаки ми їх не видаляємо а створюємо варіації у списку виключень
#     new_file_2.append(element)
#     new_file_2.append(element + ",")
#     new_file_2.append(element + ".")
#
#
# for line in file_1:
#     for element in line.split():
#         if element not in new_file_2:
#             rez = rez + element + " "
#     rez = rez.strip()                 # Так як елементи в строчці записуються з пробіломи, а в кінці вони нам не завжди потрібні, то ми їх видаляємо
#     rez = rez + "\n"
#
#
# file3.write(rez)
#
# file1.close()
# file2.close()
# file3.close()

# Whether you're new programming an experienced or developer
# it's easy learn and Python Whether you're new to programming
# an experienced developer it's easy learn and use Python


#______________________________________



    #2


# Напишіть програму транслітерації з російської на
# англійську, та навпаки. Візьміть дані для транслітерації
# з одного файлу і запишіть їх до іншого. Мовну пару встановлює користувач у меню.


# Я так зрозумів, що у нас є данні для транслітерації (текст), який ми переносимо до іншого файлу та послівно питаємо у
# користувача переклад, який і записуємо у файл


# path1 = os.path.join("data_base", "en-ua-old.txt")
# path2 = os.path.join("data_base", "en-ua-new.txt")
#
# path1 = open(path1, "r", encoding='utf-8')
# file2 = open(path2, "a", encoding='utf-8')
#
# while True:
#     interface = buttonbox("Choise action: ", "Dictionary", ["Translation", "EXIT"])
#     if interface == "Translation":
#         file1 = path1.read().split("\n")
#         for line in file1:
#             for element in line.split():
#                 words = multenterbox(element, "Dictionary", ["Tr"])
#                 file2.write(words[0] + " ")
#             file2.write("\n")
#         file2.close()
#     else:
#         break
#
# path1.close()



#-------------------------


    #3


# Користувач вводить з клавіатури назви файлів, доки
# він не введе слово «quit». Після завершення введення
# програма має об’єднати вміст усіх внесених назв файлів
# в один.


# Записуємо у файл Txt_rezult.txt
# Беремо данні з файлів Txt1.txt, Txt2.txt, Txt3.txt

path3 = os.path.join("data_base", "Txt_rezult.txt")
path3 = open(path3, "a")

rezult = []

while True:
    interface = buttonbox("Choise action: ", "Dictionary", ["ADD", "EXIT"])
    if interface == "ADD":
        data = enterbox("Enter your data: ", "Data")
        rezult.append(data)
        while data != "quit":
            data = enterbox("Enter your data: ", "Data")
            if data != "quit":
                rezult.append(data)

    else:
        break

for element in rezult:
    path = os.path.join("data_base", element)
    path = open(path, "r")
    path1 = path.read()
    path3.write(path1 + "\n")
    path.close()

path3.close()
