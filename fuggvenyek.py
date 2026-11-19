import random

def osszeg(a:int, b:int) -> int:
    return a + b

def kulonbseg(a:int, b:int) -> int:
    return a - b

def szorzat(a:int, b:int) -> int:
    return a * b

def hanyados(a:int, b:int) -> int:
    return a / b

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