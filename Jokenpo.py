import random as rd

print('*=' * 17)
print('BEM-VINDO(A) AO JOGO JOKENPO !!!')
print('*=' * 17)

print("\n")
jogadorN = input('Qual o nome do jogador? ')
print("\n")

pontosMaq = 0
pontosJog = 0
while (pontosMaq <= 2) and (pontosJog <= 2):
    opcao = ('Pedra', 'Papel', 'Tesoura')
    maquina = rd.randint(0, 2)
    
    print("OPÇÕES PARA O JOGADOR")
    print("0 - PEDRA / 1 - PAPEL / 2 - TESOURA")
    jogadorOp = int(input(f'Qual opção você vai escolher? '))
    print("\n")

    print(f'{jogadorN} escolheu {opcao[jogadorOp]}')
    print(f'A máquina escolheu {opcao[maquina]} \n')


    if maquina == 0: # Máquina é pedra
        if jogadorOp == 0: # Jogador é pedra
            print("EMPATOU COM A MÁQUINA \n")
            pontosMaq += 0
            pontosJog += 0
        elif jogadorOp == 1: # Jogador é papel
            print(f"{jogadorN} GANHOU PARA A MÁQUINA. \n")
            pontosMaq += 0
            pontosJog += 1
        elif jogadorOp == 2: # Jogador é tesoura
            print(f"{jogadorN} PERDEU PARA A MÁQUINA. \n")
            pontosMaq += 1
            pontosJog += 0
        else:
            print('Número inválido!!')
    elif maquina == 1: # Máquina é papel
        if jogadorOp == 0: # Jogador é pedra
            print(f"{jogadorN} PEDEU PARA A MÁQUINA. \n")
            pontosMaq += 1
            pontosJog += 0
        elif jogadorOp == 1: # Jogador é papel
            print(f"EMPATOU COM A MÁQUINA \n")
            pontosMaq += 0
            pontosJog += 0
        elif jogadorOp == 2: # Jogador é tesoura
            print(f"{jogadorN} GANHOU PARA A MÁQUINA. \n")
            pontosMaq += 0
            pontosJog += 1
        else:
            print('Número inválido!!')
    elif maquina == 2: # Máquina é tesoura
        if jogadorOp == 0: # Jogador é pedra
            print(f"{jogadorN} GANHOU PARA A MÁQUINA. \n")
            pontosMaq += 0
            pontosJog += 1
        elif jogadorOp == 1: # Jogador é papel 
            print(f"{jogadorN} PEDEU PARA A MÁQUINA. \n")
            pontosMaq += 1
            pontosJog += 0
        elif jogadorOp == 2: # Jogador é tesoura
            print("EMPATOU COM A MÁQUINA \n")
            pontosMaq += 0
            pontosJog += 0
        else:
            print('Número inválido!!')


    if (pontosJog == 2) and (pontosMaq == 0):
        print(f"ACABOU O JOGO 2X0 PARA {jogadorN}!!")
        break
    elif (pontosMaq == 2) and (pontosJog == 0):
        print(f"ACABOU O JOGO 2X0 PARA A MÁQUINA !!")
        break

    print(f'{jogadorN} : {pontosJog} X Máquina : {pontosMaq} \n')
