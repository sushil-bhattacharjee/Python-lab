from scrapli_netconf import NetconfDriver

MY_DEVICE = {
    "host": "10.1.10.29",
    "auth_username": "sushil",
    "auth_password": "sushil",
    "auth_strict_key": False
}

conn = NetconfDriver(**MY_DEVICE)
conn.open()
#myfilter = "/native/interface/GigabitEthernet/ip/address/primary"
#myfilter = "//primary"
#myfilter = "//subinterfaces" #by specifying some proper value, it will bring particular module instead of all yang modules
#myfilter = "//address/primary" #by specifying some proper value, it will bring particular module instead of all yang modules
#response = conn.get(filter_=myfilter, filter_type="xpath")
#myfilter = "/interfaces-state//statistics[in-unicast-pkts > 6000]"
myfilter = "/interfaces-state//statistics[in-unicast-pkts > 6000]/../name" #show the name of interfaces whhich have unicast pkts>6000
response = conn.get(filter_=myfilter, filter_type="xpath")
print(response.result)