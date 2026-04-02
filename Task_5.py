from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

sign_in = driver.find_element(By.XPATH,"//yt-touch-feedback-shape[@class='yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--overlay-touch-response yt-spec-touch-feedback-shape--down']//div[@class='yt-spec-touch-feedback-shape__fill']")
sign_in.click()

time.sleep(5)