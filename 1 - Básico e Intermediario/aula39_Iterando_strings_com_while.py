# """
# Iterando strings com while
# """
# #       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
# #      1110987654321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

# nova_string = ''
# nova_string += '*L*u*i*z* *O*t*á*v*i*o'

nome = input('Digite o seu nome: ')
tamanho_nome = len(nome)
indice = 0
novo_nome = ''


while indice < tamanho_nome:
    novo_nome += f'*{nome[indice]}'
    indice += 1

print(novo_nome)