from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import os


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.qabrains.com/")

wait = WebDriverWait(driver, 10)
form_sub = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Form Submission']")))
form_sub.click()

name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='name']")))
name.send_keys("Fahad Ali")

email = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='email']")))
email.send_keys("Example@gmail.com")


contact = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='contact']")))
contact.send_keys("03239198902")

date = wait.until(EC.presence_of_element_located((By.ID, "date")))
driver.execute_script("arguments[0].value = '02/04/2026';", date)

color = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Green']")))
driver.execute_script("arguments[0].scrollIntoView();", color)
driver.execute_script("arguments[0].click();", color)

menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Burger']")))
driver.execute_script("arguments[0].scrollIntoView();", menu)
driver.execute_script("arguments[0].click();", menu)


country = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@name='country']")))
select = Select(country)
select.select_by_visible_text("Pakistan")

file_upload = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='file']")))

# If it's hidden, make it visible first
driver.execute_script("arguments[0].style.display = 'block'; arguments[0].style.visibility = 'visible';", file_upload)

# Send the absolute path of your file
abs_path = os.path.abspath(r"C:\Users\F A H A D\Desktop\jobs.PNG")  # put your file name here
file_upload.send_keys(abs_path)

time.sleep(1)

# --- Submit the form ---
submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_btn.click()

time.sleep(2)
print("Form submitted successfully!")


time.sleep(5)