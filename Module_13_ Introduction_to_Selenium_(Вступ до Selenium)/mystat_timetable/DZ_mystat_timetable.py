import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os.path

path = os.path.join("data_base", "Timetable.txt")
file = open(path, "w", encoding='utf-8')

agent = webdriver.Chrome(executable_path="D:\python\Test\Payton basic\Python_Selenium\chromedriver.exe")
agent.get(url="https://mystat.itstep.org/")
time.sleep(2)
login = agent.find_element(By.CSS_SELECTOR, "#username")
login.send_keys("Bezko_hs06")
password = agent.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("iS57H4y6")
agent.find_element(By.CLASS_NAME, "login-action").click()
time.sleep(2)

agent.find_element(By.CLASS_NAME, 'schedule-item a').click()
time.sleep(2)

holder = agent.find_elements(By.CLASS_NAME, 'active-day')
var = ""

for i in range(len(holder)):
    holder[i].click()
    time.sleep(1)
    a = agent.find_elements(By.CLASS_NAME, 'on-hover')
    for j in a:
        var = var + f'{j.text}\n\n\n'
    agent.find_element(By.CSS_SELECTOR, 'button span').click()
    time.sleep(1)

file.write(var)
file.close()
time.sleep(1)
agent.close()