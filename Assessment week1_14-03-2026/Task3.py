from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.flipkart.in/')
print(f'The title is {driver.title}')
sleep(3)

driver.get('https://www.myntra.com/')
print(f'The title is {driver.title}')
sleep(3)

driver.get('https://www.nike.in/')
print(f'The title is {driver.title}')
sleep(3)

driver.get('https://www.hindustantimes.com/')
print(f'The title is {driver.title}')
sleep(3)

driver.get('https://www.python.org/')
print(f'The title is {driver.title}')
sleep(3)


driver.quit()
