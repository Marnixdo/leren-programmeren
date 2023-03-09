antwoord = input("voer ja of nee in")

# if antwoord == "ja" or "nee":
#     print("het is waar")
# else:
#     print("het is niet waar")



if antwoord in ("ja", "nee"):
    print("het is goed")

while antwoord not in ("ja", "nee"):
    antwoord = input("voer ja of nee in")

while True:
    antwoord = input("voer ja of nee in")
    if antwoord in ("ja", "nee"):
        break

