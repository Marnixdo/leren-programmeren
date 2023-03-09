from operator import truediv


gastheer = input("wie is de gastheer")
gasten = False
drank = True
chips = True

if gastheer != "corbijn" and (gastheer == "Marnix" or (drank and(gasten >= 4 or gastheer))): 
    print ("Start the party")
else:
    print ("No party")