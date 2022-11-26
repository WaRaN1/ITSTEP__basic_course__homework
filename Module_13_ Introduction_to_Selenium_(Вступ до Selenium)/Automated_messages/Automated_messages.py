import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

agent = webdriver.Chrome(executable_path="D:\python\Test\Payton basic\Python_Selenium\chromedriver.exe")
agent.get(url="https://outlook.office.com/mail/")


element = WebDriverWait(agent, 5).until(EC.presence_of_element_located((By.ID, "i0116")))
login = agent.find_element(By.ID, "i0116")
login.send_keys("Bezko_hs06@student.itstep.org")

element1 = WebDriverWait(agent, 5).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
agent.find_element(By.ID, "idSIButton9").click()

element2 = WebDriverWait(agent, 5).until(EC.presence_of_element_located((By.ID, "i0118")))
password = agent.find_element(By.ID, "i0118")
password.send_keys("iS57H4y6")

element3 = WebDriverWait(agent, 5).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
agent.find_element(By.ID, "idSIButton9").click()

element4 = WebDriverWait(agent, 5).until(EC.element_to_be_clickable((By.ID, "idBtn_Back")))
agent.find_element(By.ID, "idBtn_Back").click()

element5 = WebDriverWait(agent, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#innerRibbonContainer > div.groupContainer-208 > div > div > div > div:nth-child(2) > div > div > span > button.splitPrimaryButton.root-218")))
agent.find_element(By.CSS_SELECTOR, "#innerRibbonContainer > div.groupContainer-208 > div > div > div > div:nth-child(2) > div > div > span > button.splitPrimaryButton.root-218").click()

element6 = WebDriverWait(agent, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#docking_InitVisiblePart_0 > div > div.QFieH > div:nth-child(1) > div > div.AtODR.lG_qQ > div > div > div.VbY1P.T6Va1.Z4n09")))
whom = agent.find_element(By.CSS_SELECTOR, "#docking_InitVisiblePart_0 > div > div.QFieH > div:nth-child(1) > div > div.AtODR.lG_qQ > div > div > div.VbY1P.T6Va1.Z4n09")
whom.send_keys("sasha.ozerov98@gmail.com")

element7 = WebDriverWait(agent, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#TextField718")))
whom = agent.find_element(By.CSS_SELECTOR, "#TextField718")
whom.send_keys("Test message")

element8 = WebDriverWait(agent, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#editorParent_1 > div")))
whom = agent.find_element(By.CSS_SELECTOR, "#editorParent_1 > div")
whom.send_keys("Hello, this is a test message")

element9 = WebDriverWait(agent, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#docking_InitVisiblePart_0 > div > div.QH6of.yhWog.UFgnU > div.R6yXY.CEwXY > div.OTADH.xukFz > div > div > span > button.ms-Button.ms-Button--primary.ms-Button--hasMenu.b56tW.root-390")))
agent.find_element(By.CSS_SELECTOR, "#docking_InitVisiblePart_0 > div > div.QH6of.yhWog.UFgnU > div.R6yXY.CEwXY > div.OTADH.xukFz > div > div > span > button.ms-Button.ms-Button--primary.ms-Button--hasMenu.b56tW.root-390").click()

time.sleep(3)
agent.close()