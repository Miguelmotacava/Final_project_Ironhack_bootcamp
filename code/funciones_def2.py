
#funciones

import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
import selenium 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
PATH=ChromeDriverManager().install(); 
opciones=Options()
driver=webdriver.Chrome(PATH);
driver.quit()
import warnings
warnings.filterwarnings('ignore')



def datac(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    html = req.get(url, headers).text
    soup=bs(html, 'html.parser')
    body = soup.find_all('tr', class_='table-row')
    titles = [i.find_all('td') for i in body]
    
    a = [j for i in titles for j in i]
    b=[a[i] for i in range(4,len(a),16)]
    lst=[]
    for i in b:
        a = str(i).replace(' ','').split('>\n')[1].split('</')[0]
        if a == '':
            a = '0'
            lst.append(a)
        else:
            a = a.split('\n')[0]
            lst.append(a)
    precios = []
    for i in lst:
            if 'K' in i or 'k' in i:
                precios.append(float(i.replace('K',''))*1000)
            elif 'M' in i:
                precios.append(float(i.replace('M',''))*1000000)
            elif '0' in i:
                precios.append(float(i))
    
    
    c = [i.find_all('a') for i in body]
    d = [j for i in c for j in i]
    names = [str(d[i]).split('<b>')[1].split('</b>')[0] for i in range(2,len(d),7)]
    
    stats = soup.find_all('span', class_='stat')
    pac= [stats[i].text for i in range(0,len(stats),6)]
    sho = [stats[i].text for i in range(1,len(stats),6)]
    pas = [stats[i].text for i in range(2,len(stats),6)]
    dri = [stats[i].text for i in range(3,len(stats),6)]
    defe = [stats[i].text for i in range(4,len(stats),6)]
    phy = [stats[i].text for i in range(5,len(stats),6)]
    
    stars = soup.find_all('span', class_='starRating')
    stars_def = [str(i.text).split('\n\n')[1].split('\n')[0] for i in stars]
    star1 = [stars_def[i] for i in range(0,len(stars_def),2)]
    star = [i.replace(' ','') if len(i)==2 else i for i in star1]     
    wstar1 = [stars_def[i] for i in range(1,len(stars_def),2)]
    wstar = [i.replace(' ','') if len(i)==2 else i for i in wstar1]  
    
    div = soup.find_all('div')
    other_pos = [i.text for i in soup.find_all(attrs={"style" : "font-size:12px;"})][-25:]
    
    foot = soup.find_all('td')
    foots = [foot[i].text.split('\n')[1].split('\n')[0] for i in range(30, len(foot), 16)]
    igs = [foot[i].text.split('\n')[1].split('\n')[0] for i in range(31, len(foot), 16)]
    
    a = [j for i in titles for j in i]
    tipe = [i.find_all('a') for i in a]
    tipe2 = [j for i in tipe for j in i]
    tipo = [str(tipe2[i]).split('">')[1].split('</')[0] for i in range(3 ,len(tipe2), 5)]

    plat = ['console' for i in range(len(names))]
    
    ab = [i.text for i in soup.find_all('a')]
    aa = [ab[i] for i in range(len(ab)-len(names*7)-22, len(ab)-24)]
    team = [aa[i] for i in range(2, len(aa), 7)]
    liga = [aa[i] for i in range(3, len(aa), 7)]
    
    src = soup.find_all('img')
    imgs = [j for i in src for j in i]
    url = soup.find_all('img')
    ur = [url[i] for i in range(874,len(url)-81)]
    
    caras_url = ['https://www.futwiz.com'+str(ur[i]).split('src="')[1].split('"/>')[0] for i in range(0, len(ur),4)]
    club_url = ['https://www.futwiz.com'+str(ur[i]).split('src="')[1].split('"/>')[0] for i in range(1, len(ur),4)]
    flags_url = ['https://www.futwiz.com'+str(ur[i]).split('src="')[1].split('"/>')[0] for i in range(2, len(ur),4)]
    
    init = soup.find_all('a')
    med = [j.text for i in init for j in i]
        
    stats = [i for i in med if i.isnumeric()==True]
    
    tip = [i for i in soup.find_all('div') if 'otherversion23' in str(i)]
    tipo = [str(tip[i]).split('otherversion23-')[1].split('">')[0] for i in range(5, len(tip),2)]
    
    posi =soup.find_all('b')
    pos = [i.text for i in soup.find_all('b') if i.text in ['GK', 'RB', 'RWB', 'CB', 'LB', 'LWB', 'CDM', 'CM', 'CAM', 'RM', 'RW', 'LM', 'LW', 'RF', 'CF', 'LF', 'ST']]
    
    ada = soup.find_all('span', class_='wrs')
    da = [str(i.text).split('\n')[1].split(' ')[0] for i in ada]
    
    dic = {'names':names, 'pos': pos, 'pos_sec':other_pos, 'version':tipo, 'price':precios, 'med': stats, 'pac':pac, 'sho':sho, 'pas':pas, 'dri':dri, 'def':defe, 'phy':phy, 'S/M':star, 'W/F':wstar, 'foot':foots, 'igs':igs, 'att/def_average':da, 'equipo':team, 'liga':liga, 'face_url':caras_url, 'flags_url':flags_url, 'club_url':club_url}
    
    return dic

def scrap_precios_console(url):
    import requests as req
    from bs4 import BeautifulSoup as bs
    import pandas as pd
    import pandas as pd
    import time
    import warnings
    warnings.filterwarnings('ignore')
    
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"}

    html = req.get(url, headers).text
    soup=bs(html, 'html.parser')
    body = soup.find_all('tr', class_='table-row')
    titles = [i.find_all('td') for i in body]
    
    a = [j for i in titles for j in i]
    b=[a[i] for i in range(4,len(a),16)]
    lst=[]
    for i in b:
        a = str(i).replace(' ','').split('>\n')[1].split('</')[0]
        if a == '':
            a = '0'
            lst.append(a)
        else:
            a = a.split('\n')[0]
            lst.append(a)
    precios = []
    for i in lst:
            if 'K' in i or 'k' in i:
                precios.append(float(i.replace('K',''))*1000)
            elif 'M' in i:
                precios.append(float(i.replace('M',''))*1000000)
            elif '0' in i:
                precios.append(float(i))

    c = [i.find_all('a') for i in body]
    d = [j for i in c for j in i]
    names = [str(d[i]).split('<b>')[1].split('</b>')[0] for i in range(2,len(d),7)]
    
    stats = soup.find_all('span', class_='stat')
    pac= [stats[i].text for i in range(0,len(stats),6)]
    sho = [stats[i].text for i in range(1,len(stats),6)]
    pas = [stats[i].text for i in range(2,len(stats),6)]
    dri = [stats[i].text for i in range(3,len(stats),6)]
    defe = [stats[i].text for i in range(4,len(stats),6)]
    phy = [stats[i].text for i in range(5,len(stats),6)]
    
    stars = soup.find_all('span', class_='starRating')
    stars_def = [str(i.text).split('\n\n')[1].split('\n')[0] for i in stars]
    star1 = [stars_def[i] for i in range(0,len(stars_def),2)]
    star = [i.replace(' ','') if len(i)==2 else i for i in star1]     
    wstar1 = [stars_def[i] for i in range(1,len(stars_def),2)]
    wstar = [i.replace(' ','') if len(i)==2 else i for i in wstar1]  
    
    div = soup.find_all('div')
    other_pos = [i.text for i in soup.find_all(attrs={"style" : "font-size:12px;"})][-25:]
    
    foot = soup.find_all('td')
    foots = [foot[i].text.split('\n')[1].split('\n')[0] for i in range(30, len(foot), 16)]
    igs = [foot[i].text.split('\n')[1].split('\n')[0] for i in range(31, len(foot), 16)]
    
    ab = [i.text for i in soup.find_all('a')]
    aa = [ab[i] for i in range(len(ab)-len(names*7)-22, len(ab)-24)]
    team = [aa[i] for i in range(2, len(aa), 7)]
    liga = [aa[i] for i in range(3, len(aa), 7)]
    
    tip = [i for i in soup.find_all('div') if 'otherversion23' in str(i)]
    tipo = [str(tip[i]).split('otherversion23-')[1].split('">')[0] for i in range(5, len(tip),2)]
    
    posi =soup.find_all('b')
    pos = [i.text for i in soup.find_all('b') if i.text in ['GK', 'RB', 'RWB', 'CB', 'LB', 'LWB', 'CDM', 'CM', 'CAM', 'RM', 'RW', 'LM', 'LW', 'RF', 'CF', 'LF', 'ST']]
    
    ada = soup.find_all('span', class_='wrs')
    da = [str(i.text).split('\n')[1].split(' ')[0] for i in ada]
    
    dic = {'names':names, 'pos': pos, 'pos_sec':other_pos, 'version':tipo, 'price':precios, 'med': stats, 'pac':pac, 'sho':sho, 'pas':pas, 'dri':dri, 'def':defe, 'phy':phy, 'S/M':star, 'W/F':wstar, 'foot':foots, 'igs':igs, 'att/def_average':da, 'equipo':team, 'liga':liga}
    
    return dic
    
def scrap_precios_console2(url):
    import requests as req
    from bs4 import BeautifulSoup as bs
    import pandas as pd
    import pandas as pd
    import time
    import warnings
    warnings.filterwarnings('ignore')
    
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"}

    html = req.get(url, headers).text
    soup=bs(html, 'html.parser')
    body = soup.find_all('tr', class_='table-row')
    titles = [i.find_all('td') for i in body]
    
    a = [j for i in titles for j in i]
    b=[a[i] for i in range(4,len(a),16)]
    lst=[]
    for i in b:
        a = str(i).replace(' ','').split('>\n')[1].split('</')[0]
        if a == '':
            a = '0'
            lst.append(a)
        else:
            a = a.split('\n')[0]
            lst.append(a)
    precios = []
    for i in lst:
            if 'K' in i or 'k' in i:
                precios.append(float(i.replace('K',''))*1000)
            elif 'M' in i:
                precios.append(float(i.replace('M',''))*1000000)
            elif '0' in i:
                precios.append(float(i))

    c = [i.find_all('a') for i in body]
    d = [j for i in c for j in i]
    names = [str(d[i]).split('<b>')[1].split('</b>')[0] for i in range(2,len(d),7)]
    
    a = [j for i in titles for j in i]
    tipe = [i.find_all('a') for i in a]
    tipe2 = [j for i in tipe for j in i]
    tipo = [str(tipe2[i]).split('">')[1].split('</')[0] for i in range(3 ,len(tipe2), 5)]
    
    tip = [i for i in soup.find_all('div') if 'otherversion23' in str(i)]
    tipo = [str(tip[i]).split('otherversion23-')[1].split('">')[0] for i in range(5, len(tip),2)]

    times = [time.asctime() for i in range(len(names))]
    
    plat = ['console' for i in range(len(names))]
    
    init = soup.find_all('a')
    med = [j.text for i in init for j in i]
        
    stats = [i for i in med if i.isnumeric()==True]
    
    dic = {'names':names, 'med':stats, 'type':tipo, 'price':precios, 'time':times, 'platform':plat}
    
    return dic

