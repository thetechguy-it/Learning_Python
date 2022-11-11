ccie1 = "CCIE Enterprise Infrastructure"
ccie2 = "CCIE Servive Provider"
ccie3 = "CCIE Security"
ccie4 = "CCIE Collaboration"
ei = 40000
sp = 10000
sec = 15000
total_ei = f"There are {ei} {ccie1} certified people in the world"
total_sp = f"There are {sp} {ccie2} certified people in the world"
total_sec = f"There are {sec} {ccie3} certified people in the world"

print(total_ei)
print(total_sp)
print(total_sec)

total_ccies = ei + sp + sec
print(f"The total number of CCIE's in the world = {total_ccies}")