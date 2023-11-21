from selenium import webdriver
import time


browser = webdriver.Chrome()

# get()
browser.get("https://google.com")

# maximize_window()
browser.maximize_window()

time.sleep(2)

# refresh()
browser.refresh()

# get()
browser.get("https://www.saucedemo.com/")

time.sleep(5)

# back()
browser.back()
time.sleep(2)

# forward()
browser.forward()
time.sleep(2)

browser.switch_to.new_window("tab")
time.sleep(2)

# close()
browser.close()
time.sleep(2)

# quit()
browser.switch_to.new_window("tab")
browser.switch_to.new_window("tab")
time.sleep(3)
browser.quit()
