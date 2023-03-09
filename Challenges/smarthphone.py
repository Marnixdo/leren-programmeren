from tkinter import Y


iphone = int(input("hoe duur is de iphone? "))
samsung = int(input("hoe duur is de samsung? "))
zenfone = int(input("hoe duur is de zenfone? "))
verschil = iphone - samsung

if iphone > samsung:
    duurste_telefoon = "iphone"
    goedkoopste_telefoon = "samsung"
    prijs_duurste = iphone
    prijs_goedkoopste = samsung
else:
    duurste_telefoon = "samsung"
    goedkoopste_telefoon = "iphone"
    prijs_goedkoopste = iphone
    prijs_duurste = samsung

    verschil = iphone - samsung
if verschil > 50:
    advies_telefoon = "samsung"
else:
    advies_telefoon = "iphone"

if iphone > 900 and samsung > 900 and zenfone:
    print ("Het advies is dus geen telefoon te kopen, ze zijn te duur.")
    exit()

if iphone > samsung or iphone > zenfone and iphone < samsung or iphone < zenfone:
    print (f"De iphone zit er tussenin met: {iphone} Euro")
elif samsung > iphone or samsung > zenfone and samsung < iphone or samsung < zenfone:
    print (f"De samsung zit er tussenin met: {samsung} Euro")
elif zenfone > iphone or zenfone > samsung and zenfone < iphone or zenfone < samsung:
    print (f"De zenfone zit er tussenin met: {zenfone} Euro")

print (f"De {duurste_telefoon} is het duurste, de telefoon kost: {prijs_duurste} Euro. ")
print (f"De {goedkoopste_telefoon} is het goedkoopst, de telefoon kost: {prijs_goedkoopste} euro. ")
print (f"het advies is dus de {advies_telefoon} te kopen. verschil: {verschil} ")


#if samsung > iphone:
# advies = "iphone"
    #niet = "samsung"
    #aankoop_prijs = iphone
    #niet_prijs = samsung

#if verschil <= 50:
    #koop = ("iphone")
    #nietkoop = ("samsung")
    #goedduur = ("duurder")

#if verschil > 50:
    #koop = ("samsung")
    #nietkoop = ("iphone")
    #goedduur = ("goedkoper")

