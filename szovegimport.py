with open('szoveg.txt','r', encoding='utf-8') as tartalom:
    szoveg = tartalom.read()

spec_kar = ['-', '.', ',', '(', ')', ';', '!', '?', ':', '"']
for jel in spec_kar:
    szoveg = szoveg.replace(jel,"")

szoveg = szoveg.lower()

#print(szoveg)

szoveglista = szoveg.split()

print(*szoveglista, sep=';')

with open('szoveg_atalakitott.txt', 'w',encoding='utf-8') as tartalom:
    print(*szoveglista, sep=';' ,file=tartalom)

print("A fajl atalakitasa kesz")