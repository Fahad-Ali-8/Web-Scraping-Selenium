# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

# # Keep browser open after script ends
# options = Options()
# options.add_experimental_option("detach", True)

# # If using manual chromedriver (put your path)
# service = Service("C:\webdriver\chromedriver.exe")

# # Start browser              
# driver = webdriver.Chrome(service=service , options=options)

# # Open website
# driver.get("https://www.youtube.com")

# # Print page title
# print(driver.title)





from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.timesjobs.com")

title = driver.find_element(By.TAG_NAME, "h1").text
print(title)

driver.quit()