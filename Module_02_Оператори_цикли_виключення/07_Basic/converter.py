metrs = float(input("Введідь довжину в метрах\n"))
new_unit = input("У які одиниці виміру небхідно перевести? Милі, дюйми чи ярди?\n")
if new_unit == "милі":
    print(metrs, "м =", metrs * 0.000621371, "mi")
elif new_unit == "дюйми":
    print(metrs, "м =", metrs * 39.3701, "in")
elif new_unit == "ярди":
    print(metrs, "м =", metrs * 1.09361, "yd")
