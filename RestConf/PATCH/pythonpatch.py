import requests

url = "https://192.168.56.107:443/restconf/data/Cisco-IOS-XE-native:native"
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}
auth = ('cisco', 'cisco123!')
data = '{"native": {"logging": {"monitor": {"severity": "informational"}}}}'

response = requests.patch(url, headers=headers, auth=auth, data=data, verify=False)
print(response.text)
