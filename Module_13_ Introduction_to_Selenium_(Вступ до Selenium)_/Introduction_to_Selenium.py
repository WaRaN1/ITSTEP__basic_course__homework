import json

from selenium import webdriver
from selenium.webdriver.common.by import By
import os.path

path = os.path.join("data_base", "Comics_and_autor.json")

agent = webdriver.Chrome(executable_path="D:\\python\\Test\\Payton basic\\Python_Selenium\\chromedriver.exe")

agent.get(url="https://www.marvel.com/comics?&options%5Boffset%5D=0&totalcount=12")
marvel_all = agent.find_elements(By.CLASS_NAME, 'row-item-text')


marvel = {}

for i in marvel_all:
    var = i.text.split("\n")
    if len(var) > 1:
        marvel[var[0]] = var[1]
    else:
        marvel[var[0]] = "-"
print(marvel)

with open(path, "w", encoding='utf-8') as file:
    json.dump(marvel, file, ensure_ascii=False)

