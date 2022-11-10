

    #1

# Створіть клас Device, який містить інформацію про пристрій.
    # За допомогою механізму успадкування реалізуйте клас
    # CoffeeMachine (містить інформацію про кавомашину), клас
    # Blender (містить інформацію про блендер), клас MeatGrinder
    # (містить інформацію про м’ясорубку).
    # Кожен із класів має містити необхідні для роботи методи.


# class Device:
#     def __init__(self, guarantee):
#         self.guarante = guarantee
#
# class CofeeMachine(Device):
#     def __init__(self, guarantee, pump_pressure, type_of_coffee):
#         super().__init__(guarantee)
#         self.pump_pressure = pump_pressure
#         self.type_of_coffee = type_of_coffee
#
#     def change_pump_pressure(self, new_pump_pressure):
#         self.pump_pressure = new_pump_pressure
#         return "Saved"
#
#     def change_type_of_coffee(self, new_type_of_coffee):
#         self.type_of_coffee = new_type_of_coffee
#         return "Saved"
#
#     def __repr__(self):
#         return f'CofeeMachine - guarantee: {self.guarante}, ' \
#                f'pump_pressure: {self.pump_pressure}, type_of_coffee: {self.type_of_coffee}'
#
# class Blender(Device):
#     def __init__(self, guarantee, type_of_blender, number_of_speeds):
#         super().__init__(guarantee)
#         self.type_of_blender = type_of_blender
#         self.number_of_speeds = number_of_speeds
#
#     def __repr__(self):
#         return f'Blender - guarantee: {self.guarante}, ' \
#                f'type of blender: {self.type_of_blender}, number of speeds: {self.number_of_speeds}'
#
# class MeatGrinder(Device):
#     def __init__(self, guarantee, reverse, brend):
#         super().__init__(guarantee)
#         self.reverse = reverse
#         self.brend = brend
#
#     def __repr__(self):
#         return f'MeatGrinder - guarantee: {self.guarante}, ' \
#                f'reverse: {self.reverse}, brend: {self.brend}'
#
#
# x203 = CofeeMachine("one ears", "15 Bar", "grain")
# print(x203)
#
# x203.change_pump_pressure("25 Bar")
# print(x203)
#
# b527 = Blender("one ears", "immersive", "1")
# print(b527)
#
# cvr524 = MeatGrinder("one ears", "yes", "Bosch")
# print(cvr524)



# ---------------------------------------


    #2

# Створіть клас Ship, який містить інформацію про кораблі.
    # За допомогою механізму успадкування реалізуйте клас
    # Frigate (містить інформацію про фрегат), клас Destroyer (містить
    # інформацію про есмінця), клас Cruiser (містить інформацію
    # про крейсер).
    # Кожен із класів має містити необхідні для роботи методи.

# class Ship:
#     def __init__(self, subordination, water_tonnage):
#         self.subordination = subordination
#         self.water_tonnage = water_tonnage
#
# class Frigate(Ship):
#     def __init__(self, subordination, water_tonnage, name, type_fregate):
#         super().__init__(subordination, water_tonnage,)
#         self.name = name
#         self.type_fregate = type_fregate
#
#     def __repr__(self):
#         return f'Frigate - subordination: {self.subordination}, water_tonnage: {self.water_tonnage}, ' \
#                f'name: {self.name}, type_fregate: {self.type_fregate}'
#
#
#
# class Destroyer(Ship):
#     def __init__(self, subordination, water_tonnage, name, type_destroyer):
#         super().__init__(subordination, water_tonnage)
#         self.name = name
#         self.type_destroyer = type_destroyer
#
#     def __repr__(self):
#         return f'Destroyer - subordination: {self.subordination}, water_tonnage: {self.water_tonnage}, ' \
#                f'name: {self.name}, type_destroyer: {self.type_destroyer}'
#
# class Cruiser(Ship):
#     def __init__(self, subordination, water_tonnage, name, type_cruiser):
#         super().__init__(subordination, water_tonnage)
#         self.name = name
#         self.type_cruiser = type_cruiser
#
#     def __repr__(self):
#         return f'Cruiser - subordination: {self.subordination}, water_tonnage: {self.water_tonnage}, ' \
#                f'name: {self.name}, type_cruiser: {self.type_cruiser}'
#
# getman_sagaidachnyu = Frigate("Військово-Морські Сили Збройних Сил України", "3 274 т", "Гетьман Сагайдачний", "проєкт 11351")
# print(getman_sagaidachnyu)
#
# dragon = Destroyer("Kоролівські Військово-Морські Сили Великої Британії", "8 500 т", "Dragon", "D35")
# print(dragon)
#
# ukraine = Cruiser("Військово-Морські Сили Збройних Сил України", "9 300 т", "Україна", "1164 «Атлант»")
# print(ukraine)


# --------------------------------------------------------------------


    #3

# Запрограмуйте клас Money (об’єкт класу оперує однією
    # валютою) для роботи з грошима.
    # У класі мають бути передбачені: поле для зберігання цілої
    # частини грошей (долари, євро, гривні тощо) і поле для зберігання копійок (центи, євроценти, копійки тощо).
    # Реалізуйте методи виведення суми на екран, задання значень частин.
    # Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для
    # зменшення ціни на задане число.
    # Для кожного з класів реалізуйте необхідні методи та поля.

# Чомусь мені більш за все симпатизує варіант переведення всіх сумм у копійки та проведення розрахунків в них, з
    # подальним переведення до цілих та копійок

class Money:
    def __init__(self, cili, pennies, currency):
        self.currency = currency
        self.cili = cili
        self.pennies = pennies
        self.curs = {"UAH": {"UAH": 1, "DOL": 42, "UER": 41}, "DOL": {"UAH": 0.025, "DOL": 1, "UER": 0.025},
                     "EUR": {"UAH": 0.24, "DOL": 0.98, "UER": 1}}

    def __repr__(self):
        return f'{self.cili}. {self.pennies}  {self.currency}'

    def sell(self, product):
        money_sum = self.cili * 100 + self.pennies
        product_sum = (product.cili * self.curs.get(self.currency).get(product.currency)) * 100 + (product.pennies * self.curs.get(self.currency).get(product.currency))

        if money_sum > product_sum:
            money_sum = money_sum - product_sum
            self.cili = int(money_sum/100)
            self.pennies = int(str(int(money_sum))[-2::])                   # переводимо в інтт, щоб прибрати дробові чісла після переведення вілюти
            viz_pennies = str(int(money_sum))[-2::]                         # якщо в нас в загальній суммі копійок 07, то по факту, це 7 коп, проте для візуольного відображення нам потрібно 0,07
        else:
            return "You don't have enough money to make a purchase"
        return f'З вас списано: {product}\nЗалишок: {self.cili}.{viz_pennies} {self.currency}'


    def change_UAH(self, new_u):
        self.UAH = new_u
        return "Saved"

    def change_pennies(self, new_p):
        self.pennies = new_p
        return "Saved"


class Product(Money):
    pass




money = Money(250, 10, "DOL")
coffe = Product(42, 00, "UAH")

rogalik = Product(5, 10, "DOL")

print(money.sell(coffe))
print(money.sell(rogalik))
