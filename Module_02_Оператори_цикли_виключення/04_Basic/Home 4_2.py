name = input("Ваше ім'я?\n")
height = int(input("Ваш зріст у сантиметах?\n"))
weight = int(input("Ваша вага?\n"))
pol = input("Ваша стать? (чоловіча, жіноча)\n")
ideal_for_man = (height - 100) * 1.15
ideal_for_woman = (height - 110) * 1.15
if pol == "чоловіча":
    print(name, "ваша ідеальна вага -", ideal_for_man)
else:
    print(name, "ваша ідеальна вага -", ideal_for_woman)






