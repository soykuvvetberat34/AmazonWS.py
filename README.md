# Amazon Laptop category web scraping

I scrapyed 4272 product from amazon and I put this data into a dataframe

import requests
from bs4 import BeautifulSoup
import pandas as pd

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
}
i=1
a=1
deger=""
rate=""
fiyat=0
List=[]
while a<=160:
    html=requests.get("https://www.amazon.com.tr/s?i=computers&rh=n%3A12601898031&fs=true&qid=1715593506&ref=sr_pg_"+str(a),headers=headers).text
    soup=BeautifulSoup(html,"html.parser")
    response=soup.find_all("div",{"class":"a-section a-spacing-small puis-padding-left-small puis-padding-right-small"})
    
    a+=1
    for item in response:
        ad=item.find("span",{"class":"a-size-base-plus a-color-base a-text-normal"}).text
       
        try:
            deger=item.find("span",{"class":"a-icon-alt"}).text
            rate=item.find("span",{"class":"a-size-base s-underline-text"}).text
        except:
            print("")
            
        print(f"{i}.ürün")
        print(ad)
        print(rate,deger)
        List.append([ad,rate,deger])
        df=pd.DataFrame(List)
        df.columns=["Ürün detay","Ürün değerlerndirmesi","değerlendiren kişi sayısı"]
        df.to
        
        print("\n")
        i+=1
    
    

![Ekran görüntüsü 2024-05-13 204059](https://github.com/soykuvvetberat34/AmazonWS.py/assets/69586522/04c8c9bb-89d4-4fe0-a20a-e1ccf5b58994)


![Ekran görüntüsü 2024-05-13 204109](https://github.com/soykuvvetberat34/AmazonWS.py/assets/69586522/92856c1c-5d7e-4de1-86cb-297b19a54eaa)



![Ekran görüntüsü 2024-05-13 204140](https://github.com/soykuvvetberat34/AmazonWS.py/assets/69586522/711bc9cd-f04e-4af1-945f-f6ca36a5c597)


![Ekran görüntüsü 2024-05-13 204148](https://github.com/soykuvvetberat34/AmazonWS.py/assets/69586522/957300cc-b064-4770-9a57-ce5ed665ffeb)

![Ekran görüntüsü 2024-05-13 204158](https://github.com/soykuvvetberat34/AmazonWS.py/assets/69586522/1d588586-57bc-4d67-b26b-846bbb115533)

![Ekran görüntüsü 2024-05-13 204204](https://github.com/soykuvvetberat34/AmazonWS.py/assets/69586522/be7690ba-a7b9-4706-be0d-f2b106d1c09d)
