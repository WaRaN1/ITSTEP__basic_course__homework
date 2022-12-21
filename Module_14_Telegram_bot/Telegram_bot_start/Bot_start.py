import time
from pathlib import Path
import telebot
import random
import os.path
from telebot import types
import uuid
import base64

nameUser = ""
permission = False

path = os.path.join("data_base", "T_b.txt")

config = {
    "name": "Python_waran_bot",
    "token": "5737862312:AAEjHoaa-Gzxr3JbJx6TzRzBu32Q3NbbppY"
}


free_access = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_registration = types.InlineKeyboardButton("реєстрація")
button_authorization = types.InlineKeyboardButton("авторизація")
free_access.add(button_registration, button_authorization)


keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_conv_image = types.InlineKeyboardButton("конвертувати зображення")
button_magic_bol = types.InlineKeyboardButton("магічний шар")
button_get_text_isd = types.InlineKeyboardButton("перевірка на парність")
button_polindrom = types.InlineKeyboardButton("перевірка на поліндром")
button_kalkulator = types.InlineKeyboardButton("калькулятор")
button_statistics = types.InlineKeyboardButton("статистика")
keyboard.add(button_magic_bol, button_get_text_isd, button_polindrom, button_kalkulator, button_statistics, button_conv_image)


statistics_batt = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_number_of_words = types.InlineKeyboardButton("кількість слів")
button_number_of_characters = types.InlineKeyboardButton("кількість символів")
button_number_of_digits = types.InlineKeyboardButton("кількість цифр")
button_number_of_voice_letters = types.InlineKeyboardButton("кількість голосних літер")
button_number_of_vowels_letters = types.InlineKeyboardButton("кількість приголосних літер")
button_the_number_of_punctuation_marks = types.InlineKeyboardButton("кількість знаків пунктуації")
button_all = types.InlineKeyboardButton("Всю інформацію файлом")
button_exit = types.InlineKeyboardButton("Повернутись до чату")
statistics_batt.add(button_number_of_words, button_number_of_characters, button_number_of_digits,
                button_number_of_voice_letters, button_number_of_vowels_letters,
                button_the_number_of_punctuation_marks, button_all, button_exit)

ivan = telebot.TeleBot(config["token"])
@ivan.message_handler(commands=["start"])
def start(message):
    ivan.send_message(message.chat.id, "hello")
    ivan.send_message(message.chat.id, "Ви не є авторизованим користувачем, для відкриття повного функціоналу чатбота уввійдіть у систему", reply_markup=free_access)


# --------------------------------------------------------------------------------------------------------------------



@ivan.message_handler(content_types=["text"])
def get_text(message):
    now_time = time.time()

    file = open(path, "r", encoding='utf-8')
    now_users = file.read().split("\n")
    file.close()
    for el in now_users:
        if len(el.split('/')) > 2:
            if int(el.split('/')[2]) == int(message.chat.id) and (now_time - float(el.split('/')[3])) < 86400:

                if message.text.lower() == "магічний шар":
                    ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Задайте питання"), magic_bol)
                elif message.text.lower() == "перевірка на парність":
                    ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Введіть число для перевірки"), get_text_isd)
                elif message.text.lower() == "перевірка на поліндром":
                    ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Введіть значення для перевірки"), polindrom)
                elif message.text.lower() == "калькулятор":
                    ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Введіть дію"), kalkulator)
                elif message.text.lower() == "щасливий білет":
                    ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Введіть номер білету"), bil)
                elif message.text.lower() == "статистика":
                    ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Які данні вам необхідні?", reply_markup=statistics_batt), statistics)
                elif message.text.lower() == "конвертувати зображення":
                    ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Чекаю на зображення"), conv_img)

            else:
                if message.text == "Hello":
                    ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Hello"), get_text_1)
                elif message.text.lower() == "авторизація":
                    ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Введіть ваше ім'я та пароль через '/' для вхoду у систему чатбота"), authorization)
                elif message.text.lower() == "реєстрація":
                    ivan.register_next_step_handler(
                        ivan.send_message(message.chat.id, "Введіть ваше ім'я та пароль через '/'"), registration)

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
        nowtime = time.time()
        file = open(path, "a", encoding='utf-8')
        file.write(f"{message.text}\n")
        file.close()
        ivan.send_message(message.chat.id, f"Вітаю {rez[0]}, вас успішно зареєстровано у системі ")
    else:
        ivan.send_message(message.chat.id, f"Щось пішло не так. Користувач {rez[0]} вже зареєстрований у системі")


