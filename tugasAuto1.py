from selenium import webdriver
# driver = webdriver.Chrome()

# def getUrls(targeturl):
#     driver.minimize_window()
#     driver.get('http://www.'+targeturl+'.com')
#     # title=driver.title
#     # print(dtitle)
#     print(driver.title)

# webPage = ['tokopedia','tiket','orangsiber','automatetheboringstuff']
# for i in webPage:
#     getUrls(i)
#     driver.quit()


#jabawan mba rara yang sangat simple dan betul
# driver = webdriver.Chrome()
# websites = ['https://tiket.com/', 'https://www.tokopedia.com/', 'https://www.orangsiber.com/', 'https://demoqa.com/', 'https://automatetheboringstuff.com/']
# name = ['tiket.com', 'tokopedia.com', 'orangsiber.com', 'demoqa.com', 'automatetheboringstuff.com']

# for (x,y) in zip (websites,name):
#     driver.get(x)
#     print(y + ' - ' + driver.title)  

# mempersimple jawaban mba rara
driver = webdriver.Chrome()
websites = ['https://tiket.com', 'https://tokopedia.com', 'https://orangsiber.com', 'https://demoqa.com', 'https://automatetheboringstuff.com']
for x in websites:
    driver.get(x)
    print(x[8:] + ' - ' + driver.title)  