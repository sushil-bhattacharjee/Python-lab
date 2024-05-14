import requests
from rich import print as rprint

headers = {"Accept": "application/yang-data+json"}
my_url = "https://10.1.10.29/restconf/data/ietf-interfaces:interfaces"

def pull_info(url):
    with requests.Session() as client:
        response = client.get(url, headers=headers, auth=("sushil", "sushil"), verify=False)
        return response.json()
    
results = pull_info(my_url)
rprint(f"This Data ytpe is", type(results))
print()
print()
#rprint(results)

my_interfaces = results["ietf-interfaces:interfaces"]["interface"]
for intf in my_interfaces:
    rprint(intf["name"], intf["ietf-ip:ipv4"])