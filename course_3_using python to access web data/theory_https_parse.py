import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
    # http://www.dr-chuck.com/page1.htm
html = urllib.request.urlopen(url, context=ctx).read()
    #html one line with </h><p>\n dirty code
soup = BeautifulSoup(html, 'html.parser')
#soup many lines as it was in website with </h><p> without \n tags
#Retrieve all of the anchor tags
tags = soup('a')
    #pull all info inside and with tags <p> </p>
for tag in tags:
    print(tag.get('href',None))
        #[<a href="http://www.dr-chuck.com/page2.htm">Second Page</a>]
            #http://www.dr-chuck.com/page2.htm
#counts = dict()
#for line in fhand:
    #words = line.decode().split()
    #print(words)
    #for word in words:
        #counts[word] = counts.get(word, 0) + 1
#print(counts)
    #print the words in the order of the text goes
    #skip the words that repeated on the second time
