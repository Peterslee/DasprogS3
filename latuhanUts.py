hondaMc = "beat, scoopy, vario"
hondaMl = "revo, supra, gtr"

yamahaMc = "freego, x-ride, mio, gear"
yamahaMl = "vega, jupiter, mx king"
print("program ini akan membantu anda memilih jenis motor bebek")
pilihH=input("pilih brand: Yamaha (Y) atau Honda (H)?: ")
if pilihH == "y" :
    pilihT = input("Transmisi otomatis (A) atau manual (M)?: ")
    if pilihT == "a" :
        print(hondaMc)
    else :  
        print(hondaMl)
else : 
    pilihT = input("Transmisi otomatis (A) atau manual (M)?: ")
    if pilihT == "a" :
        print(yamahaMc)
    else :
        print(yamahaMl)