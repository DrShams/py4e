import urllib.request, urllib.parse, urllib.error, json
url = 'http://ip-api.com/line/?fields=8192'
myrequest = 'http://ip-api.com/json/'+str(urllib.request.urlopen(url).read().decode("UTF-8"))
json_object = json.loads(urllib.request.urlopen(myrequest).read().decode("UTF-8"))
json_formatted_str = json.dumps(json_object, indent=2)
print('Hello world, there is my handshake:\n',json_formatted_str)
#my first programm
