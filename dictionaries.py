# dictionaries are similar to list, but in the list we use "numbers" in order to identify the value/string

# List exercise
from __future__ import print_function
from distutils import dir_util
from turtle import circle


list1 = ["R1", "10.1.1.1", "IOS-XE", "aa.bb.cc.dd.ee.ff"]
print(list1)
list1[3] = list1[3].replace(".", ":")
print(list1)
print(type(list1))


#First Way
dict1 = {"Hostname": "R1", "MGMT_IP": "10.1.1.1", "Image": "IOS-XE", "MAC": "aa.bb.cc.dd.ee.ff"}
print(dict1)
print(type(dict1))

print(dict1["MGMT_IP"])
# print(dict1["image"])  case sensitive
print(dict1["Image"])

#Second Way
dict1 = {} #lo lascio vuoto di proposito
dict1["Hostname"] = "R2"
dict1["MGMT_IP"] = "10.2.2.2"
dict1["Image"] = "IOS-XR"
dict1["MAC"] = "11.22.33.44.55.66"
print(dict1)
#{'Hostname': 'R2', 'MGMT_IP': '10.2.2.2', 'Image': 'IOS-XR', 'MAC': '11.22.33.44.55.66'}

# cambiare dict
dict1["MGMT_IP"] = "10.2.2.3"
print(dict1)
#{'Hostname': 'R2', 'MGMT_IP': '10.2.2.3', 'Image': 'IOS-XR', 'MAC': '11.22.33.44.55.66'}

dict1["MGMT_Interface"] = "G0/0/0"
print(dict1)
#{'Hostname': 'R2', 'MGMT_IP': '10.2.2.3', 'Image': 'IOS-XR', 'MAC': '11.22.33.44.55.66', 'MGMT_Interface': 'G0/0/0'}


print(dir(dict1))
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', 
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', 
# '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__',
#  '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
# '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 
# 'setdefault', 'update', 'values']

print(dict1.keys())
# dict_keys(['Hostname', 'MGMT_IP', 'Image', 'MAC', 'MGMT_Interface'])
print(dict1.values())
# dict_values(['R2', '10.2.2.3', 'IOS-XR', '11.22.33.44.55.66', 'G0/0/0'])

dict2 = {} #lo lascio vuoto di proposito
dict2["Hostname"] = "R22"
dict2["MGMT_IP"] = "10.22.22.22"
dict2["Image"] = "IOS-IOS"
dict2["MAC"] = "22.22.22.22.22.22"

print(dict1["Hostname"])
print(dict2["Hostname"])

print(dict1)
#{'Hostname': 'R2', 'MGMT_IP': '10.2.2.3', 'Image': 'IOS-XR', 'MAC': '11.22.33.44.55.66', 'MGMT_Interface': 'G0/0/0'}

dict1.update(dict2)
print(dict1)
#{'Hostname': 'R22', 'MGMT_IP': '10.22.22.22', 'Image': 'IOS-IOS', 'MAC': '22.22.22.22.22.22', 'MGMT_Interface': 'G0/0/0'}

# Se ho delle keys diverse, fa il merge e non sostituisce nulla ovviamente

dict1.pop("Hostname") # Rimuove la key ed il value indicato dal dictionary
print(dict1)
#{'MGMT_IP': '10.22.22.22', 'Image': 'IOS-IOS', 'MAC': '22.22.22.22.22.22', 'MGMT_Interface': 'G0/0/0'}

dict2 = {} #lo lascio vuoto di proposito
dict2["Hostname"] = "R22"
dict2["MGMT_IP"] = "10.22.22.22"
dict2["Image"] = "IOS-IOS"
dict2["MAC"] = "22.22.22.22.22.22"

print(dict2.get("Hostname"))
# Output = R22
print(dict2.get("Hostname2")) #non esiste questa key nel dictionary
# Output = None

print(dict2.get("Hostname2", "This Key name doesn't exists")) #non esiste questa key nel dictionary
# Output = This Key name doesn't exists

print(dict2.get("Hostname", "This Key name doesn't exists"))
# Output = R22



info1 = {"hostname" : "R1", "mgmt-ip" : "10.1.1.1", "username" : "rohit", "password" : "cisc0"}
info2 = {}
info2["hostname"] = "R2"
info2["mgmt-ip"] = "10.1.1.2"
info2["username"] = "rohit"
info2["password"] = "cisco"
info = [info1, info2]
print(info)

