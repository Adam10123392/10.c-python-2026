'''# szöveg kiíratás
print("") #egy soros
print(f"") #valtozoertekkel
#\n <- sortores
#\t <- tabulátor

#tobb sor eseten
print("a")
print("b")

print("a\nb")

#adatelérés
adat = int(input("Add meg a számot: ")) # tipuskonverzio kell, minden bekérés alapvetőleg szöveg

#  változók
a = int(5) #egész szám
b = float(2) #lebegőpontos szám
c = str("Alma") # szöveg (neki vannak listaszerű tulajdonságai, minden betű külön index alatt van)
print(f"A szó kezdőbetűje: {c[0]}")
folytassuk = bool(True)

# feltételes eljárások
if folytassuk:
    print("Akkor folytassuk hát...")
else:
    print("akkor ne folytassuk...")

szam = int(98)
if szam < 100:
    print("A szám kisebb,mint 100.")
elif szam < 0:
    print("A szám minusz.")
else:
    print("A szám pontosan 0.")

inputnum = int(input("Kérem egy számot: "))
if inputnum > 0 and inputnum < 50:
    pass

if inputnum == 12 or inputnum == 33:
    pass

# listák és ciklusok
lista = [12, 34, 76, 2, 1]
print(f"{listaja[0]}\n{lista[-1]}\n{lista[2]}")

import random
szamlista = [0]

for _ in range(100): # eldobjuk a változót, mert nincsen rá szükség (sehol sem akarjuk felhasználni)
    szamlista.append(random.randint(1, 5000))

for x in range(100):
    x = random.randint(1, 5000)
    szamlista.append(x)

for x in szamlista:
    print(x)

print(szamlista)
print(*szamlista,sep='\t',end='\n')'''

import random
szamlista = []

for _ in range(100):
    szamlista.append(random.randint(1,5000))

index = 50
while index < len(szamlista): #elotesztelo ciklus
    print(f"szamlista{index}")
    index += 1

min = szamlista[0]
max = szamlista[0]

for x in szamlista:
    if min > x:
        min = x
    if max < x:
        max = x

print(f"A legkisebb elem: {min}")
print(f"A legnagyobb elem: {max}")

paros = []
for x in szamlista:
    if x % 2 == 0:
        paros.append(x)
    
print(f"paros szamok a listaban: {paros}")

print(f"minimum: {min}\nmaximum: {max} ")

teljes = 0
for x in szamlista:
    teljes += x

print(f"atlag: {teljes/len(szamlista)}")