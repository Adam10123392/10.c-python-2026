def main():
    with open('solyom.txt','r', encoding='utf-8') as befajl:
        szoveg=befajl.read()

    spec_kar = ['-', '.', ',', '(', ')', ';', '!', '?', ':', '"']

for i in spec_kar:
    szoveg = szoveg.replace(i,"")

    szoveg = szoveg.lower()

    szoveglista = szoveg.split()

for i in szoveglista:
    if i == '-' or i == '-':
        szoveglista.remove(i)

osszeg = 0
rovidszo = szoveglista[0]
husszuszo = szoveglista[0]
for i in szoveglista:
    osszeg += len(i)
    if len(i) < len(rovidszo):
        rovidszo = i
    if len(i) > len(husszuszo):
        husszuszo = i
    print(f"Az atlag betuszam: {osszeg/len(szoveglista):.2f}\fA legrovidebb szo: {rovidszo}\fA leghoszabb szo: {husszuszo}")
if __name__=='__main__':
    main()