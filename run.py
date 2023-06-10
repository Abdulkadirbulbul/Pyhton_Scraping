import requests
from bs4 import BeautifulSoup
import xlsxwriter



workbookyazdirma = xlsxwriter.Workbook("C:\\Users\\Kadir\\Desktop\\fu_web\\urunler.xlsx")
worksheet = workbookyazdirma.add_worksheet("Bolcomm_Sonuc")
worksheet.write(0,0,"Ürün Adı")
worksheet.write(0,1,"Ürün Markası")
worksheet.write(0,2,"Fiyat")
worksheet.write(0,3,"Görsel")

row=1

#sekmelere gitme
for i in range(1,10):
    kok="https://www.bol.com"
    url="https://www.bol.com/nl/nl/l/keyboards/43441/?page="+str(i)
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"html.parser")
    liste=soup.find("ul",{"id":"js_items_content"})
    urun_linki=liste.find_all("a",{"data-test":"product-title"})
    
    #urunlere gitme
    for link in urun_linki:
        tek_urun_linki=kok+link.get("href")
        response=requests.get(tek_urun_linki)
        soup=BeautifulSoup(response.content,"html.parser")

        urun_adi=soup.find("span",{"data-test":"title"})
        urun_marka=soup.find("a",{"data-role":"BRAND"})
        urun_marka=urun_marka.text.strip()
        urun_fiyat=soup.find("span",{"data-test":"price"}).text.split()
        urun_fiyat=str(urun_fiyat[0])+"."+str(urun_fiyat[1])
        urun_fiyat=urun_fiyat.split(".-")[0]
        urun_aciklama=soup.find("div",{"data-test":"product-description"})
        urun_gorsel=soup.find("img",{"data-test":"product-main-image"}).get("src")

        print(urun_adi.text)
        print(urun_marka)
        print(urun_fiyat)
        #print(urun_aciklama)
        print(urun_gorsel)
        print()

        # excel yazdırma
        column=0
        worksheet.write(row,column,str(urun_adi))
        column+=1
        worksheet.write(row,column,str(urun_marka))
        column+=1
        worksheet.write(row,column,str(urun_fiyat))
        column+=1
        worksheet.write(row,column,str(urun_gorsel))
        row=row+1

        #görsel indirme
        def gorsele_indirme():
            

            dosya_adı ="gorseller\\"+str(row-1)+ ".jpg" 
            print(dosya_adı) 
            # İndirilen görselin kaydedileceği dosya adı

            response = requests.get(str(urun_gorsel))
        
            with open(str(dosya_adı), 'wb') as f:
                f.write(response.content)
            print("Görsel indirildi.")
        
        gorsele_indirme()

workbookyazdirma.close()

    

