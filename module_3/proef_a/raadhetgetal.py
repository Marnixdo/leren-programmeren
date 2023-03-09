import random
ronde = 0
random_getal = random.randint(1, 1000)
for x in range(20):
    while ronde <10:
        ronde += 1
        geraden_getal = int(input("raad een getal tussen 1 en 1000 "))
        if geraden_getal == random_getal:
            print("goed")
        else:
            print("fout")

if ronde >10:
     print("helaas heb je het niet goed geraden")



# <50 verschil toevoegen
# <20 verschil toevoegen
# dus heel warm en warm erbij zetten


    
    


# maakt het getal altijd positief
