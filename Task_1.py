from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# TASK 1
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/?utm_source=chatgpt.com")
# title = driver.title
# print(title)
# time.sleep(5)


# TASK 2
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/?utm_source=chatgpt.com")
# element = driver.find_element(By.CSS_SELECTOR, "a[href='/checkboxes']")
# element.click()
# element_2 = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input")
# element_2[0].click()
# print(element_2[0].is_selected())
# time.sleep(3)

# TASK 3
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/?utm_source=chatgpt.com")

element = driver.find_element(By.CSS_SELECTOR, "a[href='/inputs']")
element.click()

element_2 = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
element_2.click()
element_2.send_keys("12345")
element_2.clear()
element_2.send_keys("999")
time.sleep(3)