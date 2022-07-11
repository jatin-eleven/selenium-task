"""
Error: “chromedriver” cannot be opened because the developer cannot be verified.
Solution: xattr -d com.apple.quarantine /Users/admas/Downloads/chromedriver
"""
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\selenium\chromedriver_win32\chromedriver.exe')
# driver = webdriver.Firefox()

driver.get('http://demostore.supersqa.com')


import pdb; pdb.set_trace()

print(driver.title)
