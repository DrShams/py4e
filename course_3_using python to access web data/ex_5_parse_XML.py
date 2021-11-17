#Extracting Data from XML
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#api is AWESOME but i didn't test it yet thank you Mr.Chuck and The Team I want to work with this!)))
serviceurl = 'http://py4e-data.dr-chuck.net/comments_1030209.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

newlist = list()
uh = urllib.request.urlopen(serviceurl, context=ctx)
data = uh.read()
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
for item in lst:#print(type(item))-> <class 'xml.etree.ElementTree.Element'>
    number = item.find('count').text
    newlist.append(int(number))
    sumstr = str(sum(newlist))
print('Sum ends with %s' %(sumstr[-2::]))
#print('Sum=%d' %(sum(newlist)))#->2737
