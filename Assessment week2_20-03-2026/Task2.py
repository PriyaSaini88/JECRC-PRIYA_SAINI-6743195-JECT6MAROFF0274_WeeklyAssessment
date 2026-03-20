from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://automationexercise.com/signup')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

home_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//i[@class = "fa fa-home"]')))
home_btn.click()

sign_up = wait.until(EC.element_to_be_clickable((By.XPATH, '//i[@class = "fa fa-lock"]')))
sign_up.click()

name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@data-qa = 'signup-name']")))
name.send_keys("Xyz")

email = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@data-qa = 'signup-email']")))
email.send_keys("xyz12@gmail.com")

signup_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa = 'signup-button']")))
signup_btn.click()

gender=wait.until(EC.element_to_be_clickable((By.ID,'id_gender2')))
gender.click()

newsletter=wait.until(EC.element_to_be_clickable((By.ID,'newsletter')))
newsletter.click()

special_offer=wait.until(EC.element_to_be_clickable((By.ID,'optin')))
special_offer.click()

print(f"Newsletter :{newsletter.get_attribute('checked')}")
print(f"Offer:{special_offer.get_attribute('checked')}")


driver.quit()

