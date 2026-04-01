from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
element = driver.find_element(By.XPATH, "//input[@name='username']")
element.click()
element.send_keys("tomsmith")

element_2 = driver.find_element(By.XPATH, "//input[@name='password']")
element_2.click()
element_2.send_keys("SuperSecretPassword!")

element_3 = driver.find_element(By.XPATH, "//button")
element_3.click()


element_4 = driver.find_element(By.XPATH, "//div[@class='flash success']")
print(element_4.text)



time.sleep(3)
