```py
from selenium import webdriver
import time
# ChromeDriver'ı kullanarak Chrome tarayıcısını başlat
driver = webdriver.Chrome("E:\Python\selenium_instagram\chromedriver.exe")


# Web sayfasını aç
driver.get("https://www.kawin.store")

time.sleep(500)
# Tarayıcıyı kapat
driver.quit()

//////////////////////////////////////////////////////
BeautifulSoup

from bs4 import BeautifulSoup
import requests

# Verileri çekmek istediğiniz URL'yi belirtin
url = "https://www.example.com"

# Web sayfasını alın
response = requests.get(url)

# Web sayfasının içeriğini BeautifulSoup ile analiz edin
soup = BeautifulSoup(response.content, "html.parser")

# Tüm linkleri çıkarmak için <a> etiketlerini bulun
links = soup.find_all("a")

# Elde edilen linkleri döngü ile işleyin ve yazdırın
for link in links:
    print(link.get("href"))

////////////////////////////////////

import xlsxwriter


#URL ALMA VE URL BİÇİMLENDİRME    
#https://www.bol.com/nl/nl/s/?searchtext=laptop                           Bu durumdan 
#https://www.bol.com/nl/nl/s/?page=1&searchtext=laptop&view=list          Bu duruma getirme


workbookyazdirma = xlsxwriter.Workbook("E:\\Python\\Digitalcake\\Bolcom\\bol_guncel_urunler.xlsx")
worksheet = workbookyazdirma.add_worksheet("Bolcomm_Sonuc")
worksheet.write(0,0,"Ürün Adı")
worksheet.write(0,1,"EAN Kodu")
worksheet.write(0,2,"Fiyat")
worksheet.write(0,3,"Nitelik")

        column=0
        worksheet.write(row,column,urun_adi)
        column+=1
        worksheet.write(row,column,urun_ean)
        column+=1
        worksheet.write(row,column,urun_fiyat)


workbookyazdirma.close()
```