import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
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
driver.find_element(By.XPATH, '/html/body/div/div/section[1]/h1/a[4]').click()
driver.find_element(
    By.XPATH, '/html/body/div/div/section[2]/div/div/table/tbody/tr[1]/td[5]/a').click()

workbook = openpyxl.load_workbook('absen.xlsm')
sheet = workbook['Sheet1']


i = 2
while i <= len(sheet['A']):
    date = sheet['A'+str(i)].value
    date2 = sheet['B'+str(i)].value
    jam1 = sheet['C'+str(i)].value
    jam = sheet['D'+str(i)].value
    work = sheet['F'+str(i)].value
    project = sheet['G'+str(i)].value
    i += 1
    # convert format jam
    jam2 = jam1.strftime('%H:%M')
    jam3 = jam.strftime('%H:%M')
    # Convert Format Tanggal
    date = date.strftime('%Y-%m-%d')
    date2 = date2.strftime('%Y-%m-%d')

    WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="clock_a"]')))
    driver.find_element(By.ID, 'datepicker').clear()
    driver.find_element(By.XPATH, '//*[@id="clock_b"]').clear()
    driver.find_element(By.XPATH, '//*[@id="clock_a"]').clear()
    driver.find_element(By.XPATH, '//*[@id="w3review"]').clear()
    driver.find_element(
        By.XPATH, '//*[@id="example1_filter"]/label/input').clear()
    driver.find_element(By.ID, 'datepicker_timea').clear()
    driver.find_element(By.ID, 'datepicker_timeb').clear()

    driver.find_element(By.ID, 'datepicker').send_keys(date)
    driver.find_element(By.ID, 'datepicker_timea').send_keys(date)
    driver.find_element(By.ID, 'datepicker_timeb').send_keys(date2)
    driver.find_element(By.ID, 'clock_a').send_keys(jam2)
    driver.find_element(By.ID, 'clock_b').send_keys(jam3)
    driver.find_element(By.ID, 'w3review').send_keys(work)
    driver.find_element(
        By.XPATH, '//*[@id="example1_filter"]/label/input').send_keys(project)
    driver.find_element(By.XPATH, '//*[@id="example1"]/tbody/tr').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/section[2]/div[1]/div/table/tbody/tr[15]/td[2]/button').click()
    alert = driver.switch_to.alert
    alert.accept()
    driver.get('https://portalecd.com/wm.php?req=labor')
sleep(20)

# for i in range (1):
#     driver.find_element(By.ID,'datepicker').send_keys(date[i])
#     driver.find_element(By.XPATH,'//*[@id="clock_a"]').clear()
#     driver.find_element(By.XPATH,'//*[@id="clock_b"]').clear()
#     driver.find_element(By.ID,'datepicker_timea').send_keys(date2[i])
#     driver.find_element(By.ID,'datepicker_timeb').send_keys(date2[i])
#     driver.find_element(By.ID,'clock_a').send_keys(jam1[i])
#     driver.find_element(By.ID,'clock_b').send_keys(jam[i])
#     driver.find_element(By.XPATH,'//*[@id="w3review"]').clear()
#     driver.find_element(By.ID,'w3review').send_keys(work[i])
#     driver.find_element(By.XPATH,'//*[@id="example1_filter"]/label/input').send_keys(project[i])
#     driver.find_element(By.XPATH,'//*[@id="example1"]/tbody/tr').click()
# driver.find_element(By.XPATH,'/html/body/div[1]/div/section[2]/div[1]/div/table/tbody/tr[15]/td[2]/button').click()
# driver.get('https://portalecd.com/wm.php?req=labor')
