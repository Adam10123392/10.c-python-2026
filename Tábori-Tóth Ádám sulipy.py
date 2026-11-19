nap = (input('Jó napja van?'))
if nap == "igen":
      print('Gratulálok')
elif nap == "nem":
      print("Sajnálom.")
else:
      print("Sajnos nem értem a válaszodat")


szam = int(input('Adj meg egy számot! '))
if szam % 2 == 0:
      print('A megadott szám páros.')
else:
    print('A megadott szám páratlan.')


import random

szam = random.randint(0, 5)

szami = int(input('Adj meg egy számot! '))
if szam == szami:
      print('egyenlő')
if szam < szami:
    print('nagyobb')
if szam > szami:
      print('kisebb')


szamu = int(input('Adj meg egy számot! '))
  
if  szamu > 0 and szamu %2 == 0:
    print('A szám pozitív páros')
  
if szamu < 0 and szamu %2 != 0:
    print('A szám negatiív páratlan')

szamc = int(input('Adj meg egy számot! '))

  
if szamc %3 == 0 and szamc % 4 != 0:
    print('csak 3-mal osztható')
  
if szamc %4 == 0 and szamc %3 != 0:
    print('csak 4-gyel osztható')
  
if szamc %3 == 0 and szamc % 4 == 0:
    print('3-mal és 4-gyel is osztható')
  
if szamc %3 != 0 and szamc % 4 != 0:
    print('sem 3-mal, sem 4-gyel nem osztható! ')

szaml = int(input('Adj meg egy számot! '))

szamg = random.randint(1, 3)      
if szamg == szaml:
      print('egyenlő')
if szamg < szaml:
    print('nagyobb')
if szamg > szaml:
      print('kisebb')

szamy = str(input('fej vagy írás?'))
szame = random.randint(1,2)
if szamy.lower() == "fej":
     szamy = 1
elif szamy.lower() == "írás":
     szamy = 2
else:
     print("Nem találtad el")
if szamy == szame:
     print("eltaláltad")
else:
     print("Nem tálaláltad el")