        #1

# txt = 'Python’s standard library is very extensive'                       #Записуємо у перемінну текст
#
# def count_vowels(txt):
#     print('кількості голосних у рядку -', len([letter for letter in txt if letter.lower() in 'aeiouy']))    #Створюємо список
                                                                            #в якому проходимось по символам тексту, одночасно переводячи
# count_vowels(txt)                                                         #їх у нижній регістр та записуємо співпадіння його з 'aeiouy'
                                                                            #Виводимо довжину цього списка

        #2

# text = '"Don’t let the noise of others’ opinions drown out your own inner voice." Steve Jobs'     #Записуємо у перемінну текст
#
# def textFormat(text):
#     text = text.split('."')                                               #Розбиваємо текст окремо на цитату та автора та перезаписуємо змінну
#     print("Цитата: {}".format(text[0]))                                   #Виводимо запис за допомогою format
#     print("Автор: {}".format(text[1]))
#
# textFormat(text)


        #3

# ticket = input("Enter num\n")                                             #Вводимо число з консолі
#
# def happi(ticket):
#     print(any(sum(map(int, ticket[0:3])) == sum(map(int, ticket[-3:])) for _ in ticket))      #За допомогою ф-ї 'any' виводимо 'true' якщо умова
                                                                            #задовальняється (беремо три перші індекси строчного представлення числа,
# happi(ticket)                                                             #переводимо його у число, розбиваємо на окремі числа, суммуємо їх та
                                                                            #та порівнюємо з тим же, аде по останнім трьом числам). Якщо ні, то false
