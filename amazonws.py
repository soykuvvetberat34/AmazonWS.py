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
    
    



