from numpy.core.fromnumeric import var
import pandas as pd
from reportlab.pdfgen import canvas as cv

df_folhas = pd.read_csv('Folhas_hortalicas.csv')
df_frutas = pd.read_csv('Frutas.csv')
df_C_t = pd.read_csv('Lanches_C_trigo.csv')
df_S_t = pd.read_csv('Lanches_S_trigo.csv')
df_outros = pd.read_csv('Outros.csv')
df_pasti = pd.read_csv('Pastinhas_ante.csv')
df_raizes = pd.read_csv('Raizes.csv')


def calcular_preco(quant, quantot, valortot):
    if quant < quantot:
        preco = (quant*valortot)/quantot
        return preco
    elif quant > quantot:
        preco = (quant*valortot)/quantot
        return preco
    else:
        return valortot


def cria_pdf(nome, endereço, lista_compras):
    pdf = cv.Canvas("Dados_do_Cliente.pdf")
    pdf.setTitle("Dados de entrega")
    pdf.drawString(100,800, f"Nome: {nome}.")
    pdf.drawString(100, 790, f"Endereço: {endereço}.")
    y = 750
    for chave, valor in lista_compras.items():
        pdf.drawString(100, y, f"Produto: {chave} Valor: R$ {valor[0]} Quantidade: {valor[1]}.")
        y -= 10
    soma = 0
    for valor in lista_compras.values():
        soma = soma + valor[0]
    pdf.drawString(100, 100, f"A soma dos valores dos produtos é igual a: R${soma}")
    
    pdf.save()

