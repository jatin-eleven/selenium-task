from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
password = ""


username = "jimmysharma00000m@gmail.com"

driver = webdriver.Chrome(
    executable_path='C:\Program Files (x86)/chromedriver')

driver.get("https://www.linkedin.com")


title = driver.title
print(title)

# session_key
username_field = "session_key"
username_element = driver.find_element(By.ID, username_field)
username_element.send_keys(username)

password_field = "session_password"
password_element = driver.find_element(By.ID, password_field)
password_element.send_keys(password)


btn_css = "#main-content > section.section.min-h-\[560px\].flex-nowrap.pt-\[40px\].babybear\:flex-col.babybear\:min-h-\[0\].babybear\:px-mobile-container-padding.babybear\:pt-\[24px\] > div > div > form > button"
btn_element = driver.find_element(By.CSS_SELECTOR, btn_css)
time.sleep(3)
print("\n>>>>times over")
btn_element.click()


time.sleep(5)
# global-nav-typeahead > input
# search_inp = "#global-nav-typeahead > input"
search_inp = '//*[@id="global-nav-typeahead"]/input'
# try:
search_inp_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, search_inp))
)
search_inp_element.send_keys("HARSHAL JAIN")
search_inp_element.send_keys(Keys.ENTER)
# except Exception as e:
#     print(">>>> Error Occurred")
#     print("\t", e)


msg_field = "entry-point"
msg_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, msg_field))
)
time.sleep(3)
print("done")
msg_element.click()


# msg-form__contenteditable t-14 t-black--light t-normal flex-grow-1 full-height notranslate

type_msg = "msg-form__contenteditable"
time.sleep(3)
type_msg_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, type_msg))
)
type_msg_element.send_keys("HOLA FOLKS")


# msg-form__send-button artdeco-button artdeco-button--1
send_field = "msg-form__send-button"
send_element = driver.find_element(By.CLASS_NAME, send_field)
time.sleep(3)
print("DONE")
send_element.click()
