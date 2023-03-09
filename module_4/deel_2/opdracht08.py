from fruitmand import fruitmand

x = fruitmand

fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 2500,
    'color' : 'green',
    'round' : True
})

for x in fruitmand:    
  print(x['weight'])


