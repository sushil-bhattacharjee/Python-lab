import ruamel.yaml as yaml
from rich import print as rprint
import requests
import urllib3

urllib3.disable_warnings()

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

def generate_ntp_config():
    ntp_config = yaml.safe_load(open("post-config.yaml"))
    return ntp_config

def push_config_changes(config_data):
    url = "https://10.1.10.29/restconf/data/Cisco-IOS-XE-native:native/ntp"
    response = requests.put(
        url=url,
        headers=headers,
        json=config_data,
        auth=("sushil", "sushil"),
        verify=False,
    )
    return response

my_device_configs = generate_ntp_config()
rprint(my_device_configs)
results = push_config_changes(my_device_configs)
print(results)