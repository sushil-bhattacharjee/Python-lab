#Import ConnectionHandler class from Netmiko library
from netmiko import ConnectHandler

# Define configuration commands as a list
common_config = [
    'logging console debugging',
    'ntp server 10.1.10.100',
]

# Define sandboxXR connection information
sandboxXR = {'device_type': 'cisco_xr', 'host': 'sandbox-iosxr-1.cisco.com', 'username': 'admin', 'password': 'C1sco12345'}
# Start a connection to sandboxXR router
conn = ConnectHandler(**sandboxXR)
# Find the EXEC mode propt
conn.find_prompt()
# Send configuration commands to sandboxXR router
output = conn.send_config_set(common_config)
# Display router response to each command
print(output)
# Apply configuration changes
output = conn.commit
# Display router response
print(output)
# Return to EXEC mode
output = conn.exit_config_mode()
# Display router response
print(output)
# Close connection
conn.disconnect
