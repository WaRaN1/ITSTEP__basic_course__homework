# 1

# k1 = (1, 3, 12, 24)         # задаємо перший кортедж
# k2 = (9, 3, 24, 12)         # задаємо другий кортедж
# k3 = (3, 12, 9, 60)         # задаємо третій кортедж
# k1_3 = []                   # створюємо список для загальних елементів кортеджів
# for i in k1:                # проходимо по елементах першого кортеджу
#     if i in k2 and i in k3: # порівнюємо елементи  першого кортеджу з другим та третім і якщо є співпадіння то йдемо далі
#         k1_3.append(i)      # додаємо едементи що співпадають до нового списка
# print(k1_3)                 # виводимо список зі спільними єлементами


# 2

# k1 = (1, 3, 12, 24)         # задаємо перший кортедж
# k2 = (9, 3, 24, 12)         # задаємо другий кортедж
# k3 = (3, 12, 9, 60)         # задаємо третій кортедж
# k1_3 = []                   # створюємо список для унікальних елементів кортеджів
# for i in k1:                # проходимо по елементах першого кортеджу
#     if i not in k2 and i not in k3 and i not in k1_3:           # порівнюємо елементи  першого кортеджу з другим, третім та новим списком і якщо немає співпадінь то йдемо далі
#         k1_3.append(i)                                          # додаємо едементи що не співпадають до нового списка
# for i in k2:                                                    # проходимо по елементах другого кортеджу
#     if i not in k1 and i not in k3 and i not in k1_3:           # порівнюємо елементи  другого кортеджу з першим, третім та новим списком і якщо немає співпадінь то йдемо далі
#         k1_3.append(i)                                          # додаємо едементи що не співпадають до нового списка
# for i in k3:                                                    # проходимо по елементах третього кортеджу
#     if i not in k2 and i not in k1 and i not in k1_3:           # порівнюємо елементи  третього кортеджу з другим, першим та новим списком і якщо немає співпадінь то йдемо далі
#         k1_3.append(i)                                          # додаємо едементи що не співпадають до нового списка
# print(k1_3)                                                     # виводимо список з унікальними елементами


#3

# k1 = (1, 3, 12, 12)            # задаємо перший кортедж
# k2 = (9, 3, 24, 12)            # задаємо другий кортедж
# k3 = (3, 3, 9, 12)             # задаємо третій кортедж
# k1_3 = []                      # створюємо список для загальних елементів на тих же позиціях всіх кортеджів
# for i in range(len(k1)):       # проходимо цикл по індексам найкоротшого циклу
#     if k1[i] == k2[i] == k3[i]:     # проводимо порівняння елементів по індексам
#         k1_3.append(k1[i])     # додаємо до нового списку елементи, які пройшли перевірку на співпадіння
# print(k1_3)                    # виводимо новий список