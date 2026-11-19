szam = int(input("Kérem egy számot: "))

if szam % 3 == 0 and szam % 5 == 0:
    print(f"A szám osztható 3-mal és 5-tel is!")
elif szam % 3 == 0 and not szam % 5 == 0:
    print(f"A szám csak 3-mal osztható!")
elif not szam % 3 == 0 and  szam % 5 == 0:
    print(f"A szám csak 5-tel osztható!")
else:
    print(f"A szám egyikkel sem  osztható!")