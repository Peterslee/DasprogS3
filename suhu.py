# Air dalam bentuk es pada suhu <= 0o Celcius
# Air dalam bentuk cair pada suhu 0o s.d 100o Celcius
# Air dalam bentuk uap pada suhu > 100o Celcius

# Konversi suhu dari skala Fanrenheit (oF)
# ke skala Celcius (oC) dapat dihitung dengan
# rumus C = (F-32) x 5 / 9
# C = nilai suhu dalam Celcius
# F = nilai suhu dalam Fanrenheit

# Buat sebuah program yang menerima suhu dalam skala Fanrenheit kemudian mengkonversinya ke dalam skala Celcius. Cetak bentuk/wujud air pada suhu tersebut.
f=int(input("masuakan suhu: "))
c = (f-32) * 5 / 9
if c  <= 0 :
    print(f"wujud air adalah es dengan suhu {c}o celcius")
elif c < 100 :
    print(f"wujud air adalah cair dengan suhu {c}o celcius")
else:
    print(f"wujud air adalah uap dengan suhu {c}o celcius")
