import random

menmkleuren = ("oranje", "blauw", "groen", "bruin")
zak = []

hoeveelheid = int(input("hoeveel m&m's wil jij in jou zak m&m's hebben? "))

for x in range(hoeveelheid):
    getal = random.randint(0,3)
    zak.append(menmkleuren[getal])



print(zak)





