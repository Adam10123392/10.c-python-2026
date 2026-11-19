szam1 = int(input("Kérem az első számot: "))
szam2 = int(input("Kérem a második számot: "))

ossz = szam1 + szam2
kul = szam1-szam2
szor = szam1 * szam2
hany = szam1 / szam2
mar = szam1 % szam2

print(f"-  -  -\nÖsszeg = {ossz}\nKülönbség = {kul}\nSzorzat = {szor}\nHányados = {hany}\nMaradékképzés = {mar}")
print(f"\nEgyenlet eredmény = {ossz + kul * mar / szor + (ossz * kul)}")