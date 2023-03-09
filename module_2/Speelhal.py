toegangsticket = 7.45
vipgameseat = 0.074

aantal_tickets = float(input("hoeveel tickets?"))
aantal_minuten = float(input("hoeveel minuten"))
print (" ")
totaal = aantal_tickets * toegangsticket + aantal_minuten * vipgameseat * aantal_tickets
print ("tickets " + str (aantal_tickets * toegangsticket))
print ("vipgameseat " + str (aantal_minuten * vipgameseat * aantal_tickets))
print (" ")
print ("TOTAAL")
print (totaal)

print (f"dit geweldige dagje-uit met 4 mensen in de speelhal met 45 minuten vr kost je maar {totaal} euro")