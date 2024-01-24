from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://google.com')
print(f'Nazwa storny {driver.title}')
print('Nazwa strony' ,driver.title)
time.sleep(5)
button1_accept = driver.find_element('id', 'L2AGLb')
button1_accept.click()
time.sleep(5)
search_field = driver.find_element('name', 'q')
search_field.send_keys('Na górze róże')
time.sleep(5)
search_field.send_keys(Keys.ENTER)
# search_button = driver.find_element('name', 'btnK')
# search_button.click()
time.sleep(5)
driver.quit()
