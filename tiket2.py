from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver= webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.tiket.com')
Title = driver.title
search = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/header/div/div[3]/div[1]/div/label/div/div/div/label/input').send_keys('Bandung')
sleep(2)
clear = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/header/div/div[3]/div[1]/div/label/div/div/div/label/input').clear()
# sleep(3)
button_hotel = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div[2]/div[1]/section[1]/div/div/div[2]/div[1]/section/div/div/div[2]/button')
button_hotel.click()
# sleep(3)
ambil_text = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div[2]/div[1]/section[1]/div/div/div[1]/div/h2')
print(ambil_text.text)
# sleep(3)
try:
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/main/div[1]/div[2]/div[1]/section[1]/div/div/div[2]/div[2]/div[1]/div/div[2]/div')))
    print('Nemu Banner')
except TimeoutException:
    print('kagak Muncul')
    pass
sleep(3)
button_hotel_img = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/header/div/div[3]/div[2]/div/div/ul/li[2]/a')
button_hotel_img.click()
sleep(3)