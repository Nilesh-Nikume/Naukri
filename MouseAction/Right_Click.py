import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

Right_click_Button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

Action = ActionChains(driver)

Action.context_click(Right_click_Button).perform()

time.sleep(3)