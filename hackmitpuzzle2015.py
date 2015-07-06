from bs4 import BeautifulSoup
import requests
import math

def print_qr(num):
    num = int(num)
    bn=bin(num)[2:]
    side = int(math.sqrt(len(bn)))
    for x in range(side):
        print(bn.replace('0',' ').replace('1','█')[x*side:x*side+side])

cache = dict()
if False:
    for root in 'abcdefghijklmnopqrstuvwxyz'+'abcdefghijklmnopqrstuvwxyz'.upper():
        fuck_mit = requests.get('http://0xd09eb17e.dogemit.party/p/{}'.format(root))

        fuck_mit_soup = BeautifulSoup(fuck_mit.text)
        the_number = fuck_mit_soup.find('div', {'class':'apples-column'}).find('h1').text
        if len(the_number) > 133:
           print(root, the_number)
           print_qr(the_number)
        cache[root] = the_number
        #print(root, the_number)

    for root in range(250):
        fuck_mit = requests.get('http://0xd09eb17e.dogemit.party/p/{}'.format(root))

        fuck_mit_soup = BeautifulSoup(fuck_mit.text)
        the_number = fuck_mit_soup.find('div', {'class':'apples-column'}).find('h1').text
        if len(the_number) > 133:
           print(root, the_number)
           print_qr(the_number)
        cache[root] = the_number
        #print(root, the_number)
