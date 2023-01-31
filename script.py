from selenium import webdriver
from selenium.webdriver.common.by import By

def wait(driver):
    driver.implicitly_wait(30)

mohml = webdriver.Chrome()
mohml.get("https://www.mohmal.com/")
wait(mohml)
create_account = mohml.find_element(By.XPATH, "//*[@id=\"rand\"]")
create_account.click()
wait(mohml)
email_element = mohml.find_element(By.XPATH, "//*[@id=\"email\"]/div[1]")
email = email_element.text
print(email)
