devices = [{"hostname" : "R1", "MGMT_IP" : "10.1.1.1", "Vendor" : "cisco", "Model" : "CSR1000V"}, {"hostname" : "R2", "MGMT_IP" : "10.1.1.2", "Vendor" : "cisco", "Model" : "CSR1000V"}] # list with inside dictionaries

print(devices[0])
print(devices[0] ["hostname"])

print(devices[0] ["MGMT_IP"])
print(devices[1])
print(devices[1] ["MGMT_IP"])

first_keys = devices[0].keys()
second_values = devices[1].values()
print(first_keys)
print(second_values)


interfaces = [{"interface" : "G1", "ip_address" : "10.5.5.1"}, {"interface" : "G2", "ip_address" : "10.6.6.1"}]
print(interfaces)
devices[0] ["interface"] = interfaces

print(devices)


