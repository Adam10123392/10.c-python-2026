szam = int(input("Kérem egy számot: "))

if szam < 0:
    print(f"A {szam} negatív!")
elif szam > 0:
    print(f"A {szam} pozitív!")
else:
    print(f"A {szam} pontosan 0!")