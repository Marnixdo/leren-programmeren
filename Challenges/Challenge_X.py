# from calendar import c


# Aapje = input("wat is een leuk dier in het wild? ")
# aapje2 = ""
# for c in Aapje:
#     aapje2 += c
#     aapje2 += c
# print (aapje2)

zin = input("vul hier wat in ")
zin2 = " "
woord = " "

for c in zin:
    if c == " ":
        zin2 += woord + " " + woord + " "
        woord = " "
    else:
        woord += c

zin2 += woord + " " + woord

print (zin2)
