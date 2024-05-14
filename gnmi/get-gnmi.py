from pygnmi.client import gNMIclient
from rich import print as rprint 

#host = ('10.1.10.27', '57400')

with gNMIclient(target=('10.1.10.27', '57400'), username="sushil", password="sushil", insecure=True) as gc:
    results = gc.get(path=["interfaces/interface[name=GigabitEthernet1/0/2]/state/counters/out-multicast-pkts"], encoding="json")

my_data = int(results["notification"][0]["update"][0]["val"])
print(f"The multicast packets = ",my_data)
#rprint(type(results["notification"]))
#rprint(results["notification"][0]["update"][0]["val"])
print(type(my_data))
if my_data > 500:
    print("The multicast packets are above the threshold")
else:
    print("The multicast packets are below the threshold")