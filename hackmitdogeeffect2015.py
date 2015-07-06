import requests
import random
from bs4 import BeautifulSoup
import time

start_page = 'http://0xd09eeffec7.dogemit.party/'
#start_page = 'http://0xd09eeffec7.dogemit.party/UUUUUUUUUURLDRRDDDDDDDUUUUURLRLUULLDDDDDDDDDUUUUUUUUUURLDDDDDDDDDDUUUUUUUUUURLDDDDDDDDDDUUUUUUUUUURLDRLDUDDDDDDDDDUUUUUUUUUUDRLDUDDUDRLUDUDDDD'
prizes = set()

while True:
    page = requests.get(start_page)
    a=0
    while a<10000:
        try:
            a+=1
            p = BeautifulSoup(page.text)
            game= p.find(id="inner")
            clickables = [x.parent for x in p.find_all('div', {'class':'green box'})]
            prizes.add(p.find('a',{'class':'special'}))
            click = random.choice(clickables)
            page = requests.get('http://0xd09eeffec7.dogemit.party'+click.attrs['href'])
            #print(clickables)
            print(click)
            print(prizes)
            time.sleep(0.2)
        except:
            break
