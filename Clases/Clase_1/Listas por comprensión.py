cubos = []
# elevado al cubo
for x in range(10):
    cubos.append(x**3)  
print(cubos)

# Lista por comprensión
cuboslc = [x**3 for x in range(10)]
print(cuboslc)

lista = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            lista.append((x, y))
print(lista)

# lista multidimensional por comprensión
listalc = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# >>> [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
print(listalc)
