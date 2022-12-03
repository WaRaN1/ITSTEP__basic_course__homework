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


def kalkulator(message):
    sp = ""
    for i in message.text:
        if i != " ":
            sp += i
    lst_zx = ["+", "-", "*", "/"]
    rez = []
    zn = []
    for el in sp:
        if el in lst_zx:
            rez = sp.split(el)
            zn.append(el)
    if zn[0] == "+":
        rez_fn = int(rez[0]) + int(rez[1])
        ivan.send_message(message.chat.id, f"{message.text} = {rez_fn}")
    if zn[0] == "-":
        rez_fn = int(rez[0]) - int(rez[1])
        ivan.send_message(message.chat.id, f"{message.text} = {rez_fn}")
    if zn[0] == "/":
        rez_fn = int(rez[0]) / int(rez[1])
        ivan.send_message(message.chat.id, f"{message.text} = {rez_fn}")
    if zn[0] == "*":
        rez_fn = int(rez[0]) * int(rez[1])
        ivan.send_message(message.chat.id, f"{message.text} = {rez_fn}")


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
ivan.polling(none_stop=True, interval=0)
