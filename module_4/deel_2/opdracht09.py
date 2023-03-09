from fruitmand import fruitmand
kleur = []

for fruit in fruitmand:
    if fruit['name'] == 'druif':
        fruitmand.remove(fruit)

for x in fruitmand:    
    if x ['color'] not in kleur:
        kleur.append(x['color'])
print(kleur)
    
