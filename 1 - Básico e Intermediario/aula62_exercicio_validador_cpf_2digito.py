"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
import re
import sys

#cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
# cpf = '702.405.081-06' \
#     .replace('.', '')\
#     .replace('-', '')


entrada = input('CPF: ')

cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

## Validando o primeiro digito
nove_digitos = cpf[:9]
contador_regressivo_1 = 10
primeiro_digito = 0

for digito in nove_digitos:
    primeiro_digito += (int(digito) * contador_regressivo_1)
    contador_regressivo_1 -=1

primeiro_digito = (primeiro_digito * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0


## Validando o segundo digito
dez_digitos = nove_digitos + str(primeiro_digito)
contador_regressivo_2 = 11
segundo_digito = 0

for digito in dez_digitos:
    segundo_digito += (int(digito) * contador_regressivo_2)
    contador_regressivo_2 -=1

segundo_digito = (segundo_digito * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0


#validando CPF
ultimos_digitos = cpf[-2:]

if str(primeiro_digito) + str(segundo_digito) == ultimos_digitos:
    print(primeiro_digito,segundo_digito, sep='')
    print('CPF é valido!')
else:
    print(primeiro_digito,segundo_digito, sep='')
    print('CPF é invalido!') 
