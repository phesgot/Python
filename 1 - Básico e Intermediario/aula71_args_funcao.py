"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembre-te de desempacotamento

# x,y,*resto = 1,2,3,4
# print(x,y, resto)

# def soma(x,y):
#     return x+y

numeros = 1,2,3,4,5,6,7,8,9

def soma(*args):
    soma = 0
    for numero in args:
        soma +=numero
        
    return soma

primeira_soma = soma(1,2,3,4,5,6)
print(primeira_soma)

segunda_soma = soma(*numeros)
print(segunda_soma)

print(sum((1,2,3,4,5,6)))