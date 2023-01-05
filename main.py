print("""Bem vindo ao pedra, papel e tesoura de terminal.
Para jogar é muito simples basta seguir as instruções abaixo:
    [0]Pedra
    [1]Papel
    [2]Tesoura
Você vai jogar com a maquina, acha que consegui me vencer?""")

import random
from time import sleep

total_computador = 0
total_usuario = 0
empate = 0

while True:

    usuario = input("Qual a jogada? ")

    computador = random.randint(0,2)
    

    if computador == 0:
        # print("computador escolheu Pedra")
        if usuario == '0':
            empate += 1
            print("Empate")
        elif usuario == '1':
            total_usuario -= 1
            print("Computador ganha!")
        elif usuario == '2':
            total_computador += 1
            print("Computador venceu!")
        elif usuario == 'sair':
            print("Saindo...")
            sleep(3)
            break
        elif usuario != computador:
            print("Opção inválida")
        

    elif computador == 1:
        # print("Computador jogou Papel")
        if usuario == '0':
            computador -= 1
            print("Você ganha!")
        elif usuario == '1':
            empate += 1
            print("Empate")
        elif usuario == '2':
            total_usuario += 1
            print("Jogador venceu!")
        elif usuario == 'sair':
            print("Saindo...")
            sleep(3)
            break
        elif usuario != computador:
            print("Opção inválida")
        

    elif computador == 2:
        if usuario == '0':
            total_usuario += 1
            print("Jogador venceu!")
        elif usuario == '1':
            total_computador += 1
            print("Computador venceu!")
        elif usuario == '2':
            empate += 1
            print("Empate")
        elif usuario == 'sair':
            print("Saindo...")
            sleep(3)
            break
        elif usuario != computador:
            print("Opção inválida")
        
print(f'''
TOTAL DA PARTIDA:
    Jogador = {total_usuario}
    Compuatdor = {total_computador}
    Empate = {empate}
''')

if total_computador > total_usuario:
    print("Computador venceu!")
elif total_usuario > total_computador:
    print("Jogador venceu!")