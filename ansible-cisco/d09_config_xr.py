# Import ConnectHandler class from Netmiko library
from netmiko import ConnectHandler

# Define R3 conection information
sandboxXR = {
    'device_type': 'cisco_xr',
    'host': 'sandbox-iosxr-1.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    }

# Start a connection to the router R3
ssh_connection = ConnectHandler(**sandboxXR)

# Find the EXEC mode prompt
ssh_connection.find_prompt()

# Send common configuration commands to R3 from file
#output = ssh_connection.send_config_from_file('d09_config_xe_common.cfg')
# Display router response to each command
#print(output)

# Send core side configuration commands to R3 router from file
output = ssh_connection.send_config_from_file('d09_config_xr_ospf_mpls_intfs.cfg')
# Display router response to each command
print(output)

# Return to global configuration mode
output = ssh_connection.send_config_set(['root'])
print(output)

# Send edge side configuration commands to R3 router from file
output = ssh_connection.send_config_from_file('d09_config_xr_vrf_bgp_ospf_ints.cfg')
# Display router response to each command
print(output)
# Apply Configuration chnages
output = ssh_connection.commit()
# Display router response
print(output)

# Return to EXEC mode
output = ssh_connection.exit_config_mode()
# Display router response
print(output)

# Close connection
ssh_connection.disconnect


