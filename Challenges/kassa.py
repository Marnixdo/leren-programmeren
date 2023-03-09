bedrag = int(input("voer een getal in "))

aantal_twee_euro = bedrag // 200
print(f"aantal 2 euro: {aantal_twee_euro}")
restand = bedrag % 200

aantal_een_euro = bedrag // 100
print(f"aantal 1 euro: {aantal_een_euro}")
restand = bedrag % 100

aantal_vijftig_cent = bedrag // 50
print(f"aantal 50 cent: {aantal_vijftig_cent}")
restand = bedrag % 50

aantal_twintig_cent = bedrag // 20
print(f"aantal 20 cent: {aantal_twintig_cent}")
restand = bedrag % 20

aantal_tien_cent = bedrag // 10
print(f"aantal 10 cent: {aantal_tien_cent}")
restand = bedrag % 10

print(restand)

