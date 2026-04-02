from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://practice.qabrains.com/")

email = driver.find_element(By.XPATH,"//input[@id='email']")
email.send_keys("qa_testers@qabrains.com")

password = driver.find_element(By.XPATH,"//input[@id='password']")
driver.execute_script("arguments[0].scrollIntoView();", password)
password.send_keys("Password123") 

btn = driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
btn.click()
time.sleep(5)

