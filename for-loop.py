routers = ["192.168.10.1", "10.1.1.1", "172.16.20.10", "115.100.10.11"]
interfaces = ["gi0/1", "Gi0/2", "Loopback0", "gi0/3"]

#print("router bgp 64500")
#print("router ospf 100")


for ip in routers:
    print("router ospf 100") 
    print(f"router id {ip}\n")
    for int in interfaces:
        print(f"interface  {int}")
        print("ip ospf 100 area 0\n")