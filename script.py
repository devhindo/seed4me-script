from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
input()
#browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/ul/li[8]/a').click()
#browser.find_element_by_xpath('/html/body/div[3]/div/div/a[2]').click()
