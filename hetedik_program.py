lista = [34, 122, 6, 8, 10] # lista rugalmasan bővíthető öszetett adatszerkezet
# 0. index az első elem

lista.append(234)
lista.append(234)
lista.remove(234)
lista.pop()
print(f"Lista elemei: {lista}") # lista kiírása
print(f"Lista elemei: {lista [0]}")
print(f"Lista elemei: {lista [-1]}")
print(f"Lista elemeinek száma: {len(lista)}")
lista.clear()
