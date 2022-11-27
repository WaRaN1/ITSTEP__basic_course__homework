import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os.path

path = os.path.join("data_base", "Lardi.txt")
file = open(path, "w", encoding='utf-8')

agent = webdriver.Chrome(executable_path="/Payton basic/Python_Selenium/chromedriver.exe")
agent.get(url="https://lardi-trans.ua/ru/")

element1 = WebDriverWait(agent, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "main-nav-category")))
agent.find_element(By.CLASS_NAME, "main-nav-category").click()

element6 = WebDriverWait(agent, 5).until(EC.presence_of_element_located((By.ID, "react-select-2-input")))
city = agent.find_element(By.ID, "react-select-2-input")
city.send_keys("Украина")
time.sleep(1)
city.send_keys(Keys.ENTER)

element2 = WebDriverWait(agent, 5).until(EC.presence_of_element_located((By.ID, "react-select-4-input")))
city = agent.find_element(By.ID, "react-select-4-input")
city.send_keys("Киев")
time.sleep(1)
city.send_keys(Keys.ENTER)

element4 = WebDriverWait(agent, 5).until(EC.presence_of_element_located((By.ID, "react-select-8-input")))
city = agent.find_element(By.ID, "react-select-8-input")
city.send_keys("Запорожье")
time.sleep(1)
city.send_keys(Keys.ENTER)

time.sleep(1)
element5 = WebDriverWait(agent, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#proposal-search > div > div > div.proposal-search__footer > div.proposal-search__side.proposal-search__side_center > button")))
agent.find_element(By.CSS_SELECTOR, "#proposal-search > div > div > div.proposal-search__footer > div.proposal-search__side.proposal-search__side_center > button").click()

price = []
sum = []
count = 0
while count != 1:
    try:
        time.sleep(1)
        element7 = WebDriverWait(agent, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "ps_data_payment_info")))
        variable_price = agent.find_elements(By.CLASS_NAME, 'ps_data_payment_info')

        for el in variable_price:
            if len(el.text) > 1:
                price.append(el.text)

        time.sleep(1)
        element8 = WebDriverWait(agent, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "ps_data_wrapper ")))
        variable_v = agent.find_elements(By.CLASS_NAME, 'ps_data_wrapper ')
        time.sleep(1)

        for el in variable_v:
            sum.append(el.text)

        element9 = WebDriverWait(agent, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search-results > div > div.ps_paginator.tp_pagination > div > nav > ul > li.lrd-paginator__forward.lrd-paginator__arrow > a")))
        agent.find_element(By.CSS_SELECTOR, "#search-results > div > div.ps_paginator.tp_pagination > div > nav > ul > li.lrd-paginator__forward.lrd-paginator__arrow > a").click()
    except:
        count = 1

price_filter = []
for i in range(len(price)):
    if price[i].split(" ")[0] != 'запрос':
        price[i].split(" ")[0] = int
        el = price[i].split(" ")[0]
        if float(el) >= 2000.0:
            price_filter.append(i)

text = ""
for i in range(len(sum)):
    if i in price_filter:
        text += f'{sum[i]}\n\n--------------------------\n\n'


file.write(text)
file.close()
time.sleep(3)
agent.close()