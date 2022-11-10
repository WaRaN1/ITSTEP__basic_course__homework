    #1

# def sum_elem(*lst):
#     return sum(lst)
#
# print(sum_elem(2, 4, 9))


    #2

# def sum_elem(*lst):
#     return max(lst)
#
# print(sum_elem(2, 15, 9))


    #3
# def element(*lst):
#     double_numbers = []                                                           #Створюємо список для парних чисел
#     [double_numbers.append(elem) for elem in lst if elem % 2 == 0]                #Заповнюємо список парних чисел
#     unpaired_numbers = []                                                         #Створюємо список для непарних чисел
#     [unpaired_numbers.append(elem) for elem in lst if elem % 2 != 0]              #Заповнюємо список непарних чисел
#     positive_numbers = []                                                         #Створюємо список для додатніх чисел
#     [positive_numbers.append(elem) for elem in lst if elem > 0]                   #Заповнюємо список додатніх чисел
#     negative_numbers = []                                                         #Створюємо список для від'ємних чисел
#     [negative_numbers.append(elem) for elem in lst if elem < 0]                   #Заповнюємо список від'ємних чисел
#     return len(double_numbers), len(unpaired_numbers), len(positive_numbers), len(negative_numbers)   #Повертаємо к-ть заданих чисел
#
# print(element(2, 4, -3, -9, 12))


    #4
#На думку спадає 2 вирішення цієї задачки, тому пишу обидва

# def output_list(*lst):
#     return lst
# print(output_list(2, 4, 6 ,8, 11))
#
#
#     #4
#
# def output_list(*lst):
#     [print(elem, end=" ") for elem in lst]
# output_list(2, 4, 6 ,8, 11)


    #5
# lst = [2, 4, 6 ,8, 11]
#
# def number_search(lst, num):
#     return any([num in lst])                  #Повертаємо наявність числа у списку за допомогою функції any
#
#
# print(number_search(lst, 4))


    #6

# import math
#
# old_lst = [2, 4, 6, 8, 11]
# def lst_f(lst):
#     new_lst = []                                                #Створюємо новий список для факторіалів
#     [new_lst.append(math.factorial(elem)) for elem in lst]      #Перебираємо поелементно початковий список, беремо факторіал
#                                                                 # елементів та додаємо їх у новий список
#     return new_lst                                              #Повертаємо новий список
#
#
# print(lst_f(old_lst))
