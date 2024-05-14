from scrapli_netconf import NetconfDriver
from lxml import etree
#search google lxml tree
from io import StringIO

MY_DEVICE = {
    "host": "sandbox-iosxr-1.cisco.com",
    "auth_username": "admin",
    "auth_password": "C1sco12345",
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
#myfilter = "/interfaces-state//statistics[in-unicast-pkts > 6000]/../name" #show the name of interfaces whhich have unicast pkts>6000
#ios-xr doesn't support xpath, therefore it requires to use subtree

myfilter = """
<interfaces xmlns="http://openconfig.net/yang/interfaces">
</interfaces"
"""

response = conn.get(filter_=myfilter, filter_type="subtree")
#print(response.result)

conn.close()

et = etree.parse(StringIO(response.result), parser=etree.HTMLParser(recover=True))
root = et.getroot()

path = root.xpath("//subinterface/ipv4//config")
for element in path:
    print(element.text)
    interface = element.xpath("ancestor::interface/name/text()")[0]
    print(interface)
    for children in element:
        print(f"     {children.text}")