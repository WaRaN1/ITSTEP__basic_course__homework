
    #1

# def product(*lst):
#     rezult = 1                                    #Створюємо змінну для зберігання добутку елементів списку
#     for element in lst:                           #Проходимо по елементам списку
#         rezult *= element                         #Перемножуємо всі елементи списку
#     return rezult                                 #Повертаємо результат

# print(product(2, 4, 6))


    #2

# def min_number(*lst):
#     return  min(lst)
#
# print(min_number(21, 4, 16))


    #3

# from sympy import *
#
# def number_n(*num):
#     num_simple = []                                               #Створюємо новий список, поки що порожній
#     [num_simple.append(elem) for elem in num if isprime(elem)]    #Перевіряємо заданий список чисел на прості числа та додаємо їх до нового
#     return len(num_simple)                                        #Повертаємо довжину нового списка , що = к-ті простих чисел
#
# print(number_n(2, 4, 5, 9))


    #4
# У завданні не вказано що список передається як параметр, тому вважаю, що він заданий завчасно
# old_lst = [2, 4, 65, 4, 32, 12, 4]                                #Задаємо початковий список
#
# def new_list(lst, number):
#     new_lst = []                                                  #Створюємо новий список, поки що порожній
#     [new_lst.append(elem) for elem in lst if elem != number]      #Заповнюємо новий список усіма елементами старого, окрім заданого числа
#     return len(lst) - len(new_lst)                                #Повертаємо к-ть видалених елементів, що як раз і дорівнюють різниці довжин списків
#
# print(new_list(old_lst, 4))                                       #Виводимо функцію у консоль


    #5

# def new_lst(lst_1, lst_2):
#     lst_3 = lst_1 + lst_2
#     return lst_3
#
# print(new_lst([1,2], [3,4]))


    #6

# def new_lst(lst, num):
#     n_lst = []                                              #Створюємо новий список, поки що порожній
#     [n_lst.append(elem**num) for elem in lst]               #Перебираємо всі елементи старого списка, беремо у заданий степінь та додаємо результат до нового списку
#     return n_lst                                            #Повертаємо новий список
#
# print(new_lst([2, 4, 8], 2))