import json

# pessoa = {
#     'nome': 'Pedro',
#     'sobrenome': 'Torres',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.7,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open('aula117.json', 'w', encoding='utf8') as arquivoJson:
#     json.dump(
#         pessoa, 
#         arquivoJson, 
#         ensure_ascii=False,
#         indent=2
#         )

with open('aula117.json', 'r', encoding='utf8') as arquivoJson:
    pessoa = json.load(arquivoJson)
    print(pessoa)
    print(pessoa['nome'])
    print(pessoa['sobrenome'])
    print(pessoa['enderecos'][0])