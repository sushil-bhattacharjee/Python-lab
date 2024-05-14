import requests
from collections import OrderedDict

BASE_URL = "https://10.1.10.29/restconf"  # replace with your base url
USERNAME = "sushil"  # replace with your username
PASSWORD = "sushil"  # replace with your password
HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

def configure_ip_address(interface, ip, length):
    url = BASE_URL + f"/data/ietf-interfaces:interfaces/interface={interface}"
    
    data = {
        "ietf-interfaces:interface": {
            "name": interface,
            "type": "iana-if-type:ethernetCsmacd",
            "ietf-ip:ipv6": {
                "address": [
                    {
                        "ip": ip,
                        "prefix-length": length
                    }
                ]
            }
        }
    }

    response = requests.put(url, auth=(USERNAME, PASSWORD), headers=HEADERS, verify=False, json=data)
    print(response.status_code)

configure_ip_address("GigabitEthernet4", "2001:db8:636c:6179:2063:7572:7469:7300", 64)
