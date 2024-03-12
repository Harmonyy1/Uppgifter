#Uppgift 1a
"""
while True:

    try:
        name = input("Filename: ")
        file = open(name, "r", encoding="utf-8")
        reader = file.readlines()
        info = [reader]
        file.close()
        break
    except:
        print("Gick inte att öppna filen")

for read in reader:
    print(read.strip())

print("\nSlut på utskriften!\n")
"""

#Uppgift 1b

while True:

    try:
        name = input("Filename: ")
        file = open(name, "r", encoding="utf-8")
        reader = file.readlines()
        file.close()
        break
    except:
        print("Gick inte att öppna filen")
count = 1 
for read in reader:
    
    print(str(count) + ".", str(read.strip()))
    count = count + 1

print("\nSlut på utskriften!\n")