
numUser = int(input('Кількість пасажирів?\n'))                  # Вводимо к-ть пасажирів
numStorage = int(input('Кількість камер схову?\n'))             # Вводимо к-ть камер схову( не менше ніж пасажирів)
userInfo = [{} for i in range(numUser)]                         # Створюємо список зі словниками для вводу данних пасажирів (Ім'я, час прийому багажу, час видачі багажу)
storage = [0 + i for i in range(numStorage + 1)]                # Створюємо список з к-тю камер схову
storage = dict.fromkeys(storage)                                # Перетворюємо список у порожній словник, де номер камери схову є ключем
for i in range(len(storage)):                                   # Заповнюємо всі ключі списками де будуть вниситись данні про стан
    storage[i] = ['порожня', '_', [0, 0]]                       # камери схову - (порожня за замовчуванням), ім'я ким зайнята та час видачі
                                                                # багажу(також перетворена у список)
resultStorage = {}                                              # Стаорюємо порожній словник і резервуємо його для кінцевого виводу результату

for i in range(numUser):                                        # Створюємо цикл з к-тю ітерацій що дорівнює к-ті пасажирів
    userInfo[i]['Name'], userInfo[i]['baggage_entrance'], userInfo[i]['baggage_exit'] = input(      # Заповнюємо данні масажирів через input
        'Введіть данні пасажира [Ivanov 09:45 12:25]\n').split(' ')
    userInfo[i]['baggage_entrance'] = userInfo[i]['baggage_entrance'].split(':')                    # Сплітуємо годину здачі багажу по літералу ':'
    userInfo[i]['baggage_entrance'] = [int(j) for j in userInfo[i]['baggage_entrance']]             # Створюємо список з годин та хвилин та перетворюємо у тип 'int'
    userInfo[i]['baggage_exit'] = userInfo[i]['baggage_exit'].split(':')                            # Сплітуємо годину видачі багажу по літералу ':'
    userInfo[i]['baggage_exit'] = [int(j) for j in userInfo[i]['baggage_exit']]                     # Створюємо список з годин та хвилин та перетворюємо у тип 'int'

listKeys = []                                                   # Створюємо порожній список
for i in storage.keys():                                        # Заповнюємо список переліком ключів у словнику з камер схову
    listKeys.append(i)

for i in range(len(userInfo)):                                  # Задаємо цикл з к-ть ітерацій, що = к-ті пасажирів

    for j in listKeys:                                          # Створюємо вкладений цикл, що проходить по всім ключам списку камер схову

        if storage[j][0] == 'порожня':                          # Перевіряємо стан камери схову і задаємо умову роботи при її вільності
            storage[int(j)] = ['зайнята', userInfo[i]['Name'], userInfo[i]['baggage_exit']]         # Вводимо інформацію по камерам схову
            userInfo[i]['luggage_compartment'] = j              # Додаємо інформацію про те, яку камеру схову зайняв вантаж пасажира у блок інформації про пасажирів
            resultStorage[userInfo[i]['Name']] = j              # Додаємо інформацію про те, яку камеру схову зайняв вантаж пасажира у списак, зарезервований для виводу інформації
            if userInfo[i]['Name'] in storage[int(j)]:          # Перевіряємо, щоб данні про зайняття конкретним пасажиром камери схову було введено лише 1 раз
                break

        elif storage[j][0] == 'зайнята':                        # Перевіряємо стан камери схову і задаємо умову роботи при її зайнятості

            if storage[j][2][0] < userInfo[i]['baggage_entrance'][0]:           # Задаємо роботу при умові, що час здачі багажу більше за час його видачі з зайнятої камери схову
                storage[int(j)] = ['зайнята', userInfo[i]['Name'], userInfo[i]['baggage_exit']]     # Задаємо новий стан камери схову
                userInfo[i]['luggage_compartment'] = j          # Додаємо інформацію про те, яку камеру схову зайняв вантаж пасажира у блок інформації про пасажирів
                resultStorage[userInfo[i]['Name']] = j          # Додаємо інформацію про те, яку камеру схову зайняв вантаж пасажира у списак, зарезервований для виводу інформації
                if userInfo[i]['Name'] in storage[int(j)]:      # Перевіряємо, щоб данні про зайняття конкретним пасажиром камери схову було введено лише 1 раз
                    break

            if ((storage[j][2][0] == userInfo[i]['baggage_entrance'][0]) and (storage[j][2][1] <= userInfo[i]['baggage_entrance'][1])):     # Задаємо роботу при умові, що година здачі багажу = годині його видачі, але за хвилинами багаж забрали раніше
                storage[int(j)] = ['зайнята', userInfo[i]['Name'], userInfo[i]['baggage_exit']]     # Задаємо новий стан камери схову
                userInfo[i]['luggage_compartment'] = j          # Додаємо інформацію про те, яку камеру схову зайняв вантаж пасажира у блок інформації про пасажирів
                resultStorage[userInfo[i]['Name']] = j          # Додаємо інформацію про те, яку камеру схову зайняв вантаж пасажира у списак, зарезервований для виводу інформації
                if userInfo[i]['Name'] in storage[int(j)]:      # Перевіряємо, щоб данні про зайняття конкретним пасажиром камери схову було введено лише 1 раз
                    break

            else:                                               # Умова при якій камера схову ще зайнята, а багаж потрібно прийняти (переходимо у іншу камеру)
                continue

for i in resultStorage:                                         # Виводимо інформацію по пасажирам та занятим ними камерам схову
    print(i, resultStorage[i] + 1)

# Введіть данні пасажира
# Ivanov 09:45 12:25
# Введіть данні пасажира
# Petrov 12:00 14:00
# Введіть данні пасажира
# Vasiliev 13:00 16:00
