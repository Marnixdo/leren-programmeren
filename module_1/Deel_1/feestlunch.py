croissant = 0.39
stokbrood = 2.78
kortingsbon = 0.50

aantal_croissant = float(input("hoeveel croissant?"))
aantal_stokbrood = float(input("hoeveel stokbrood?"))
aantal_kortingsbon = float(input("hoeveel kortingsbon"))
print (" ")
totaal_prijs = aantal_croissant * croissant + aantal_stokbrood * stokbrood - aantal_kortingsbon * kortingsbon
print ("croissantjes " + str (croissant * aantal_croissant))
print ("stokbroodjes " + str (stokbrood * aantal_stokbrood))
print ("korting " + str (kortingsbon * aantal_kortingsbon))
print (" ")
print ("TOTAAL")
print (totaal_prijs)

print (f"de feestlunch kost je bij de bakker {totaal_prijs} euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn! ")