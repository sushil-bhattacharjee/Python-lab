from ncclient import manager
from rich import print as rprint
import xmltodict
import xml.dom.minidom

myfilter = """
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface></interface>
  </interfaces>
"""
myfilter1 = """
 <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
    <interface>
      <name/>
      <admin-status/>
    </interface>
 </interfaces>
"""

myfilter2 = """
 <ipv4 xmlns="http://openconfig.net/yang/interfaces/ip">
    <addresses>
      <address>
        <ip/>
      </address>
    </addresses>
 </ipv4>
"""
myfilter3 = """
  <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
    <interface>
      <name/>
      <interface-type/>
      <admin-status/>
      <oper-status/>
      <last-change/>
      <if-index/>
      <phys-address/>
    </interface>
  </interfaces>
"""
myfilter4 = """
  <yang-interfaces-cfg-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-yang-interfaces-cfg">
    <acl/>
  </yang-interfaces-cfg-data>
"""
with manager.connect(
    host="10.1.10.29",
    port="830",
    username="admin",
    password="C1sco12345",
    hostkey_verify=False,
) as m:
    #results = m.get_config(source="running", filter= ('subtree', myfilter))
    results = m.get(filter= ('subtree', myfilter3))

pretty_results = xml.dom.minidom.parseString(str(results)).toprettyxml()
print(pretty_results)


# Parse the returned XML to an Ordered Dictionary
#netconf_data = xmltodict.parse(results.xml)["rpc-reply"]["data"]

# Create a list of interfaces
#interfaces = netconf_data["interfaces"]["interface"]


#for interface in interfaces:
# #   print("Interface {} enabled status is {}".format(
#  #          interface["name"],
##   #         interface["enabled"]
#    #        )
#    )