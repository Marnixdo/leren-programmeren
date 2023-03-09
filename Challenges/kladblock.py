#vraagt een getal aan de gebruiker en geeft deze terug
# def vraag_een_getal(vraag: str) -> int: # betekent defineer = maak aan
#     while True:
#         try:
#             getal  = int(input(vraag))
#             break
#         except ValueError:
#             print("je moet wel een getal invoeren ")
#             continue
#     return getal

# leeftijd = vraag_een_getal("voer je leeftijd in. ")
# geboortejaar = vraag_een_getal("voer je geboortejaar in. ")
# geboortemaand = vraag_een_getal("voer je geboortemaand in. ")
# geboortedag = vraag_een_getal("voer je geboortdag in. ")

# print(leeftijd)
# print(geboortejaar)
# print(geboortemaand)
# print(geboortedag)


antwoord  = input("wat is je naam. ").lower()

def vraag_een_naam(vraag: str) -> str: # betekent defineer = maak aan
    antwoord  = input(vraag)
    return vraag
naam = vraag_een_naam("wat is je naam. ")







