#Scraping Numbers from HTML using BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

url = input('Enter URL:')
test = False
if url == 'http://py4e-data.dr-chuck.net/comments_42.html':
    test = True
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1030207.html'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')#Retrieve all of the anchor tags
tags = soup('span')#pull all info inside and with tags <span> </span>

newlist = list()
for tag in tags:#type(tag) = bs4.element.Tag
    newline = str(tag)
    link_wn = re.findall('([0-9]+)',newline)#at least one number or more
    print(link_wn[0])#it works only if each line has only 1 number. Use loops for different
    newlist.append(int(link_wn[0]))
totalsum = sum(newlist)
if test == True:
    print('Sum=%d' %(totalsum))
else:
    print('Sum ends with',str(totalsum)[-2::])#output just last 2 numbers
    #Sum=2274
