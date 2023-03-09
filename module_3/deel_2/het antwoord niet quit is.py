a = 0

while True:
    zin = input("Geef een random antwoord op deze vraag en typ quit als je wilt stoppen ")
    a +=1
    if zin == "quit":
        break
print(f" Je hebt {a} keer een input gebruikt")