from datetime import datetime
from dateutil.relativedelta import relativedelta

formato_br = '%d/%m/%Y'

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo

while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_de_parcelas = len(data_parcelas)
valor_da_parcela = valor_total / numero_de_parcelas

print('Datas de vencimento:\n')

for datas in data_parcelas:
    print(datas.strftime(formato_br))


print(f'\nVocê pegou R$ {valor_total:,.2f}')
print(f'para pagar em {delta_anos.years} anos '
      f'({numero_de_parcelas} meses) em parcelas de '
      f'R${valor_da_parcela:,.2f}\n')
