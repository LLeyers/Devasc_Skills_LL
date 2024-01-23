import requests

url = "https://192.168.56.107:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"
headers = {'Accept': 'application/yang-data+json'}
auth = ('cisco', 'cisco123!')

response = requests.options(url, headers=headers, auth=auth, verify=False)
print(response.text)
