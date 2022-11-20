import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os.path

path = os.path.join("data_base", "Hero.txt")
file = open(path, "w", encoding='utf-8')

agent = webdriver.Chrome(executable_path="D:\python\Test\Payton basic\Python_Selenium\chromedriver.exe")
agent.get(url="https://www.marvel.com/characters")

hero = agent.find_elements(By.CLASS_NAME, 'explore__link')
hero_targeted = hero[18:54]
hero_links = []
for el in hero_targeted:
    hero_links.append(el.get_attribute("href"))

hero_info = ""
count = 0
for el in hero_links:
    agent.get(el)
    one_hero = agent.find_element(By.CLASS_NAME, 'masthead__headline')
    hero_ol = agent.find_elements(By.CLASS_NAME, 'railBioLinks li')
    print("len_elements =", len(hero_ol))
    if len(hero_ol) >= 6:
        hero_info += f'Name: {one_hero.text} \nLink: {el} \nUniverse: {hero_ol[0].text} \nOther aliases: {hero_ol[1].text} \n' \
                     f'Education: {hero_ol[2].text} \nPlace of origin: {hero_ol[3].text} \nIdentity: {hero_ol[4].text} \n' \
                     f'Known relatives: {hero_ol[5].text}\n\n'
    elif len(hero_ol) == 5:
        hero_info += f'Name: {one_hero.text} \nLink: {el} \nUniverse: {hero_ol[0].text} \nOther aliases: {hero_ol[1].text} \n' \
                     f'Education: {hero_ol[2].text} \nPlace of origin: {hero_ol[3].text} \nKnown relatives: {hero_ol[4].text}\n\n'
    else:
        hero_info += f'Name: {one_hero.text} \nLink: {el} \nUniverse: None \nOther aliases: None \n' \
                     f'Education: None \nPlace of origin: None \nIdentity: None \n' \
                     f'Known relatives: None\n\n'
file.write(hero_info)
file.close()
time.sleep(3)
agent.close()
