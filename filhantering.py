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
"""
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
    if count > 20:
        input()

print("\nSlut på utskriften!\n")
"""


#Uppgift 2
"""
def main():
    name = "TELE.txt"

    try:
        file = open(name, "w")

    except:
        print("Gick inte att öppna filen")
        return
    
    else:
        while True:
            name = input("Name: ")
            if name == "":
                file.close()
                return
            
            telnr = input("Telnr: ")
            file.write(name + "\n")
            file.write(telnr + "\n")
main()
"""


#Uppgift 3

print("TELEFONLISTA")

name = "TELE.txt"

try:
    file = open(name, "r")

except:
    print("Gick inte att öppna filen")

else:
    inforow = file.readline().strip()   #tar värdet längst upp i filen och tar bort "\n" som finns mellan nästa grej, tar det värdet också

    while inforow:
        print(inforow, end = "\t")  #printar inforow och avslutar med "\t" istället för default "\n"
        inforow = file.readline().strip()

        if not inforow:     #om programmet inte kan skapa en inforow enligt instruktion
            print("*loud incorrect buzzer sound*")
        
        else:
            print(inforow)
            inforow = file.readline().strip()