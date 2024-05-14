import yaml
from rich import print as rprint

inventory_data = yaml.safe_load(open("examp2.yml"))
rprint(f"Total inventory data", inventory_data)
print()
rprint(f"R1", inventory_data["R1"])
print()
rprint(f"R1 hostname\n", inventory_data["R1"]["hostname"])
print("\n")
rprint(f"R2 group\n", inventory_data["R2"]["group"])
print()

list_of_groups_R2 = inventory_data["R2"]["group"]
for item in list_of_groups_R2:
    print(item)

print()
config_data = yaml.safe_load(open("examp-yml1.yaml"))
#rprint(config_data)

print()
peer_asns = config_data["BGP"]["peers"]
#neighbor = peer_asn["neighbor"]
for peer in peer_asns:
    result1 = peer["neighbor"]
    result2 = peer["peer_asn"]
    #print(peer ["neighbor"])
    #print(peer["peer_asn"])
    #results = peer["neighbor"] + peer["peer_asn"]
    print(f"neighbor {result1} remote-as {result2}")

print()
