from ncclient import manager

my_config = """
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

with manager.connect(
    host="10.1.10.30",
    port="830",
    username="admin",
    password="C1sco12345",
    hostkey_verify=False,
) as m:
    results = m.edit_config(target="running", config=my_config, default_operation="merge")
    

print(results)