from cgitb import enable
from ipaddress import ip_address
from netmiko import ConnectHandler

SSH = ConnectHandler(ip = "10.155.233.201", username = "riccardo", password = "nalesso", secret = "lutech2022", device_type = "cisco_ios")
SSH_Status = SSH.is_alive()
print(SSH_Status)
# Result : True
print(SSH.find_prompt())
# Result: SW1_Automation>
# Essendo che il "line con0" sullo switch è settato con Priv 0, entro in ">" mode, per elevarmi ad exec mode devo dare .enable()
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