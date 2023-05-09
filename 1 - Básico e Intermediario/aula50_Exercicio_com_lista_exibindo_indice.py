"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']


indices = range(len(lista))
print(indices)


for indice in indices:
    print(indice, lista[indice], type(lista[indice]))


