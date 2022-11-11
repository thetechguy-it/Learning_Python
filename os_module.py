import os

print(os.getcwd())
#Result c:/Users/riccardo.nalesso/Documents/GitHub
os.chdir("c:/Users/riccardo.nalesso/Documents")
print(os.getcwd())
#Result c:/Users/riccardo.nalesso/Documents
# os.open(path: c:/Users/riccardo.nalesso/Documents/GitHub/Learn_Python/list.py)
os.chdir("c:/Users/riccardo.nalesso/Documents/Virtual Machines")
#os.mkdir("OS_TEST")
print(os.listdir())

