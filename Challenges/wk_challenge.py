land1 = input("Noem een land dat in het WK speelt ")
land2 = input("Noem een land dat in het WK speelt ")
land3 = input("Noem een land dat in het WK speelt ")
Afkortingland1 = input("Noem de afkorting van land 1 ")
afkortingland2 = input("Noem de afkorting van land 2 ")
afkortingland3 = input("Noem de afkorting van land 3 ")

puntentotaal1 = 0
puntentotaal2 = 0
puntentotaal3 = 0

doelsaldo1 = int(input(f"hoeveel heeft {land1} gescoord in de eerste wedstrijd tegen {land2}? "))
doelsaldo2 = int(input(f"hoeveel heeft {land2} gescoord in de eerste wedstrijd tegen {land1}? "))
doelsaldo3 = int(input(f"hoeveel heeft {land2} gescoord in de eerste wedstrijd tegen {land3}? "))
doelsaldo4 = int(input(f"hoeveel heeft {land3} gescoord in de eerste wedstrijd tegen {land2}? "))

if doelsaldo1 > doelsaldo2:
    puntentotaal1 += 3
else:
    puntentotaal2 += 3

if doelsaldo3 > doelsaldo4:
    puntentotaal2 += 3
else:
    puntentotaal3 += 3

if doelsaldo1 > doelsaldo2:
    doelsaldo2 -= doelsaldo1
else:
    doelsaldo1 -= doelsaldo2

if doelsaldo3 > doelsaldo4:
    doelsaldo2 -= doelsaldo3
else:
    doelsaldo3 -= doelsaldo2

doelsaldo2 += doelsaldo3


print(f"Wedstrijd {land1} - {land2} eindigde in: {doelsaldo1} {doelsaldo2}")
print("Overzicht groep A")
print(f"{Afkortingland1}: punten {puntentotaal1}; doelsaldo: {doelsaldo1} ")
print(f"{afkortingland2}: punten {puntentotaal2}; doelsaldo: {doelsaldo2} ")
print(f"{afkortingland3}: punten {puntentotaal3}; doelsaldo: {doelsaldo3} ")

