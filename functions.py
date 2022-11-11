from ast import IfExp
from distutils.errors import DistutilsClassError


def vlan_exist(vlan):      #vlan è una variabile temporanea, il mio input
    vlans_on_switch = [10, 20, 30, 40, 50, 60]
    return vlan in vlans_on_switch
print(vlan_exist(10)) #dentro la parentesi metto un input io

# Result = "True"

def vlan_info(id, name):
    print(f"The VLAN ID is {id} and the VLAN name is {name}")

print(vlan_info("10","MGMT"))
# The VLAN ID is 10 and the VLAN name is MGMT
# Il trick è quello di ottenere valori dinamici e richiamare le funzione, che non cambia


def intf(interface, speed = "1000", duplex = "full"):
    print(f"The interface of the router is {interface}")
    print(f"The speed of the interface is {speed}")
    print(f"The duplex of the interface is {duplex}")
print(intf("Gi0/1", "2000", "half"))
# Output 
# The interface of the router is Gi0/1
# The speed of the interface is 2000
# The duplex of the interface is half

# Se non specifico niente per i valori già messi staticamente dentro la funzione
print(intf("Gi0/1"))
# Output is:
# The interface of the router is Gi0/1
# The speed of the interface is 1000
# The duplex of the interface is full




def get_ip(temp):
    dict1 = {"hostname" : "R1", "os" : "IOS-XR", "mgmt_ip" : "10.1.1.1"}
    if temp in dict1["os"]:
        print(dict1["mgmt_ip"])
    else:
        print(f"The device is not running {temp}")

print(get_ip("IOS-XR"))
# result:
# 10.1.1.1
print(get_ip("IOS-XE"))
# result:
# The device is not running IOS-XE



# LAB
print("START LAB")

def device_ip(temp):
    dict1 = {"hostname" : "R1", "OS" : "IOS-XE", "mgmt_ip" : "10.1.1.1"}
    dict2 = {"hostname" : "R2", "OS" : "IOS-XR", "mgmt_ip" : "10.1.1.2"}
    if temp in dict1["OS"] == "IOS-XE":
        print("The management IP of ", dict1["hostname"], "is ", dict1["mgmt_ip"])
    elif temp in dict2["OS"] == "IOS-XR":
        print("The management IP of ", dict2["hostname"], "is ", dict2["mgmt_ip"])
    else:
        print("The device has an unknown image")

print(device_ip("IOS-XR"))
print(device_ip("IOS-XE"))
print(device_ip("PIPPO"))