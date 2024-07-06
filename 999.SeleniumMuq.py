from selenium import webdriver
import time

driver = webdriver.Chrome()

url ="https://github.com/"
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("gitgub.com-homepage.png")

url ="https://github.com/Melikeda"
driver.get(url)

print(driver.title)
time.sleep(4)
driver.back()

time.sleep(2)
driver.close()
