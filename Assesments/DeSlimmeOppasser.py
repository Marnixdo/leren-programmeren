giraffe_poten = 4
struisvogel_poten = 2
zebra_poten = 4

aantal_giraffen  = input("hoeveel giraffe zijn er? ")
aantal_struisvogels = input("hoeveel struisvogels zijn er? ")
aantal_zebras = input("hoeveel zebra's zijn er? ")


def De_Slimme_Oppasser(giraffen , struisvogels , zebras):
    aantal_poten =  aantal_giraffen * giraffe_poten + aantal_struisvogels * struisvogel_poten + aantal_zebras * zebra_poten  

    return aantal_poten
print(De_Slimme_Oppasser())
   








