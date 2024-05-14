from ncclient import manager
import xmltodict
import xml.dom.minidom
from rich import print as rprint


myfilter1 = """
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
</native>
"""

myfilter2 = """
<interfaces xmlns="http://openconfig.net/yang/interfaces">
</interfaces>
"""
myfilter3 = """
 <ethernet xmlns="http://openconfig.net/yang/interfaces/ethernet">
    <config>mac-address</config>
 </ethernet>
"""
with manager.connect(
    host="10.1.10.29",
    username="admin",
    password="C1sco12345",
    port="830",
    hostkey_verify=False,
) as m:
  # For the next command it requires few spaces (identation) since the session is open
    results = m.get(filter=('subtree', myfilter2))

pretty_results = xml.dom.minidom.parseString(str(results)).toprettyxml()

rprint(pretty_results)





#my_device = manager.connect(
#           host="10.1.10.29",
#           username="admin",
#           password="C1sco12345",
#           port="830",
#           hostkey_verify=False
#)

#for capability in my_device.server_capabilities:
#    print(capability)

#my_device.close_session()