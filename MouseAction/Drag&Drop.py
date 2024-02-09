import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

Soure_elements = driver.find_element(By.XPATH,  "//div[@id='draggable']")
Traget_elements = driver.find_element(By.XPATH,  "//div[@id='droppable']")

Action = ActionChains(driver)
Action.drag_and_drop(Soure_elements,Traget_elements).perform()

time.sleep(3)
driver.close()


