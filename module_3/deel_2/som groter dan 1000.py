totaal_getal = 50
getal = 50
string_getal = '50'
erbij = 0
while totaal_getal + 1 <= 1000:
    getal += 1
    string_getal += " + " + str(getal)
    totaal_getal += getal
    erbij += 1
    print(f"{erbij}. {string_getal} = {totaal_getal}")