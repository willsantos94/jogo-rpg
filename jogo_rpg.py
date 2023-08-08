#Willian Ferreira Santos
#25/11/22
#Batalha dos guerreiros
#Ultima alteração 06/08/23

import random
from time import sleep

jogadores = []
temporario = []
nome1 = nome2 = ''
hp1 = hp2 = 0
forca1 = forca2 = 0
cont = 1
round = 0

while cont <= 2:
    nome = str(input(f'Jogador {cont}: ')).title()
    hp = random.randrange(10, 20)
    forca = random.randrange(5, 15)
    jogadores.append([nome, [hp, forca]])
    cont += 1
print('BEM VINDO AO BATALHA DE HERÓIS')
print('-_' * 20)
print(f'{jogadores[0][0]} <VS> {jogadores[1][0]}')

nome1 = (jogadores[0][0])  #player 1
hp1 = (jogadores[0][1][0]) # hp 1
forca1 = (jogadores[0][1][1]) # forca 

nome2 = (jogadores[1][0]) # player 2
hp2 = (jogadores[1][1][0]) # hp 2
forca2 = (jogadores[1][1][1]) # forca 

print(f'{nome1} possui Hp {hp1} e FORÇA {forca1}')
print(f'{nome2} possui Hp {hp2} e FORÇA {forca2}')
print('-_' * 20)

while True:
    round += 1
    print(f'Round {round}: ', end='')
    n = random.randint(1, 4)
    sleep(1)
    if n == 1:
        sleep(1)
        print(f'{nome1} acertou em cheio!! {nome2} perdeu o rumo de casa!')
        sleep(1)
        print('VLAAAAAAU!!')
        sleep(1)
        hp2 = hp1 - forca2
        print(f'{nome1} possui Hp {hp1} e FORÇA {forca1}')
        print(f'{nome2} possui Hp {hp2} e FORÇA {forca2}')
        if hp1 <= 0:
            sleep(1)
            print('-_' * 20)
            print(f'{nome2} GANHOU A BATALHA APÓS {round} ROUNDS')
            break
        elif hp2 <= 0:
            sleep(1)
            print('-_' * 20)
            print(f'{nome1} GANHOU A BATALHA APÓS {round} ROUNDS')
            break
    
    if n == 2:
        sleep(1)
        print(f'{nome2} acertou um belo golpe!! {nome1} saiu catando cavaco!')
        sleep(1)
        print('VLAAAAAAU!!')
        sleep(1)
        hp1 = hp2 - forca1
        print(f'{nome1} possui Hp {hp1} e FORÇA {forca1}')
        print(f'{nome2} possui Hp {hp2} e FORÇA {forca2}')
            
        if hp2 <= 0:
            print('-_' * 20)
            print(f'{nome1} GANHOU A BATALHA APÓS {round} ROUNDS')
            break
        elif hp1 <= 0:
            sleep(1)
            print('-_' * 20)
            print(f'{nome2} GANHOU A BATALHA APÓS {round} ROUNDS')
            break

    if n == 3:
        sleep(1)
        print(f'{nome2} tomou poção de ENERGIA')
        sleep(1)
        print('Ahh que refrescante')
        hp2 += random.randrange(1, 6)
        sleep(1)
        print(f'{nome1} possui Hp {hp1} e FORÇA {forca1}')
        print(f'{nome2} possui Hp {hp2} e FORÇA {forca2}')
        sleep(1)
    
    if n == 4:
        sleep(1)
        print(f'Eles ficaram se olhando')
        sleep(1)
        print('... e não fizeram nada.')
    print('-_' * 20)
print()
print('GAME OVER')

