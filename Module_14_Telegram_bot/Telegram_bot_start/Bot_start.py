import telebot
import random
import os.path

config = {
    "name": "Python_waran_bot",
    "token": "5737862312:AAEjHoaa-Gzxr3JbJx6TzRzBu32Q3NbbppY"
}
ivan = telebot.TeleBot(config["token"])

# @ivan.message_handler(content_types=["text"])
# def get_text(message):
#     if message.text == "Hello" or message.text == "😄":
#         ivan.send_message(message.chat.id, "Hello user")
#
# ivan.polling(none_stop=True, interval=0)


# --------------------------------------------------------------------------------------------------------------------


nameUser = ""


@ivan.message_handler(content_types=["text"])
def get_text(message):
    if message.text == "Hello":
        ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Hello"), get_text_1)
    elif message.text.lower() == "магічний шар":
        ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Задайте питання"), magic_bol)
    elif message.text.lower() == "перевірка на парність":
        ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Введіть число для перевірки"), get_text_isd)
    elif message.text.lower() == "перевірка на поліндром":
        ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Введіть значення для перевірки"), polindrom)
    elif message.text.lower() == "калькулятор":
        ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Введіть дію"), kalkulator)
    elif message.text.lower() == "щасливий білет":
        ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Введіть номер білету"), bil)
    elif message.text.lower() == "реєстрація":
        ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Введіть ваше ім'я та пароль через '/'"), registration)
    elif message.text.lower() == "авторизація":
        ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Введіть ваше ім'я та пароль через '/' для вхлду у систему чатбота"), authorization)


def magic_bol(message):
    answers = ["Не дуже", "Звісно", "Ні", "Мрій", "100%", "Віримо в краще"]
    ivan.send_message(message.chat.id, random.choice(answers))


def get_text_1(message):
    if message == "Hello":
        if nameUser:
            ivan.send_message(message.chat.id, f"Hello, {nameUser}")
        else:
            name = ivan.send_message(message.chat.id, "What is your name?")
            ivan.register_message_handler(name, meet)


def get_text_isd(message):                                      # Перевірка числа на парність
    if message.text.isdigit():
        if int(message.text) % 2 == 0:
            ivan.send_message(message.chat.id, f"{message.text} це парне число")
        else:
            ivan.send_message(message.chat.id, f"{message.text} це непарне число")
    else:
        ivan.send_message(message.chat.id, "Введіть цифрове значення")


def polindrom(message):                                         # Перевірка числа на поліндром
    if message.text == message.text[::-1]:
        ivan.send_message(message.chat.id, f"{message.text} це значення є поліндромом")
    else:
        ivan.send_message(message.chat.id, f"{message.text} це значення не є поліндромом")


def meet(message):
    global nameUser
    nameUser = message.text


def bil(message):
    one = message.text[0:int(len(message.text) / 2)]
    two = message.text[int(len(message.text) / 2)::]
    one_rez, two_rez = 0, 0
    for i in range(len(one)):
        one_rez += int(one[i])
        two_rez += int(two[i])
    if one_rez == two_rez:
        ivan.send_message(message.chat.id, f"{message.text} щасливий білет")
    else:
        ivan.send_message(message.chat.id, f"{message.text} не щасливий білет")


def registration(message):                                  # Реєстрація у системі
    path = os.path.join("data_base", "T_b.txt")
    file = open(path, "r", encoding='utf-8')
    all_users = file.read().split("\n")
    file.close()
    rez = message.text.split("/")
    var_var = 0
    for el in all_users:                                    # Перевірка чи такий користувач вже зареєстрований
        var = el.split("/")
        if var[0] == rez[0]:
            var_var = 1
            break
    if var_var == 0:
        file = open(path, "a", encoding='utf-8')
        file.write(f"{message.text}\n")
        file.close()
        ivan.send_message(message.chat.id, f"Вітаю {rez[0]}, вас успішно зареєстровано у системі ")
    else:
        ivan.send_message(message.chat.id, f"Щось пішло не так. Користувач {rez[0]} вже зареєстрований у системі")


def authorization(message):                                     # Авторизація у системі
    path = os.path.join("data_base", "T_b.txt")
    file = open(path, "r", encoding='utf-8')
    log_pass = file.read().split("\n")
    rez = message.text.split("/")
    if message.text in log_pass:
        ivan.send_message(message.chat.id, f"{rez[0]}, вітаємо у системі")
    else:
        ivan.send_message(message.chat.id, f"Невірно введені логін або пароль.")




def kalkulator(message):
    try:
        num_lst, znak_lst, var = [], [], ""  # Списки для чисел та дій
        if message.text[0].isdigit():
            var_one_znak = "+"
        else:
            message.text = message.text[1::]
            var_one_znak = "-"

        def diya(el, ind, var_znak):
            znak_lst.remove(el)
            num_lst.pop(ind)
            num_lst.pop(ind)
            num_lst.insert(ind, var_znak)

        for el in message.text:
            if el == " ":  # Видаляємо пробіли, якщо вони є
                continue
            elif el.isdigit():
                var = var + el  # Перевірка на строкове представлення числа та формування чиссел більше 9
            else:
                num_lst.append(int(var))  # Заповнення списка чисел
                var = ""
                znak_lst.append(el)  # Заповнення списка дій
        num_lst.append(int(var))  # Внесення у список останнього числа виразу

        if var_one_znak == "-":
            var_one_znak = -int(num_lst[0])
            num_lst.pop(0)
            num_lst.insert(0, var_one_znak)

        num_zn = len(znak_lst)
        count = 0
        while count <= num_zn:
            for el in znak_lst:
                count += 1
                if el == "*":
                    for ind in range(len(znak_lst)):  # Проходимось по довжині списка дій
                        if znak_lst[ind] == "*":  # Подальша умова виконання - вираз множення у списку дій
                            var_znak = num_lst[ind] * num_lst[
                                ind + 1]  # Множимо цифри у списку чисел які відповідають індексу знака множення у списку дій та (індексу + 1)
                            diya(el, ind, var_znak)  # Вносимо у список чисел результат виразу видалених значень
                            break
                elif el == "/":
                    for ind in range(len(znak_lst)):
                        if znak_lst[ind] == "/":
                            var_znak = num_lst[ind] / num_lst[ind + 1]
                            diya(el, ind, var_znak)
                            count += 1

        while "+" in znak_lst or "-" in znak_lst:
            for ind in range(num_zn):
                if znak_lst[ind] == "+":
                    el, var_znak = "+", num_lst[ind] + num_lst[ind + 1]
                    diya(el, ind, var_znak)
                    break
                elif znak_lst[ind] == "-":
                    el, var_znak = "-", num_lst[ind] - num_lst[ind + 1]
                    diya(el, ind, var_znak)
                    break
        print(message.text, "=", num_lst[0])
        ivan.send_message(message.chat.id, f"{message.text} = {num_lst[0]}")
    except:
        ivan.send_message(message.chat.id, "Перевірте правильність введеня")

ivan.polling(none_stop=True, interval=0)
