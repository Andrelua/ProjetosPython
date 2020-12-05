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
    
    compras = []

    menu_Entrada = 1
    while menu_Entrada != 0:
        menu_Entrada = int(input("PARA QUAL ÁREA DESEJA IR ? \n 1 - Folhas e hortaliças \n 2 - Frutas \n 3 - Lanches com trigo \n 4 - Lanches sem trigo \n 5 - Outros \n 6 - Pastinhas, antepastos e geleias. \n 7 - Raizes \n 0 - Sair \n:"))
        # Dataframe Folhas
        if (menu_Entrada == 1):
           print(df_folhas.head(14)) 
           escolha_produto = 1
           while escolha_produto != 999:
                escolha_produto = int(input("Escolha um produto pelo seu inidice (999 - encerra):"))
                if escolha_produto == 999:
                   break
                else:
                    print(f'VOCÊ ESCOLHEU O PRODUTO : {df_folhas.loc[escolha_produto][0]} POR R$ {df_folhas.loc[escolha_produto][2]}.')
                    compras.append(df_folhas.loc[escolha_produto])
        # Dataframe Frutas
        elif (menu_Entrada == 2):
           print(df_frutas.head(6)) 
           escolha_produto = 1
           while escolha_produto != 999:
                escolha_produto = int(input("Escolha um produto pelo seu inidice (999 - encerra):"))
                if escolha_produto == 999:
                   break
                else:
                    print(f'VOCÊ ESCOLHEU O PRODUTO : {df_frutas.loc[escolha_produto][0]} POR R$ {df_frutas.loc[escolha_produto][2]}.')
                    compras.append(df_frutas.loc[escolha_produto])
               
menu()
