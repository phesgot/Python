# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\Users\phesg\Desktop\exemplos'
import os

caminho = os.path.join('C:\\Users', 'phesg', 'Desktop', 'exemplos')


for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        caminho_completo_imagem = os.path.join(caminho, pasta, imagem)
        print(f'Camninho: {caminho_completo_imagem}  --- {imagem}')
