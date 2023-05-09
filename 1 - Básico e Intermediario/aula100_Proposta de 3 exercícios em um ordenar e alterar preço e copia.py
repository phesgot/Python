import copy

from dados import produtos

# copy, sorted, produtos.sort

# Exercícios

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

print('\n Produtos originais \n')
print(*produtos, sep='\n')
print('\n Produtos com preço alterado \n')
print(*novos_produtos, sep='\n')
print('\n Produtos ordenados por nome \n')
print(*produtos_ordenados_por_nome, sep='\n')
print('\n Produtos ordenados por preço \n')
print(*produtos_ordenados_por_preco, sep='\n')