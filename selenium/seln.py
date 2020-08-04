from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://www.youtube.com/channel/UCZdaR5QvofZ_TzVAcnRir_A?view_as=subscriber"

driver.get(url)

time.sleep(2)
driver.maximize_window()
title = driver.title
print(title)
time.sleep(3)

driver.close()


