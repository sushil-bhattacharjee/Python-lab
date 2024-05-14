my_interfaces = ["FastEthernet1", "GigabitEthernet1", "FasttEthernet2", "GigabitEthernet2", "Loopback0", "Loopback1"]
print()
for intf in my_interfaces:
    if intf.startswith("Fast"):
        print(f"interface {intf}")
        print("This is a FastEthernet interface\n")
    elif intf.startswith("Giga"):
        print(f"interface {intf}")
        print("This is a Gigabit Ethernet\n")
    else:
        print(f"interface {intf}")
        print("This is a Loopback interface\n")
