from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.wikipedia.org/')
driver.maximize_window()
sleep(3)
search = driver.find_element(By.ID, 'searchInput')
print('Working')

english = driver.find_element(By.XPATH, '//option[text()="English"]')
print('Working')

logo_image = driver.find_element(By.CLASS_NAME, "central-featured-logo")
print('working')

languages = driver.find_elements(By.CSS_SELECTOR, 'nav[class="central-featured"] a')
print(len(languages))
print('working')

driver.back()
sleep(3)
driver.forward()
sleep(3)
driver.refresh()
sleep(3)
print(f'The title is :{driver.title}')

driver.quit()