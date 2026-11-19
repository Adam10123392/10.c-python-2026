# egyszerű kiírás
print(f"első üzenet!")
print(f"Egyszerű kiírás")
print(f"-   -   -")
# változó
a=int(5)
b=int(7)
print(f"Összeg = {a + b}")
print(f"Különbség =  {a - b}")
print(f"Szorzat =  {a * b}")
print(f"Hányados =  {a / b}")
print(f"Maradékképzés =  {a % b}")

#adatbevitel
szam = int(input("Kérek egy számot: "))
print(f"A szám fele: {szam / 2}")

#szöveg
szoveg= str("Alma")

print(f"{type(a)}")
print(f"{type(szoveg)}")

#páros-páratlan

szam = int(input("Kérek egy számot: "))
if szam % 2 == 0:
    print(f"A szám páros!")
else:
    print(f"A szám páratlan!")  