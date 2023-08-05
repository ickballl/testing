import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl
import datetime

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://portalecd.com/')

login = 'ickbal'
pw = 'IckbaL0906'

log1 = driver.find_element(
    By.XPATH, '/html/body/div/div/form/div[1]/input').send_keys(login)
pw1 = driver.find_element(
    By.XPATH, '/html/body/div/div/form/div[2]/input').send_keys(pw)
driver.find_element(
    By.XPATH, '/html/body/div/div/form/div[3]/div[2]/button').click()

driver.get('https://portalecd.com/wm.php?req=engineer_absensi_2023')

workbook = openpyxl.load_workbook('absen.xlsm')
sheet = workbook['Sheet1']

i = 2
while i <= len(sheet['A']):
    date = sheet['A'+str(i)].value
    work = sheet['F'+str(i)].value
    cus = sheet['E'+str(i)].value
    detail = (cus, '-', work)
    i += 1
    date1 = date.strftime('%d/%m/%Y')

    driver.find_element(By.XPATH, '//*[@id="tanggal"]').clear()
    driver.find_element(By.XPATH, '//*[@id="w3review"]').clear()

    driver.find_element(By.XPATH, '//*[@id="tanggal"]').send_keys(date1)
    driver.find_element(By.XPATH, '//*[@id="w3review"]').send_keys(detail)
#     sleep(2)
    driver.find_element(
        By.XPATH, '/html/body/div/div/section[2]/div[1]/div/table/tbody/tr[6]/td[2]/button').click()
    alert = driver.switch_to.alert
    alert.accept()
    sleep(2)
    driver.get('https://portalecd.com/wm.php?req=engineer_absensi_2023')
# driver.get('https://portalecd.com/wm.php?req=engineer_absensi_mei_23&id=ickbal')
