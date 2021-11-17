import urllib.request, urllib.parse, urllib.error
import json
#import xml.etree.ElementTree as ET
#import ssl
    # Ignore SSL certificate errors
    #ctx = ssl.create_default_context()
    #ctx.check_hostname = False
    #ctx.verify_mode = ssl.CERT_NONE

api_key = True
    # If you have a Google Places API key, enter it here
api_key = 'AIzaSyDJ6x_Zx1tP71ERNQcOm_lh6RBPvJh_P2c'
    # https://developers.google.com/maps/documentation/geocoding/intro
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
#old#serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'
while True:#why do I need this?
    address = input('Enter location: ')
    if len(address) < 1: break
    #parms = dict()
    #parms['address'] = address
    url = serviceurl + urllib.parse.urlencode({'address' : address})
    url = url + '&' + urllib.parse.urlencode({'key' : api_key})
#old#url = serviceurl + urllib.parse.urlencode(parms)
    #urlencode(parms) divide parms into 'key1=value1' + & 'key2=value2'
        #parms['address'] = Ufa
        #parms['key'] = api_key
    print('Retrieved',url)
    uh = urllib.request.urlopen(url)
#old#uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None

#if api_key is not False: parms['key'] = api_key
#print('Retrieving', url)
    if not js or 'status' not in js or js['status'] != 'OK':
        print('FAILUTE TO RETRIEVE->')
        print('->not js or status not in js or js[status] != OK:')
        print(data)
        continue
    #print(data)
    print('json.dumps\n',json.dumps(js, indent=4))#indent 4 very comfortable to read
        #dict->
            #->list->
                #->dict->
                    #->keys
#old#tree = ET.fromstring(data)
    #results = tree.findall('result')
    location = js["results"][0]["geometry"]["location"]
        #if I type js["results" without ']'
            #SyntaxError: invalid syntax
#old#location = results[0].find('geometry').find('location')
    lat = location["lat"]
#old#lat = location.find('lat').text
    lng = location["lng"]
#old#lng = location.find('lng').text
    location_addr = js['results'][0]['formatted_address']
#old#location_addr = results[0].find('formatted_address').text
    print('lat', lat, 'lng', lng)
    print(location_addr)
