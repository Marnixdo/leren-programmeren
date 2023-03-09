from random import randint
import random

naam =  input("wat is je naam")
hoeveelheid = int(input("hoeveel keer wil je complimenten krijgen? "))
vorig_random_getal = 0

print (f"je bent een coole gozer {naam}")

for x in range(hoeveelheid):
    random_getal = randint(1, 4)
    while random_getal == vorig_random_getal:
        random_getal = randint(1, 4)

        vorig_random_getal =random_getal

    if random_getal == 1:
        print (f"je bent autistisch {naam}")
    elif random_getal == 2:
        print (f"je bent een coole gozer {naam}")
    elif random_getal == 3:
        print (f"je bent lgtbq member {naam}")
    elif random_getal == 4:
        print (f"je valt op jongens{naam}")
    

