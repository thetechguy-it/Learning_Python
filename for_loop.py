devices = ["R1", "R2", "R3", "R4", "FW1"]
print(devices)
# Output ['R1', 'R2', 'R3', 'R4', 'FW1']

print(devices[0])
# Output R1

for item in devices:
    print(item)
    #result:
# R1
# R2
# R3
# R4
# FW1

interfaces  = ["Loop0", "G0/1", "Ten0/1", "Fa0/1", "VLAN100"]
for item in interfaces:
    if item.lower().startswith("g"):
        int_type = "GigabitEthernet"
    elif item.lower().startswith("loop"):
        int_type = "Loopback"
    elif item.lower().startswith("ten"):
        int_type = "TenGigabitEthernet"
    elif item.lower().startswith("fa"):
        int_type = "FastEthernet"
    else:
        int_type = "unknown"
    print(f"The interface type of {item} is {int_type}")



#LAB

dev1 = {"HOSTNAME" : "R1", "OS" : "IOS-XE", "MGMT_IP" : "10.1.1.1"}
dev2 = {"HOSTNAME" : "R2", "OS" : "IOS-XR", "MGMT_IP" : "10.1.1.2"}
dev3 = {"HOSTNAME" : "R3", "OS" : "IOS-XE", "MGMT_IP" : "10.1.1.3"}
dev4 = {"HOSTNAME" : "R4", "OS" : "IOS-XR", "MGMT_IP" : "10.1.1.4"}
dev5 = {"HOSTNAME" : "R5", "OS" : "NEXUS", "MGMT_IP" : "10.1.1.5"}

device_list = [dev1, dev2, dev3, dev4, dev5]

def device_info(os):
    for device in device_list:
        if os in device["OS"] == "IOS-XE":
            print("The management IP of ", device["HOSTNAME"], f"running {os} is ", device["MGMT_IP"])
        elif os in device["OS"] == "IOS-XR":
            print("The management IP of ", device["HOSTNAME"], f"running {os} is ", device["MGMT_IP"])
        elif os in device["OS"] == "NEXUS":
            print("The management IP of ", device["HOSTNAME"], f"running {os} is ", device["MGMT_IP"])
        else:
            pass

print("Devices with IOS-XE as OS")
print(device_info("IOS-XE"))

print("Devices with IOS-XR as OS")
print(device_info("IOS-XR"))

print("Devices with NEXUS as OS")
print(device_info("NEXUS"))