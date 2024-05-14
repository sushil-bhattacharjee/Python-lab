# Import ConnectHandler class from Netmiko library
from netmiko import ConnectHandler

# Define R3 conection information
R3 = {
    'device_type': 'cisco_xe',
    'host': '10.1.10.53',
    'username': 'sushil',
    'password': 'sushil',
    }

# Start a connection to the router R3
ssh_connection = ConnectHandler(**R3)

# Find the EXEC mode prompt
ssh_connection.find_prompt()

# Send common configuration commands to R3 from file
output = ssh_connection.send_config_from_file('d09_config_xe_common.cfg')
# Display router response to each command
print(output)

# Send core side configuration commands to R3 router from file
output = ssh_connection.send_config_from_file('d09_config_xe_ospf_mpls_ints.cfg')
# Display router response to each command
print(output)

# Send edge side configuration commands to R3 router from file
output = ssh_connection.send_config_from_file('d09_config_xe_vrf_bgp_ospf_ints.cfg')
# Display router response to each command
print(output)
# Close connection
ssh_connection.disconnect

