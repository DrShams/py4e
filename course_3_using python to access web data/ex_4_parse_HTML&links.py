import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

url = input('Enter URL:')
if url== 'http://py4e-data.dr-chuck.net/known_by_Fikret.html':
    hops = 4
    maxpos = 3
else:
    hops = 7
    maxpos = 18
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Kyran.html'
for hop in range(hops):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')#Retrieve all of the anchor tags
    tags = soup('a')#<a>pull all info inside tags</a>
    i = 0
    for tag in tags:#type(tag) = bs4.element.Tag
        i+=1#count lines
        if i == maxpos:
            url = (tag.get('href',None))#href="take_this_to_string"
            link_wn = re.findall('known_by_([\w]*)',url)
            break#only first loop
    #print(hop)
print(link_wn[0])#the last name after last hop
