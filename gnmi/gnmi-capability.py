from pygnmi.client import gNMIclient
from rich import print as rprint 

host = ('10.1.10.27', '57400')

with gNMIclient(target=host, username="sushil", password="sushil", insecure=True) as client:
    results = client.capabilities()

rprint(results["supported_models"])