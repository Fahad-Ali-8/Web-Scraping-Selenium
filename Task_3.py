from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")

# check_box = driver.find_elements(By.XPATH, "//input[@type='checkbox']")


# if check_box[0].is_selected():
#     print("Already Selected")
# else:
#     print("Not Selected now Selected")
#     check_box[0].click()



# if check_box[1].is_selected():
#     print("Already Selected")
# else:
#     print("Not Selected now selected")
#     check_box[1].click()    
    

# check_boxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

# for i,cb in enumerate(check_boxes):
#     if cb.is_selected():
#         print(f"Checkbox {i+1} already selected")
#     else:
#         print(f"Checkbox {i+1} was not selected → now selected")
#         cb.click()    

# time.sleep(5)



# TASK 3

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")

drop_down = driver.find_element(By.XPATH, "//select[@id='dropdown']")
drop_down.click()

time.sleep(5)