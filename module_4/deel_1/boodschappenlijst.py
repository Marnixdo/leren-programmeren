dictionary = {}
teller = 1

while True:
    vraag_boodschappen = input("Welk product ga je kopen? ")
    if vraag_boodschappen in dictionary:
        dictionary[vraag_boodschappen] += 1
    else:
        dictionary.update({vraag_boodschappen : teller})
    vraag_doorgaan = input("wil je nog een product kopen? ")
    if vraag_doorgaan == "nee":
        break

print(" ")
print("-[ BOODSCHAPPENLIJST ]-")       
for key,value in dictionary.items():
	print(key, ':', value)

print("-----------------------")
print(" ")
