from ncclient import manager
import xml.dom.minidom
from rich import print as rprint

myfilter = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
   <ntp>
    <server xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ntp">
     <server-list>
      <ip-address>10.1.10.101</ip-address>
     </server-list>
    </server>
   </ntp>
  </native>
</config>
"""

myfilter2 = """
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <ntp>
  </ntp>
</native>
"""
myfilter3 = """
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <username>
    <name>bond</name>
    <privilege>15</privilege>
    <secret>
      <encryption>9</encryption>
      <secret>$9$zBTuqLiiX1WKFU$2MPxbHtERq7gyCzNVuUIYR00Oc8yEE4XDcV7wUo.Mxo</secret>
    </secret>
  </username>
</native>
"""

with manager.connect(
    host="10.1.10.30",
    port="830",
    username="admin",
    password="C1sco12345",
    hostkey_verify=False
) as m:
    #netconf_reply = m.edit_config(target="candidate", config=myfilter3, default_operation="merge")
    netconf_reply = m.get_config(source="running", filter=('subtree', myfilter2))
    #prettyresults = xml.dom.minidom.parseString(str(netconf_reply)).toprettyxml()

print(netconf_reply)
#rprint(prettyresults)
