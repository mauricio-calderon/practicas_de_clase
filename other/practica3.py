"""
x = []  #lista vacía, [-10, 10]
c = -10   #controla el bucle
while c <= 10:
    if c == -10:
        x.append(round(c, 1))
        c += 0.1
    else:
        c += 0.1
        x.append(round(c, 1))

# y = x^2
y = []  #coordenadas en Y
for i in x:
    y.append(round(i**2, 1))
#print(x)
#print(y)
n = len(x)
print(f"X\t\tY = X^2")
for i in range(0, n):
    print(f"{x[i]}\t\t{y[i]}")
"""
texto = "Sergio Antonio Padilla Torres"
n_vocal = 0
n_espacio = 0
n_consonantes = 0
for letra in texto:
    if letra.lower() in "aeiouáéíóúäëïöü":
        n_vocal = n_vocal + 1
    if letra.isspace():
        n_espacio = n_espacio + 1
    if letra.lower() in "bcdfghjklmnñpqrstvwxyz":
        n_consonantes += 1
print(f"Total vocal: {n_vocal}")
print(f"Total espacio: {n_espacio}")
print(f"Total consonantes: {n_consonantes}")
t = n_vocal + n_espacio + n_consonantes
print(len(texto), t)

