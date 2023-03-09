from fruitmand import fruitmand

for x in fruitmand: 
  naam = x['name']
  if naam == "appel":
    print(x['weight'])
    print(naam)


