import requests 
from bs4 import BeautifulSoup 
import csv 
  
URL = "http://www.passiton.com/inspirational-quotes"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 
  
quotes=[]  # a list to store quotes 
  
table = soup.find('div', attrs = {'id':'wrapper'}) 
# print(table)
for row in table.findAll('div', attrs = {'class':'portfolio-image'}): 
    quote = {} 
#     quote['theme'] = row.h5.text 
    quote['url'] = row.a['href'] 
    quote['img'] = row.img['alt'].split('#')[0]
    print("Quote : ",quote['img'])
#     quote['lines'] = row.h6.text 
#     quote['author'] = row.p.text 
    quotes.append(quote) 
for item in quotes:
    print(item)
