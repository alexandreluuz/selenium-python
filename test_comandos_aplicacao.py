from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("https://www.saucedemo.com/")

# title
print("O título da página é: ", browser.title)

# current_url
print("O URL da página é: ", browser.current_url)

# page_source
print("O código-fonte da página é: ", browser.page_source)
