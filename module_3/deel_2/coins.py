# name of student: Marnix den Otter
# number of student: 99073040
# purpose of program: 
# function of program:
# structure of program: 

vijfeuro = 500
viereuro = 400
drieeuro = 300
tweeeuro = 200
eeneuro = 100
vijftigcent = 50
twintigcent = 20
tiencent = 10
vijfcent = 5

toPay = int(float(input('Amount to pay: '))* 100) # hoveel er betaald moet worden 
paid = int(float(input('Paid amount: ')) * 100) # hoeveel er is betaald
change = paid - toPay # wisselgeld variabelen

if change > 0: # als de variabel change 0 is begint de programma
  coinValue = 500 # de waarde van de coin in het begin
  
  while change > 0 and coinValue > 0:#start van de loop de loop stopt pas als alle wissel geld  teruggegeven is 
    nrCoins = change // coinValue # berekend change gedeeld door coinvalue dan krijg je nrCoins

    if nrCoins > 0: # als er nog een coin moet ingevoerd worden dan start de IF statement
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #laat je zien hoeveel munten van  coinvalue kan geven.
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #Change is - De aantal coins dat ingevoerd is keer de coinvalue

# comment on code below: Hier gaat die langs alle coinvalue's
    if coinValue == vijfeuro:
      wappie = nrCoinsReturned
    elif coinValue == viereuro:
      wappie2 = nrCoinsReturned
    elif coinValue == drieeuro:
      wappie3 = nrCoinsReturned
    elif coinValue == tweeeuro:
      wappie4 = nrCoinsReturned
    elif coinValue == eeneuro:
      wappie5 = nrCoinsReturned
    elif coinValue == vijftigcent:
      wappie6 = nrCoinsReturned
    elif coinValue == twintigcent:
      wappie7 = nrCoinsReturned
    elif coinValue == tiencent:
      wappie8 = nrCoinsReturned
    elif coinValue == vijfcent:
      wappie9 = nrCoinsReturned
    else:
      coinValue = 0
try:
  if change > 0: # Hier laat hij de change zien dat is ingevuld ,en  als de change niet is compleet terug gegeven
    print('Change not returned: ', str(change) + ' cents')
  else:
    print(f"{vijfeuro}: {wappie}")
    print(f"{viereuro}: {wappie2}")
    print(f"{drieeuro}: {wappie3}")
    print(f"{tweeeuro}: {wappie4}")
    print(f"{eeneuro}: {wappie5}")
    print(f"{vijftigcent}: {wappie6}")
    print(f"{twintigcent}: {wappie7}")
    print(f"{tiencent}: {wappie8}")
    print(f"{vijfcent}: {wappie9}")
except NameError: 
  exit()