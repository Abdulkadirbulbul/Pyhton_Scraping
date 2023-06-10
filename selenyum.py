from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



# ChromeDriver'ı kullanarak Chrome tarayıcısını başlat
driver = webdriver.Chrome("E:\Python\selenium_instagram\chromedriver.exe")

# Web sayfasını aç
driver.get("https://www.linkedin.com/feed/")
time.sleep(2)
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
input_element = driver.find_element("name","email-address")
input_element.send_keys("username@gmail.com")

input_element = driver.find_element("name","password")
input_element.send_keys("pasword")

buton=driver.find_element("id","join-form-submit")
buton.click()

time.sleep(500)
# Tarayıcıyı kapat
driver.quit()