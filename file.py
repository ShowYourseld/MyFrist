from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import random

browser = webdriver.Firefox()
browser.get('https://play2048.co/')
time.sleep(3)


score_elem = browser.find_elements(By.CLASS_NAME, "shrink-1")[0]
html_elem = browser.find_element(By.TAG_NAME,'html')

while int(score_elem.text) < 10000:
    html_elem.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.2)
    html_elem.send_keys(Keys.ARROW_LEFT)
    time.sleep(0.2)
    html_elem.send_keys(Keys.ARROW_UP)
    time.sleep(0.2)
    html_elem.send_keys(Keys.ARROW_RIGHT)
    time.sleep(0.2)
    score_elem = browser.find_elements(By.CLASS_NAME, "shrink-1")[0]
