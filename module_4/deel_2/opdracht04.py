from fruitmand import fruitmand
import random

naam = []
getal = int(input("noem een getal "))

for x in fruitmand:
    naam.append(x['name'])

for x in range(getal):
    print (random.choice(naam))