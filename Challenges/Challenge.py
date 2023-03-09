Lengte = float(input("Hoe lang gaat u zwembad worden? "))
Breedte = float(input("Hoe breedt gaat u zwembad worden? "))
Diepte = float(input("Hoe diep gaat u zwembad worden? "))

Totale_m3 = Lengte * Breedte * Diepte
Totale_m2 = Lengte * Breedte
Uitgraven = 25.0
afvoeren = 32.5
uitgraven_TOTAAL = Totale_m3 * Uitgraven
afvoeren_TOTAAL = Totale_m3 * afvoeren

if Totale_m3 > 20:
    Afstand = float(input("Hoeveel km afstand is het bedrijf van joris van u vandaan? "))
    print (Afstand)
if Totale_m3 < 20:
    print (Afstand)

print (f"Offerte voor een zwembad van {Lengte} bij {Breedte} bij {Diepte} meter: {Totale_m3} M3 en {Totale_m2} M2 ")
print (f"Uitgraven: {uitgraven_TOTAAL} euro ")
print (f"Afvoeren: {afvoeren_TOTAAL} euro ")


