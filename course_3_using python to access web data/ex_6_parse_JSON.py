import urllib.request, urllib.parse, urllib.error
import json

#url = 'http://py4e-data.dr-chuck.net/comments_42.json'
url = 'http://py4e-data.dr-chuck.net/comments_1030210.json'

uh = urllib.request.urlopen(url)
data = uh.read().decode()
try:
    js = json.loads(data)["comments"]#class list (inside dict)
except:
    js = None
listsum = list()
if js is not None:
    for u in js:
        listsum.append(u['count'])
#print('Sum=%d' %(sum(listsum)))
print('Sum ends with %s' %(str(sum(listsum))[-2::]))
