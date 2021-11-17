import urllib.request, urllib.parse, urllib.error
#fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#1: wsl LINUX
        # AttributeError: module 'html5lib.treebuilders' has no attribute '_base'
        # apt-cache madison python3-html5lib
            #it shows only version 1.0-1.2
        # apt-install python3-pip
    #1.1  apt-get install python3-bs4
    #1.2  from bs4 import BeautifulSoup to
    #       import bs4
    #1.3  pip3 uninstall html5lib , pip3 uninstall bs4
#2: cmd WINDOWS
#pip3 install bs4
    #c:\users\1\appdata\roaming\python\python39\site-packages (from bs4)
from bs4 import BeautifulSoup
    #open 1)check local folder libs>#2)check python folder libs>3)check global folder libs>class BeatifulSoup
#fhand = urllib.request.urlopen('http://dr-chuck.com/page1.htm')
#type(fhand) class 'http.cliend.HTTPResponse'
#url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
    # works on http and https ???
    # http://www.dr-chuck.com/page1.htm
html = urllib.request.urlopen(url).read()
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
