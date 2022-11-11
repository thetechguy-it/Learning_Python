from ipaddress import ip_address


ccie = "CCIE EI\nCCIE SP\nCCIE SEC"
ip_address1 = "10.1.2.100"
ip_address2 = "10.3.4.200"
lower_ccie = ccie.lower()
new_ip_address1 = ip_address1.split(".")
new_ip_address2 = ip_address2.split(".")
new_lower_ccie = lower_ccie.splitlines()
print(new_ip_address1[2])
print(new_ip_address2[3])
print(new_lower_ccie)


ccie1 = "CCIE Enterprise Infrastructure"
no_of_ccie = 25000
total_ei = f"There are {no_of_ccie} {ccie1} in the world"
print(total_ei)

ccie2 = "CCIE Security"
no_of_sec = 15000
total_sec = "There are {} {} in the world"
print(total_sec.format(no_of_sec, ccie2))
#I can call multiple variables, it is more scalable that the "format string" (f"string") 


ip_address1 = "10.1.5.5"
temp_ip_address = ip_address1.replace("5", "2") #Replace all the 5 with 2
print(temp_ip_address)
new_ip_address = temp_ip_address.replace("2", "100", 1) #Replace the first 2 with 100
print(new_ip_address)
csr_ip_address = "The IP address of the gateway router is {}"
print(csr_ip_address.format(new_ip_address))