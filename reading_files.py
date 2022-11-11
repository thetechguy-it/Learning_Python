from asyncore import write
import os
print(os.getcwd())
print(os.listdir())
# Se linux
# os.system("cat test.txt")

config = open("test.txt", "r") # crea una variabile temporanea (<class '_io.TextIOWrapper'>), è da convertire subito in una variabile nostra. Ogni volta che richiamo una variabile temporanea, al primo colpo scompare e devo richiamare il file
print(config.read())
print(type(config))
config = open("test.txt", "r")
python_learn = config.read()
print(python_learn)


#Creare un file, in scrittura, e riportare dentro il contenuto dei dictionary all'interno della list

vlans1 = [{"id" : "10","name" : "DATA"}, {"id" : "20","name" : "VOICE"}, {"id" : "30","name" : "MGMT"}]
print(vlans1)
modify_vlans1 = open("vlans1.txt", "w")
modify_vlans1.write("vlan " + vlans1[0]["id"] + "\n")
modify_vlans1.write("name " + vlans1[0]["name"] + "\n")

modify_vlans1.write("vlan " + vlans1[1]["id"] + "\n")
modify_vlans1.write("name " + vlans1[1]["name"] + "\n")

modify_vlans1.write("vlan " + vlans1[2]["id"] + "\n")
modify_vlans1.write("name " + vlans1[2]["name"] + "\n")
modify_vlans1.close()

print(os.getcwd())


vlans2 = [{"id" : "40","name" : "DATAAAA"}, {"id" : "50","name" : "VOICEEEEE"}, {"id" : "60","name" : "MGMTTTTTT"}]
print(vlans2)
with open("vlans2.txt" , "w") as modify_vlans2:
    modify_vlans2.write("vlan " + vlans2[0]["id"] + "\n")
    modify_vlans2.write("vlan " + vlans2[0]["name"] + "\n")
    modify_vlans2.write("vlan " + vlans2[1]["id"] + "\n")
    modify_vlans2.write("vlan " + vlans2[1]["name"] + "\n")
    modify_vlans2.write("vlan " + vlans2[2]["id"] + "\n")
    modify_vlans2.write("vlan " + vlans2[2]["name"] + "\n")



intf = [{"int" : "interface", "name" : "G0/0"}, {"int" : "interface", "name" : "G0/1"}, {"int" : "interface", "name" : "G0/2"}, {"descr" : "description", "name" : "Connected via Python"}, {"cmd" : "no", "status" : "shut"}]
with open("r1_interfaces.txt", "w") as modify_intf:
    modify_intf.write(intf[0]["int"] + " " + intf[0]["name"] + "\n")
    modify_intf.write(intf[3]["descr"] + " " + intf[3]["name"] + "\n")
    modify_intf.write(intf[4]["cmd"] + " " + intf[4]["status"] + "\n\n")
    modify_intf.write(intf[1]["int"] + " " + intf[1]["name"] + "\n")
    modify_intf.write(intf[3]["descr"] + " " + intf[3]["name"] + "\n")
    modify_intf.write(intf[4]["cmd"] + " " + intf[4]["status"] + "\n\n")
    modify_intf.write(intf[2]["int"] + " " + intf[2]["name"] + "\n")
    modify_intf.write(intf[3]["descr"] + " " + intf[3]["name"] + "\n")
    modify_intf.write(intf[4]["cmd"] + " " + intf[4]["status"] + "\n\n")
copy = open("r1_interfaces.txt", "r")
R1 = copy.read()
print(R1)