with open('szoveg_atalakitott.txt', 'r', encoding='utf-8') as tartalom:
    szoveg=tartalom.read()

szoveglista = szoveg.split(';')

#egyéb felesleges szavak eltávolítása
for szo in szoveglista:
    print(szo)
    if szo == '–':
        szoveglista.remove(szo)

#for szo in szoveglista:
 #print(szo)

print(f"szavak száma: {len(szoveglista)}")

abc = []
for szo in szoveglista:
    if szo[0] == 'a' or szo [0] == 'b' or szo[0] == 'c':
        if szo !='a' and szo != 'az':
            abc.append(szo)

print(*abc, sep=' - ')

# határozd meg, hogy mennyi az átlagos betűszám

osszeg = 0
for szo in szoveglista:
    osszeg += len(szo)
print(f"Az atlag betuszam: {osszeg/len(szoveglista):.2f}")

#legrovidebb leghoszabb szó hivatkozást szed ki