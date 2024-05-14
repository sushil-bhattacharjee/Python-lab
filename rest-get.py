import requests
from rich import print as rprint

headers = {"Accept" : "application/yang-data+json"}

url = "https://10.1.10.29/restconf/data/Cisco-IOS-XE-native:native/platform"
response = requests.get(url=url, headers=headers, auth=("sushil", "sushil"), verify=False)

#By default openconfig yang data includes config data as well as state data. 
#To see only the state data ?=nonconfig
#To see only the config data ?=config

url1 = "https://10.1.10.29/restconf/data/openconfig-interfaces:interfaces?content=nonconfig"
response = requests.get(url=url1, headers=headers, auth=("sushil", "sushil"), verify=False)

rprint(response.text)