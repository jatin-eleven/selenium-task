import time
from tkinter import E

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
options = webdriver.ChromeOptions()

options.add_experimental_option("debuggerAddress", "localhost:9014")

options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")

driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver_win32\chromedriver.exe", options=options)

driver.maximize_window()


# driver.get("https://www.linkedin.com/talent/jobs/jobs-list")



# path = "projects-list-jobs-list-item__talent-pool-value"
# jobs = driver.find_element(By.CLASS_NAME, path)
# jobs.click()

# # time.sleep(10)
# driver.implicitly_wait(15)
# print("timer over")


# # check_box = "small-input"
# check_box = "profile-list__select-all"
# check = driver.find_element(By.CLASS_NAME, check_box).click()


# #collapsible-toolbar-ember38188 > li:nth-child(4)
# full_path =  "/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div/main/span/div/form/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/ul/li[4]"

# driver.implicitly_wait(3)
# print("timer over")

# btn_project = driver.find_element(By.XPATH, full_path).click()


# setTimeout(()=>{debugger;},60000)


projectname_field = "save-to-projects-typeahead"
projectname_element = driver.find_element(By.ID, projectname_field)
projectname_element.send_keys("python testing")

time.sleep(5)
print("timer over")

try:
                # /html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[1]/div[1]/div/div[2]/div[2]/div    
                # /html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[1]/div[1]/div/div[2]/div[2]
    drop_down='/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[1]/div[1]/div/div[2]'

        # drop_down='/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[1]/div[1]/div/div[2]/div/div'
    # drop_down='/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[1]/div[1]/div/div[2]/div[2]/div'
    drop_down_ele=driver.find_element(By.XPATH,drop_down)    
    print(drop_down_ele.text)
    time.sleep(5)
    drop_down_ele.click()
except Exception as e  :
    print("ex : ",e)

savebtn="artdeco-button--primary"
savebtn_ele=driver.find_element(By.CLASS_NAME,savebtn)
savebtn_ele.click()
