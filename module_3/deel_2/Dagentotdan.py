x = 0
dag = input("Welke dag van de week?")
while x < 7:
    print("ma")
    if dag == "ma":
        break
    print("di")
    if dag == "di":
        break
    print("wo")
    if dag == "wo":
        break
    print("do")
    if dag == "do":
        break
    print("vrij")
    if dag == "vrij":
        break
    print("za")
    if dag == "za":
        break
    print("zo")
    if dag == "zo":
        break   
    x += 1

# dag = int(input("welke dag? ma=1 di=2 wo=3 do=4 vr=5 za=6 zo=7 "))
# if dag > 7:
#     raise NameError("nummer mag niet hoger dan 7 zijn")

# lijst = ["ma","di","wo","do","vr","za","zo"]

# print (lijst[:dag])
