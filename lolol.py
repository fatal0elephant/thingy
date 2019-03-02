import time
import requests
from bs4 import BeautifulSoup
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
for i in range(1,13):
    time.sleep(5)
    url='http://www.tianqihoubao.com/aqi/beijing-2018'+str("%02d"%i)+',html'
    response=requests.get(url=url,headers=headers)
    soup=BeautifulSoup(response.text,'html.parser')
    tr=soup.find_all('tr')
    for j in tr[1:]:
        td=j.find_all('td')
        Date=td[0].get_text().strip()
        Quality_grade=td[1].get_text().strip()
        AQI=td[2].get_text().strip()
        AQI_rank=td[3].get_text().strip()
        PM=td[4].get_text()
        with open('air_beijing_2018.csv','a+',encoding='utf-8-sig') as f:
            f.write(Date+','+Quality_grade+','+AQI+','+AQI_rank+','+PM)
