import json
from urllib.request import urlopen

json_url='https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'

#使用urlopen
response=urlopen(json_url)
req=response.read()
with open('btc_close_2017_urlopen.json','wb') as f:
    f.write(req)
file_urllib=json.loads(req)
#print(file_urllib)

#使用requests
import requests

req2=requests.get(json_url)
with open('btc_close_2017_requests.json','w') as f:
    f.write(req2.text)
file_requests=req2.json()
print(file_urllib==file_requests)
