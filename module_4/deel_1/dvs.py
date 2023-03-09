import random

deck_kleuren = ["harten", "klaveren", "schoppen", "ruiten"]
deck_kaarten = ["","2","3","4","5","6","7","8","9","10", "boer", "vrouw", "heer", "aas"]
deck = []

for x in deck_kleuren:
    for c in deck_kaarten:
        deck.append(x + " " +c) 

for x in range(2):
    deck.append("joker")

random.shuffle(deck)

for v in range(7):
    deck.pop(v)
    print(deck[v])

print (f"deck: {deck}")





#aparte secties maken voor:
#joker
#kaartsoorten
#en de kleur kaarten
#randint gebruiken
#