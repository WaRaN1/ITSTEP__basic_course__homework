list_2 = input("Enter text\n").split()
list_1 = input("ВВедіть перелік зарезервованих слів\n").split()
list_4 = []
for i in list_2:
    if i not in list_1:
        list_4 += [i]
    else:
        list_4 += [i.upper()]
myString = ' '.join(list_4)
print(myString)


