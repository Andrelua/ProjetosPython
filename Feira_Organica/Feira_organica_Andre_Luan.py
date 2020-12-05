import pandas as pd
from reportlab.pdfgen import canvas as cv

df_folhas = pd.read_csv('Folhas_hortalicas.csv')
df_frutas = pd.read_csv('Frutas.csv')
df_C_t = pd.read_csv('Lanches_C_trigo.csv')
df_S_t = pd.read_csv('Lanches_S_trigo.csv')
df_outros = pd.read_csv('Outros.csv')
df_pasti = pd.read_csv('Pastinhas_ante.csv')
df_raizes = pd.read_csv('Raizes.csv')


def menu():
    print('-='*30)
    print('OLÁ CLIENTE !! BEM-VINDO(A) A FEIRA ORGâNICA DA CIDADE')
    print('-='*30)

    print('PRIMEIRO VOU PEDIR PARA QUE SE REGISTRE.')
    nome_Cli = input("Com o seu nome: ")
    end_Cli = input("Com o seu endereço (Rua, Número, Bairro, Cidade): ")

    print('AGORA, VAMOS AS COMPRAS!')
    
    compras = 0

    menu_Entrada = 1
    while menu_Entrada != 0:
        menu_Entrada = int(input("QUAL ÁREA DESEJA IR PRIMEIRO? \n 1 - Folhas e hortaliças \n 2 - Frutas \n 3 - Lanches com trigo \n 4 - Lanches sem trigo \n 5 - Outros \n 6 - Pastinhas, antepastos e geleias. \n 7 - Raizes \n 0 - Sair \n:"))
        if (menu_Entrada == 1):
            compras = compras + 1
    
    


menu()