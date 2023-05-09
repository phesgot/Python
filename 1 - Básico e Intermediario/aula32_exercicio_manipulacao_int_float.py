"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_inteiro = input('Digite um numero inteiro: ')

try:
    par_impar = int(numero_inteiro) % 2

    if par_impar:
        print(f'Número digitado "{numero_inteiro}" é impar')
    else:
        print(f'Número digitado "{numero_inteiro}" é par')

except:
    print('O número digitado não é inteiro')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = input('Quantas horas? ')


try:
    bom_dia = int(horas) <=11
    boa_tarde = int(horas) <=17
    boa_noite = int(horas) <=23

    if bom_dia:
        print('Bom dia! :) ')
    elif boa_tarde:
        print('Boa tarde! :) ')
    elif boa_noite:
        print('Boa noite! :) ')
    else: 
        print('Não conheço essa hora! :( ')
except:
    print('Você não digititou um número inteiro! :( ')



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input('Qual o seu primeiro nome? ')

tamanho_nome = len(primeiro_nome)

if tamanho_nome <= 4:
    print(f'{primeiro_nome} seu nome é curto')
elif tamanho_nome == 5 or tamanho_nome == 6:
    print(f'{primeiro_nome} seu nome é normal')
else:
    print(f'{primeiro_nome} seu nome é muito grande')