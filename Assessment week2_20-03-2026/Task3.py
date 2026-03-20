from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get("https://google.com")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

search = wait.until(EC.visibility_of_element_located((By.ID, 'APjFqb')))
search.send_keys("Selenium Python")

suggestions = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//ul[@class = "G43f7e"]/child::li')))
for i in suggestions:
    print(i.text)

click_suggest = wait.until(EC.element_to_be_clickable((By.XPATH,'//ul[@role="listbox"]/child::li[5]')))
click_suggest.click()

driver.quit()



