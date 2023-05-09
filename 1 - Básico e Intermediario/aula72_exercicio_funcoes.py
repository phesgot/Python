# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável


def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1,2,3,4,5)
print(multiplicacao)


# Crie uma funcao que fala se um numero é par ou ímpar.
# Retone se o número é par ou ímpar

def par_impar(x):
    valor = x % 2 == 0
    if valor:
        return f'{x} É PAR'
    return f'{x} É IMPAR'

print(par_impar(4)) 
