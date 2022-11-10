import os.path


    #3

# Зчитуємо з Txt2.txt
# Записуємо в Test_3.txt

# path = os.path.join("data_base", "Txt2.txt")
# path2 = os.path.join("data_base", "Test_3.txt")
#
# file_1 = open(path, "r", encoding='utf-8')
# file_2 = open(path2, "w", encoding='utf-8')
#
# old_file = file_1.readlines()
# new_file = old_file[0:-1]
# [file_2.write(elem) for elem in new_file]
#
#
# file_1.close()
# file_2.close()


#----------------------

    #4
# Зчитуємо з  файла Txt2.txt

# path = os.path.join("data_base", "Txt2.txt")
# data = open(path, "r", encoding='utf-8')
#
# data_1 = data.readlines()
#
# print("Найдовший рядок у файлі: ", max(data_1, key=len))
#
#
# data.close()


#----------------------

    #5
# Зчитуємо з  файла Txt2.txt

# path = os.path.join("data_base", "Txt2.txt")
# path1 = open(path, "r", encoding='utf-8')
# file = path1.read()
#
# count_n = file.count("файл")
#
# print(count_n)
#
# path1.close()


#----------------------

    #6

# Зчитуємо з  файла Txt2.txt

# path = os.path.join("data_base", "Txt2.txt")
# path1 = open(path, "r", encoding='utf-8')
#
# n_file = path1.read()
# n_file = n_file.replace(input("Яке слово змінити\n"), input("На яке слово замінити?\n"))
#
# path1.close()
#
# path = os.path.join("data_base", "Txt2.txt")
# path2 = open(path, "w", encoding='utf-8')
#
# path2.write(n_file)
#
# path2.close()