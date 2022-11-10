import os.path

# Підрахувати та вивесли кількість слів у кожному рядку

path1 = os.path.join("data_base", "File1.txt")
path2 = os.path.join("data_base", "File2.txt")
path_1 = open(path1, "r")
path_2 = open(path2, "w")

data_1 = path_1.read().split("\n")

for line in data_1:
    word = line.split(" ")
    path_2.write(f'{line} ({len(word)}) \n')

path_1.close()
path_2.close()