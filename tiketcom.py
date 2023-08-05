# import selenium  = import keseluruhan lib dari selenium
from selenium import webdriver
driver = webdriver.Chrome()
driver.minimize_window
while True:
    driver.get('https://www.tiket.com/')
    driver.get('https://www.tokopedia.com/')
    driver.get('https://www.orangsiber.com/')
    # driver.get('https://www.demoqa.com/')
    driver.get('https://www.automatetheboringstuff.com/')
    title = driver.title(f'driver.get')
    print(title)
    break

