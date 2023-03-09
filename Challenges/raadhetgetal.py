grootste_getal = 0
kleinste_getal = 1000
aant_deelbaar_drie = 0

for x in range(10):
    getallen = int(input("geef een random getal boven de 0 en onder de 1000: "))
    if getallen > grootste_getal:
        grootste_getal = getallen
    
    if getallen < kleinste_getal:
        kleinste_getal = getallen

if getallen % 3 == 0:
    aant_deelbaar_drie = aant_deelbaar_drie + 1

print (f"het grootste getal is {grootste_getal}")
print (f"het kleinste getal is {kleinste_getal}")
print (f"aantal deelbaar door drie(zonder rest) {aant_deelbaar_drie}")



