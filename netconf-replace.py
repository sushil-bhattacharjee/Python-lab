from ncclient import manager

my_config = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
   <ntp operation="replace">
    <server xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ntp">
     <server-list>
      <ip-address>9.9.9.9</ip-address>
     </server-list>
    </server>
   </ntp>
  </native>
</config>
"""

with manager.connect(
    host="10.1.10.29",
    port="830",
    timeout=30,
    username="sushil",
    password="sushil",
    hostkey_verify=False,
) as m:
    results = m.edit_config(target="running", config=my_config, default_operation="none")
    print(results)