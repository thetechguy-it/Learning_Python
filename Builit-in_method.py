from hashlib import new
from ipaddress import ip_address
from re import I


ip_address = "10.10.10.10"
print(ip_address.startswith("10"))

#Result = True, the variable "ip_address" starts with 10, the output is "True"

ip = "9.9.9.9"
swag = ip.startswith("10")
print(swag)

#Result = False

UPPER_CASE = "RICCARDO NALESSO"
print(UPPER_CASE.lower())
#the same of 
UPPER_CASE = "RICCARDO NALESSO"
lower_case = UPPER_CASE.lower()
print(lower_case)
#print the variable "lower_case", that is the result of "UPPER_CASE" with the lower built-in option

list = UPPER_CASE.split(" ")
print(list[0])
#print RICCARDO
print(list[1])
#print NALESSO


mac_address = "aa.bb.cc.dd.ee.ff"
new_mac_address = mac_address.replace(".", ":")
print("The old MAC address format was:", mac_address)
print(f"The new MAC address format is {new_mac_address}")

# Built-in method explanation: https://www.tutorialsteacher.com/python/string-methods

ip_address = "192.168.2.1" #variable
octect = ip_address.split(".") #create a list from "ip_address"
print(octect)
print(octect[0]) #Print 192, this is the position 0 "zero" of the list
print(octect[1]) #Print 168
print(octect[2]) #Print 2
print(octect[3]) #Print 1


show_run = "conf t\nint g1/0/1\n descr TEST\n no shut"
print(show_run)
#this is the output
#conf t
#int g1/0/1
# descr TEST
# no shut
list_show_run = show_run.split("\n")
print(list_show_run)
#This is the output
#['conf t', 'int g1/0/1', ' descr TEST', ' no shut']
#A list, each line is an entry on the list
list_show_run = show_run.splitlines()
#Should be the same result
print(list_show_run)