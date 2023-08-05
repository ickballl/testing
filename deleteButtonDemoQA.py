from selenium import webdriver
from selenium.webdriver.common.by import By

# buat instance dari Selenium WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# buka halaman web
driver.get("https://demoqa.com/webtables")

# cari semua tombol hapus pada halaman web
delete_buttons = driver.find_element(By.XPATH,"//button[@class='btn btn-danger']")

# hitung jumlah tombol hapus yang ditemukan
num_delete_buttons = len(delete_buttons)

# tampilkan jumlah tombol hapus yang ditemukan
print("Jumlah tombol hapus adalah:", num_delete_buttons)

# tutup browser
driver.quit()
