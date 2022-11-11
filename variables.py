name = "Riccardo"
surname = "Nalesso"

site = "Vicenza"
type(site)
#Il type mi dice che formato è la variabile (stringa, intero, float, ecc)
routers = 10
type(routers)
switches = 6
type(switches)
devices = routers + switches
print(devices)
engineers = 2
workflow = devices / engineers

print("There are ", routers, "routers in", site)

full_name = name + surname
print(full_name)

# Format string
full_name_final = f"My name is {name} and the surname is {surname}. The correct name is: {name} {surname}" 
print(full_name_final)
print("Each engineers have to manage ", workflow, " devices")