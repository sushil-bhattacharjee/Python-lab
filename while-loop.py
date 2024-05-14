support_devices = ["cisco", "juniper", "hp", "ciena"]
platform_choice = input("Enter the platform name: ")

while platform_choice not in support_devices:
    print("Sorry not supported devices")
    platform_choice = input("Try again. Use a supported devices: ")

print("Great! We got supported devices")