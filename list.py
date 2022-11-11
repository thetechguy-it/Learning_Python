router = "csr1000v"
type(router)
# The result is "class 'str' " because it is a string

version = 16.7
type(version)
# The result is "class 'float' " because it is a float number

description = "This router is a"


info = ["Hello", router, 10, version, description, "end of the test"]
type(info)

# The result is "class 'list' " because it is a list of something

print(info[0])
print(info[5])
print(info[1])
print(info[4])
print(info[2])
print(info[3])
# the result is
#Hello
#end of the test
#csr1000v
#This router is a
#10
#16.7
info = ["Hello", router, 10, version, description, "end of the test"]

print(info[2:])
# It prints everything FROM the third (number 2) element of the list
# [10, 16.7, 'This router is a', 'end of the test']

print(info[1:3])
# It prints everything from the second (number 1) element of the list to the second number -1 (numero scritto escluso, quindi fino al 2)

interface1 = ["description Configured by Python", "switchport mode access", "switchport access vlan 10"]
# This is a list with 3 string variable
print(interface1)

print(dir(interface1))

# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


interface1.append("no shut") #adding "no shut" at the end of the list
print(interface1) # Result ['description Configured by Python', 'switchport mode access', 'switchport access vlan 10', 'no shut']

interface1.insert(1, "duplex full")
print(interface1) # Result  ['description Configured by Python', 'duplex full', 'switchport mode access', 'switchport access vlan 10', 'no shut']


print(interface1.count("no shut"))
#how many "no shut" there are into the list? 1

basic = ["conf t", "int g0/0/1"]

print(basic)
print(interface1)
#I want to combine list BASIC with list INTERFACE1
basic.extend(interface1)
print(interface1) #the same
print(basic) #basic + interface1

vlans = [20, 39, 44, 65, 22, 19 ,1]
print(vlans)
vlans.sort() #mette in ordine numerico
print(vlans)

# before [20, 39, 44, 65, 22, 19, 1]
# after [1, 19, 20, 22, 39, 44, 65]

print(basic)
# ['conf t', 'int g0/0/1', 'description Configured by Python', 'duplex full', 'switchport mode access', 'switchport access vlan 10', 'no shut']
# i want to change the "int g0/0/1" with "int fa0/0/1"

basic[1] = "int fa0/0/1" 
print(basic)


#LAB TASK
ip_address = "10.1.5.5"
interface = "G0/0/0/0"
list = [interface, ip_address, "descriptio connected via Python", "shut"]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list)
list[3] = "no shut"
print(list)
print("The IP address of the router is", list[1], "and the management interface is", list[0])


# List exercise
list1 = ["R1", "10.1.1.1", "IOS-XE", "aa.bb.cc.dd.ee.ff"]
print(list1)
list1[3] = list1[3].replace(".", ":")
print(list1)