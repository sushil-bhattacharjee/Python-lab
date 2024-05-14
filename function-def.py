def send_config(target, cmd):
    print(f"ssh sushil@{target}")
    print('enable')
    print("configure terminal")
    print(cmd)
   
print()
send_config("10.1.10.1", "router bgp 64500")
print()
send_config(cmd="router-id 10.1.10.1", target="10.1.10.1")