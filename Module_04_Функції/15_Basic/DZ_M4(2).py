list_1 = ["Приймак", "Кленько", "Шаталов", "Іванов", "Кленько"]

person = input("Введіть ім'я клієнта\n")
num_visit = 0

def client(person):
    count = []
    global num_visit

    for i in range(len(list_1)):
        if list_1[i] == person:
            count.append(i)

    num_visit = len(count)
    print("Кількість візитів:", num_visit)
    [print(i, end=" ") for i in count]


client(person)

if num_visit > 1:
    print("\nЦе постійний клієнт, йому надається знижка 5%")
elif num_visit == 1:
    print("\nЦей клієнт у нас вдруге, йому ще не надано знижку")
else:
    print("\nЦей клієнт у нас вперше, йому не надано знижку")
