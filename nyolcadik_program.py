szamlista = []

for index in range(1000):
    if index % 133 == 0:
        szamlista.append (index)

print(f"{szamlista}")
print(f"Elemek száma: {len(szamlista)}")