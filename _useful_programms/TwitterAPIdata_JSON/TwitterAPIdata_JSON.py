import urllib.request, urllib.parse, urllib.error
import json
import twurl

api_key = 'AIzaSyDJ6x_Zx1tP71ERNQcOm_lh6RBPvJh_P2c'
serviceurl = 'https://api.twitter.com/1.1/friends/list.json'

while True:#why do I need this?
    #acct = input('Enter Twitter Account: ')
    acct = 'drchuck'
    if len(acct) < 1: break
    #parms = dict()
    #parms['address'] = address
    url = twurl.augment(serviceurl,
                        {'screen_name' : acct, 'count' : '5'})
    print('Retrieved',url)
    uh = urllib.request.urlopen(url)
    print('uh',uh)
#uh = connection
    data = uh.read().decode()
    #print('Retrieved', len(data), 'characters')
    headers = dict(uh.getheaders())
    #print('Remaining',headers['x-rate-limit-remaining'])

    try:
        js = json.loads(data)
        print(js)
    except:
        js = None

    #if not js or 'status' not in js or js['status'] != 'OK':
    #    print('FAILUTE TO RETRIEVE->')
    #    print('->not js or status not in js or js[status] != OK:')
    #    print(data)
    #    continue
    #print(data)
    print('json.dumps\n',json.dumps(js, indent=4))#indent 4 very comfortable to read
    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print('  ', s[:50])

#curl -v --compressed -u ruslanshamsnet@gmail.com:Xa5xv9958! "https://gnip-api.twitter.com/search/30day/accounts/<account-name>/prod/counts.json?query=from%3Atwitterdev"
#curl X-POST https://api.twitter.com/1.1/friendships/update.json?user_id=2244994945
#curl --request GET --url 'https://api.twitter.com/1.1/friends/ids.json?screen_name=twitterdev' --header 'authorization: Bearer <bearer>'
#curl --request GET --url 'https://api.twitter.com/1.1/friends/ids.json?screen_name=twitterdev' --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", oauth_nonce="generated-nonce", oauth_signature="generated-signature", oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", oauth_version="1.0"'
#twurl authorize --consumer-key 3nVuSoBZnx6U4vzUxf5w --consumer-secret Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys
