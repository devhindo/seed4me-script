from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def wait(seed):
    seed.implicitly_wait(30)

def generate_password(n):
    import random
    import string
    password = ''
    for i in range(n):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation + string.digits)
    return password

chrome_options = Options()
chrome_options.add_argument("--incognito")

mohml = webdriver.Chrome(chrome_options=chrome_options)
mohml.get("https://www.mohmal.com/")
wait(mohml)
create_account = mohml.find_element(By.XPATH, "//*[@id=\"rand\"]")
create_account.click()
wait(mohml)

email_element = mohml.find_element(By.XPATH, "//*[@id=\"email\"]/div[1]")
email = email_element.text

seed = webdriver.Chrome(chrome_options=chrome_options)
seed.get("https://seed4.me/")
wait(seed)

my_account = seed.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/ul/li[8]/a")
my_account.click()
wait(seed)

create_seed4me_account = seed.find_element(By.XPATH, "/html/body/div[3]/div/div/a[2]")
create_seed4me_account.click()
wait(seed)

email_textbox = seed.find_element(By.XPATH, "//*[@id=\"UserUsername\"]")
email_textbox.send_keys(email)
password_textbox = seed.find_element(By.XPATH, "//*[@id=\"UserPassword\"]")
password = generate_password(10)
password_textbox.send_keys(password)
confirm_password_textbox = seed.find_element(By.XPATH, "//*[@id=\"UserConfirmPassword\"]")
confirm_password_textbox.send_keys(password)
confirm = seed.find_element(By.XPATH, "//*[@id=\"UserAccept\"]")
confirm.click()

register = seed.find_element(By.XPATH, "//*[@id=\"UserRegisterForm\"]/div[8]/div/input")
register.click()

while True:
    pass