
    #1

# def list_format():
#     print(" " * 7, '“Don’t compare yourself with anyone in this world…\n'," " * 8, 'if you do so, you are insulting yourself."\n', " " * 48, 'Bill Gates')
#
# list_format()


    #2

# def num_double():
#     num_d = []
#     [num_d.append(x) for x in range(int(input("num_1\n")) + 1, int(input('num_2\n'))) if not x % 2]
#     return num_d
# print(num_double())


    #3

# def square(l, s, s_b):
#     if s_b == False:
#         s = " "
#     s = s + "  "
#     x = [[s] * l for i in range(l)]
#     for i in range(l):
#         print(l * s)
# square(5, "*", True)


    #4

# def num_min(num_1, num_2, num_3, num_4, num_5):
#     num_min = min(num_1, num_2, num_3, num_4, num_5)
#     return num_min
# print(num_min(2, 4, 6, 5, 1))


    #5

# def dob(a, b):
#     rez = 1
#     if a < b:
#         for elem in range(a, b + 1):
#             rez *= elem
#         return rez
#     if a > b:
#         for elem in range(b, a + 1):
#             rez *= elem
#         return rez
#
# print(dob(2, 4))


    #6

# def num_number(num):
#     return len(str(num))
#
# print(num_number(12345))


    #7

# def poli(number):
#     number = str(number)
#     return any([number == number[::-1]])
#
# print(poli(123321))
