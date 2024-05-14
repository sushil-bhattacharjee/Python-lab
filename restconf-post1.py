import ruamel.yaml as yaml
from rich import print as rprint


def generate_ntp_config():
    ntp_config = yaml.safe_load(open("post-config.yaml"))
    return ntp_config

my_device_configs = generate_ntp_config()
rprint(my_device_configs)