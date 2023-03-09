import random

kleuren_lijst = ["rood", "blauw", "groen", "geel", "bruin"]
hoeveelheid = int(input("hoeveel m&m's wil jij in jou zak m&m's hebben? "))
zak ={}

aantal = 1

for x in range(hoeveelheid):
    kleur = random.choice(kleuren_lijst)
    if kleur not in zak:
        zak.update({kleur : aantal})
    else:
        zak[kleur] += 1

    
print(zak)
    
