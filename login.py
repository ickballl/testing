import pwinput
import selenium
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

LoginId = input('Masukan Login ID / Email / Nomer telp yang terdafatr : ')
pwd = getpass('Password : ')

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://seller.shopee.co.id')

login = driver.find_element(By.XPATH,'//*[@id="shop-login"]/div[1]/div/div[1]/div/div/input').send_keys(LoginId)
pwd2 = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[3]/div/div/div/form/div[2]/div/div[1]/div/div/input').send_keys(pwd)
button_login = driver.find_element(By.XPATH,'//*[@id="shop-login"]/div[4]/div/div/button').click()
sleep(10)

