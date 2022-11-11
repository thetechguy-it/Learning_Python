from cgitb import enable
from ipaddress import ip_address
from netmiko import ConnectHandler

SSH = ConnectHandler(ip = "10.155.233.201", username = "riccardo", password = "nalesso", secret = "lutech2022", device_type = "cisco_ios")
SSH_Status = SSH.is_alive()
print(SSH_Status)
# Result : True
print(SSH.find_prompt())
# Result: SW1_Automation>
# Our user has Priv0 so we are facing the ">" and not the "#", we need to elevate using the enable command --> .enable() in python
SSH.enable()
print(SSH.find_prompt())
# Result: SW1_Automation#
comands = ["interface loop10", "descr Conf via Python", "ip address 1.1.1.1 255.255.255.255"]
output = SSH.send_config_set(comands)
print(output)
# Result: interface Loopback10
#         description Conf via Python
#         ip address 1.1.1.1 255.255.255.255

SSH.disconnect()
print(SSH.is_alive())
# Result: False
