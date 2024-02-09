import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Use By.XPATH to specify the locator method
Double_Click = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")

Action = ActionChains(driver)
Action.double_click(Double_Click).perform()
time.sleep(3)

driver.close()