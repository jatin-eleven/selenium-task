

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pdb

driver = webdriver.Chrome(executable_path='/Users/admas/Downloads/chromedriver')

driver.get('http://demostore.supersqa.com')

# By.ID
cart = driver.find_element(By.ID, "site-header-cart")
print(cart)
print(type(cart))
cart_txt = cart.text
print(cart_txt)

# By.ID
search_field = driver.find_element(By.ID, 'woocommerce-product-search-field-0')
search_field.send_keys('Hoodie')
# search_field.send_keys(Keys.ENTER)

# By.CSS_SELECTOR
# my_acct = driver.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9')
# my_acct = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]')
# my_acct = driver.find_element(By.XPATH, '/html/body/div/header/div[2]/div/nav/div[1]/ul/li[4]')
# my_acct.click()

pdb.set_trace()

# driver.quit()
# driver.close()