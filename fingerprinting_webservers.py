#!/usr/bin/python3
import requests

//use the target url
req = requests.get('http://10.0.3.8')
headers = ['Server', 'Date', 'Via', 'X-Powered-By', 'X-Country-Code']
for header in headers:
    try:
        result = req.headers[header]
        print('%s: %s' % (header, result))
    except:
        print ('%s: Not found' % header)
