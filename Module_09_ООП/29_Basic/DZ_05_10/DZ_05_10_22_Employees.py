import json
import os.path
from easygui import *

# dict = {
#   "Ivanov Oleg": {
#     "Name": "Ivanov Oleg",
#     "Age": "20",
#     "Work": "teacher"
#   },
#   "Iidorov Max": {
#     "Name": "Iidorov Max",
#     "Age": "40",
#     "Work": "Boss"
#   },
#   "Kenobi Obi-Wan": {
#     "Name": "Kenobi Obi-Wan",
#     "Age": "20",
#     "Work": "BigBoss"
#   }
# }
path = os.path.join("data_base", "File1.json")
path2 = os.path.join("data_base", "File4.json")

while True:
    interface = buttonbox("Choise action: ", "Employees", ["ADD", "DEL", "EDITING", "SEARCH", "All", "EXIT"])
    if interface == "ADD":
        data = multenterbox("Enter your Employees: ", "Employees", ["SURNAME and NAME", "AGE", "WORK"])
        with open(path, "r") as file:
            old_data = json.load(file)
        old_data[data[0]] = {"Name": data[0], "Age": data[1], "Work": data[2]}
        with open(path, "w") as file:
            json.dump(old_data, file)

    elif interface == "DEL":
        with open(path, "r") as file:
            dict = json.load(file)
        name_del = multenterbox("Enter your delete Employees: ", "Employees", ["SURNAME and NAME"])
        dict.pop(name_del[0])
        with open(path, "w") as file:
            json.dump(dict, file)

    elif interface == "EDITING":
        with open(path2, "r") as file:
            dict = json.load(file)
        data = multenterbox("Enter your words: ", "Dictionary", ["Name", "Change_Parameter", "Change_Meaning"])
        dict[data[0]][data[1]] = data[2]
        with open(path, "w") as file:
            json.dump(dict, file)



    elif interface == "SEARCH":
        with open(path, "r") as file:
            old_data = json.load(file)
        data = multenterbox("Enter your words: ", "Dictionary", ["Parameter", "Meaning"])
        msg_box = ""
        rezult_search = {}
        for element in old_data:
            if data[1] == old_data.get(element).get(data[0]):
                msg_box = msg_box + f'Name: {element}, Age: {old_data.get(element).get("Age")}, Work: {old_data.get(element).get("Work")}\n'
                rezult_search[element] = old_data[element]
                print(rezult_search)
            elif old_data[element][data[0]].startswith(data[1]):
                msg_box = msg_box + f'Name: {element}, Age: {old_data.get(element).get("Age")}, Work: {old_data.get(element).get("Work")}\n'
                rezult_search[element] = old_data[element]
                print(rezult_search)
        interface2 = buttonbox(f'{msg_box}', "Employees", ["Ok", "Saved"])
        if interface2 ==  "Saved":
            with open(path2, "w") as file:
                json.dump(rezult_search, file)
        else:
            break

    elif interface == "All":
        with open(path, "r") as file:
            old_data = json.load(file)
        msg_box = "\n".join([f'Name: {element}, Age: {old_data.get(element).get("Age")}, Work: {old_data.get(element).get("Work")}' for element in old_data])
        interface2 = buttonbox(f'{msg_box}', "Employees", ["Ok", "Saved"])
        if interface2 == "Saved":
            path2 = os.path.join("data_base", "File4.json")
            with open(path2, "w") as file:
                json.dump(old_data, file)
    else:
        break