def authorization(message):                                     # Авторизація у системі
    global text
    text = message.text
    path = os.path.join("data_base", "T_b.txt")
    file = open(path, "r", encoding='utf-8')
    log_pass = file.read().split("\n")
    rez = text.split("/")
    var = 0
    for ind in range(len(log_pass)+1):
        log_pass[ind] = log_pass[ind].split('/')
        if rez[0] == log_pass[ind][0] and rez[1] == log_pass[ind][1]:
            ivan.send_message(message.chat.id, f"{rez[0]}, вітаємо у системі", reply_markup=keyboard)
            global nameUser
            nameUser = f"{rez[0]}"
            var, old = 1, time.time()
            log_pass[ind] = f'{log_pass[ind][0]}/{log_pass[ind][1]}/{message.chat.id}/{old}'
            var_var = ''
            print(log_pass)
            for ind in range(len(log_pass)):
                var_var += f'{log_pass[ind]}\n'
            file = open(path, "w", encoding='utf-8')
            file.write(var_var)
            file.close()
            break
    if var == 0:
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


def statistics(message):
    global text
    text = message.text
    ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Введіть данні"), statistics_w)


def statistics_w(message):
    slovo_count, sambol_count, num_count, isdigit_g_count, isdigit_p_count, punct_count = [], 0, 0, 0, 0, 0
    isdigit_g, isdigit_p, num, punct = ["а", "е", "є", "и", "і", "ї", "щ", "у", "ю", "я", "о"], \
                                       ["б", "в", "г", "ґ", "д", "ж", "з", "к","л", "м", "н", "п", "р", "с", "т", "ф","х", "ц", "ч", "ш", "щ"], \
                                       ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], \
                                       [".", ",", "*", "/", "+", "-"]
    slovo_count = message.text.split(" ")
    slovo_count = len(slovo_count)
    for el in message.text:
        sambol_count += 1
        if el in num:
            num_count += 1
        if el in isdigit_g:
            isdigit_g_count += 1
        if el in isdigit_p:
            isdigit_p_count += 1
        if el in punct:
            punct_count += 1
    sum_count = f"Загальна кількість слів:    {slovo_count}\n" \
                f"Загальна кількість символів: {sambol_count}\n" \
                f"Загальна кількість цифр: {num_count}\n" \
                f"Загальна кількість голосних літер: {isdigit_g_count}\n" \
                f"Загальна кількість приголосних літер: {isdigit_p_count}\n" \
                f"Загальна кількість знаків пунктуації: {punct_count}"
    path = os.path.join("data_base", "statistics.txt")
    file = open(path, "w", encoding='utf-8')
    file.write(sum_count)
    file.close()
    if text == "Всю інформацію файлом":
        with open(path, "r", encoding='utf-8') as file:
            ivan.send_document(message.chat.id, file)
            file.close()
    elif text == "кількість слів":
        ivan.send_message(message.chat.id, f"Загальна кількість слів: {slovo_count}", reply_markup=keyboard)
    elif text == "кількість символів":
        ivan.send_message(message.chat.id, f"Загальна кількість символів: {sambol_count}", reply_markup=keyboard)
    elif text == "кількість цифр":
        ivan.send_message(message.chat.id, f"Загальна кількість цифр: {num_count}", reply_markup=keyboard)
    elif text == "кількість голосних літер":
        ivan.send_message(message.chat.id, f"Загальна кількість голосних літер: {isdigit_g_count}", reply_markup=keyboard)
    elif text == "кількість приголосних літер":
        ivan.send_message(message.chat.id, f"Загальна кількість приголосних літер: {isdigit_p_count}", reply_markup=keyboard)
    elif text == "кількість знаків пунктуації":
        ivan.send_message(message.chat.id, f"Загальна кількість знаків пунктуації: {punct_count}", reply_markup=keyboard)
    elif text == "Повернутись до чату":
        ivan.register_next_step_handler(ivan.send_message(message.chat.id, reply_markup=keyboard))


@ivan.message_handler(content_types=['photo'])
def conv_img(message):
    image_filename = str(uuid.uuid4())
    file_id = message.photo[-1].file_id
    file_info = ivan.get_file(file_id)
    downloaded_file = ivan.download_file(file_info.file_path)
    Path("images/").mkdir(parents=True, exist_ok=True)
    Path("txt_reports/").mkdir(parents=True, exist_ok=True)
    with open(f"images/{image_filename}.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    with open(f"images/{image_filename}.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return ivan.send_document(message.chat.id, encoded_string)



ivan.polling(none_stop=True, interval=0)