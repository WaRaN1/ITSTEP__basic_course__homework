import os.path

    #1

# txt1 = os.path.join("data_base", "Txt1.txt")
# txt2 = os.path.join("data_base", "Txt2.txt")
#
# file1 = open(txt1, "r", encoding = 'utf-8')
# file2 = open(txt2, "r", encoding = 'utf-8')
#
# file_1 = file1.readlines()
# file_2 = file2.readlines()
#
# file1.close()
# file2.close()
#
# [print("У першому файлі немає: ", elem) for elem in file_2 if elem not in file_1]
# [print("У другому файлі немає: ", elem) for elem in file_1 if elem not in file_2]



#___________________________


    #2

# Пробіли також рахую за символи
# Зробив двома варіантами, обидва здались цікавими
# Зчитуємо з файла Txt2.txt
# Дозаписуємо кожен результат у файл Txt_rez.txt

#______

    #2_1 варіант

# def read_file(file):
#     txt2 = os.path.join("data_base", file)
#     file1 = open(txt2, "r", encoding='utf-8')
#     return file1
#
# def close_file(file):
#     read_file(file).close()
#
# def write_file(file, text, rez):
#     path = os.path.join("data_base", file)
#     file_rez = open(path, "a", encoding='utf-8')
#     file_rez.write(text + rez + "\n")
#     file_rez.close()
#
#
# txt_f_s = read_file("Txt2.txt").read()
# write_file("Txt_rez.txt", "К-ть символів: ", str(len(txt_f_s)))
#
#
# txt_f_r = read_file("Txt2.txt").readlines()
# write_file("Txt_rez.txt", "К-ть рядків: ", str(len(txt_f_r)))
#
#
# txt_f_v = read_file("Txt2.txt").read()
# list_v = []
# [list_v.append(elem) for elem in txt_f_v if elem in "аеєиіїоюуя"]
# write_file("Txt_rez.txt", "К-ть голосних: ", str(len(list_v)))
#
#
# txt_f_c = read_file("Txt2.txt").read()
# list_c = []
# [list_c.append(elem) for elem in txt_f_c if elem not in "0123456789аеєиіїоюуя "]
# write_file("Txt_rez.txt", "К-ть приголосних: ", str(len(list_c)))
#
#
# txt_f_n = read_file("Txt2.txt").read()
# list_n = []
# [list_n.append(elem) for elem in txt_f_n if elem in "0123456789"]
# write_file("Txt_rez.txt", "К-ть цифр: ", str(len(list_n)))
#
#
# close_file("Txt_rez.txt")


#______


# #2_2 варіант
#
#
#
# def read_file(file):
#     txt2 = os.path.join("data_base", file)
#     file1 = open(txt2, "r", encoding='utf-8')
#     return file1
#
# def close_file(file):
#     read_file(file).close()
#
# def write_file(file, text, rez):
#     path = os.path.join("data_base", file)
#     file_rez = open(path, "a", encoding='utf-8')
#     file_rez.write(text + rez + "\n")
#     file_rez.close()
#
#
# list_v, list_c, list_n = [], [], []
# txt_f_n = read_file("Txt2.txt").read()
#
#
# write_file("Txt_rez.txt", "К-ть символів: ", str(len(txt_f_n)))
#
# txt_f_r = read_file("Txt2.txt").readlines()
# write_file("Txt_rez.txt", "К-ть рядків: ", str(len(txt_f_r)))
#
# for i in txt_f_n:
#     if i in "аеєиіїоюуя":
#         list_v.append(i)
#
#     elif i not in "0123456789аеєиіїоюуя ":
#         list_c.append(i)
#
#     elif i in "0123456789":
#         list_n.append(i)
#
#
# write_file("Txt_rez.txt", "К-ть голосних: ", str(len(list_v)))
# write_file("Txt_rez.txt", "К-ть приголосних: ", str(len(list_c)))
# write_file("Txt_rez.txt", "К-ть цифр: ", str(len(list_n)))
#
# close_file("Txt_rez.txt")

