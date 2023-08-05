from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.nfl.com/schedules/2022/POST1/')
sleep(20)