def menu():
    print('-='*30)
    print('OLÁ CLIENTE !! BEM-VINDO(A) A FEIRA ORGâNICA DA CIDADE')
    print('-='*30)

    print('PRIMEIRO VOU PEDIR PARA QUE SE REGISTRE.')
    nome_Cli = input("Com o seu nome: ")
    end_Cli = input("Com o seu endereço (Rua, Número, Bairro, Cidade): ")

    print('AGORA, VAMOS AS COMPRAS!')
    
    compras = {}

    menu_Entrada = 1
    while menu_Entrada != 0:
        menu_Entrada = int(input("PARA QUAL ÁREA DESEJA IR ? \n 1 - Folhas e hortaliças \n 2 - Frutas \n 3 - Lanches com trigo \n 4 - Lanches sem trigo \n 5 - Outros \n 6 - Pastinhas, antepastos e geleias. \n 7 - Raizes \n 0 - Sair \n:"))
        
        # Dataframe Folhas
        if (menu_Entrada == 1):
           print(df_folhas.head(14)) 
           escolha_produto = 1
           while escolha_produto != 999:
                escolha_produto = int(input("Escolha um produto pelo seu indice (999 - encerra):"))
                if escolha_produto == 999:
                   break
                else:
                    quanti = int(input("Agora informe a quantidade: "))
                    variavel = calcular_preco(quanti, df_folhas.loc[escolha_produto][1], df_folhas.loc[escolha_produto][2])
                    print(f'VOCÊ ESCOLHEU O PRODUTO : {df_folhas.loc[escolha_produto][0]} E FICOU POR R$ {variavel}.')
                    compras[df_folhas.loc[escolha_produto][0]] = [variavel, quanti]
        

        # Dataframe Frutas
        elif (menu_Entrada == 2):
           print(df_frutas.head(6)) 
           escolha_produto = 1
           while escolha_produto != 999:
                escolha_produto = int(input("Escolha um produto pelo seu indice (999 - encerra):"))
                if escolha_produto == 999:
                   break
                else:
                    quanti = int(input("Agora informe a quantidade: "))
                    variavel = calcular_preco(quanti, df_frutas.loc[escolha_produto][1], df_frutas.loc[escolha_produto][2])
                    print(f'VOCÊ ESCOLHEU O PRODUTO : {df_frutas.loc[escolha_produto][0]} E FICOU POR R$ {variavel}.')
                    compras[df_frutas.loc[escolha_produto][0]] = [variavel, quanti]
        
        
        # Dataframe Lanches com trigo
        elif (menu_Entrada == 3):
           print(df_C_t.head(7)) 
           escolha_produto = 1
           while escolha_produto != 999:
                escolha_produto = int(input("Escolha um produto pelo seu indice (999 - encerra):"))
                if escolha_produto == 999:
                   break
                else:
                    quanti = int(input("Agora informe a quantidade: "))
                    variavel = calcular_preco(quanti, df_C_t.loc[escolha_produto][1], df_C_t.loc[escolha_produto][2])
                    print(f'VOCÊ ESCOLHEU O PRODUTO : {df_C_t.loc[escolha_produto][0]} E FICOU POR R$ {variavel}.')
                    compras[df_C_t.loc[escolha_produto][0]] = [variavel, quanti]
        
        
        # Dataframe Lanches sem trigo
        elif (menu_Entrada == 4): 
           print(df_S_t.head(6)) 
           escolha_produto = 1
           while escolha_produto != 999:
                escolha_produto = int(input("Escolha um produto pelo seu indice (999 - encerra):"))
                
                if escolha_produto == 999:
                   break
                else:
                    quanti = int(input("Agora informe a quantidade: "))
                    variavel = calcular_preco(quanti, df_S_t.loc[escolha_produto][1], df_S_t.loc[escolha_produto][2])
                    print(f'VOCÊ ESCOLHEU O PRODUTO : {df_S_t.loc[escolha_produto][0]} E FICOU POR R$ {variavel}.')
                    compras[df_S_t.loc[escolha_produto][0]] = [variavel, quanti]


        # Dataframe Outros
        elif (menu_Entrada == 5): 
           print(df_outros.head(24)) 
           escolha_produto = 1
           while escolha_produto != 999:
                escolha_produto = int(input("Escolha um produto pelo seu indice (999 - encerra):"))
                if escolha_produto == 999:
                   break
                else:
                    quanti = int(input("Agora informe a quantidade: "))
                    variavel = calcular_preco(quanti, df_outros.loc[escolha_produto][1], df_outros.loc[escolha_produto][2])
                    print(f'VOCÊ ESCOLHEU O PRODUTO : {df_outros.loc[escolha_produto][0]} E FICOU POR R$ {variavel}.')
                    compras[df_outros.loc[escolha_produto][0]] = [variavel, quanti]


        # Dataframe Pastinhas, antepastos e geleias.
        elif (menu_Entrada == 6): 
           print(df_pasti.head(8)) 
           escolha_produto = 1
           while escolha_produto != 999:
                escolha_produto = int(input("Escolha um produto pelo seu indice (999 - encerra):"))
                if escolha_produto == 999:
                   break
                else:
                    quanti = int(input("Agora informe a quantidade: "))
                    variavel = calcular_preco(quanti, df_pasti.loc[escolha_produto][1], df_pasti.loc[escolha_produto][2])
                    print(f'VOCÊ ESCOLHEU O PRODUTO : {df_pasti.loc[escolha_produto][0]} E FICOU POR R$ {variavel}.')
                    compras[df_pasti.loc[escolha_produto][0]] = [variavel, quanti]

        
        # Dataframe Raizes
        elif (menu_Entrada == 7): 
           print(df_raizes.head(8)) 
           escolha_produto = 1
           while escolha_produto != 999:
                escolha_produto = int(input("Escolha um produto pelo seu indice (999 - encerra):"))
                if escolha_produto == 999:
                   break
                else:
                    quanti = int(input("Agora informe a quantidade: "))
                    variavel = calcular_preco(quanti, df_raizes.loc[escolha_produto][1], df_raizes.loc[escolha_produto][2])
                    print(f'VOCÊ ESCOLHEU O PRODUTO : {df_raizes.loc[escolha_produto][0]} E FICOU POR R$ {variavel}.')
                    compras[df_raizes.loc[escolha_produto][0]] = [variavel, quanti]

        cria_pdf(nome_Cli, end_Cli, compras)


menu()