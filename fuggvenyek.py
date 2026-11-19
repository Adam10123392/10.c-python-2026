import random

def osszeg(a:int, b:int) -> int:
    return a + b

def kulonbseg(a:int, b:int) -> int:
    return a - b

def szorzat(a:int, b:int) -> int:
    return a * b

def hanyados(a:int, b:int) -> int:
    return a / b

def listageneralas(db:int, tol:int, ig:int) -> list:
    lista = []
    for _ in range(db):
        lista.append(random.randint(tol, ig))
    return lista

#szam1 = int(input("Kérem az első számot: "))
#szam2 = int(input("Kérem a második számot: "))

szam1 = random.randint(1, 1000)
szam2 = random.randint(1, 1000)
osszeadas = osszeg(szam1, szam2)
kivonas = kulonbseg(szam1, szam2)
szorzás = szorzat(szam1,szam2)
osztas = hanyados(szam1, szam2)

print(f"A(z) {szam1} és A(z) {szam2} összege = {osszeadas}")
print(f"A(z) {szam1} és A(z) {szam2} különbsége = {kivonas}")
print(f"A(z) {szam1} és A(z) {szam2} szorzata = {szorzás}")
print(f"A(z) {szam1} és A(z) {szam2} hányadosa = {osztas:.2f}")

# ez után
szamlista1 = listageneralas(20000, 1, 500)
szamlista2 = listageneralas(20000, 1, 500)

index = 0
hanyszor = 0
egyezes = []
for x in szamlista1:
    if x == szamlista2[index]:
       hanyszor += 1
    index += 1
print(f"\nA 2 lista ennyiszer aztonos egymással: {hanyszor}")
if len(egyezes) != 0:
    print(*egyezes, sep=' - ')
else:
    print("A két lista között nincs egyezés")