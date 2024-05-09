from random import randint
from time import sleep 
itens = ("Pedra", "Papel", "Tesoura")
comp = randint(0, 2)
print("""Sua opçãos 
      [0] Pedra 
      [1] Papel
      [2] Tesoura""")
jogador = int(input("Qual sua jogada? "))
sleep(1)
print("JO")
sleep(1)
print("KE")
sleep(1)
print("PO!!!")
sleep(1)
print("-="* 12)
print(f"Computador jogou {itens[comp]}")
print(f"Jogador jogou {itens[jogador]}")
print("-="*12)

if comp == 0:  #Computador jogou PEDRA
    if jogador == 0: 
        print("Empate")
    elif jogador == 1: 
        print("Jogador Vence")
    elif jogador == 2:
        print("Computador Vence")
    else:
        print("JOGADA INVALIDA")
if comp == 1:   #Computador jogou PAPEL
    if jogador == 0: 
        print("Computador Vence")
    elif jogador == 1: 
        print("Empate")
    elif jogador == 2:
       print("Jogador Vence")

    else:
     print("JOGADA INVALIDA")

if comp == 2:   #Computador jogou TESOURA
    if jogador == 0: 
        print("Jogador Vence")
    elif jogador == 1: 
        print("Computador Vence")
    elif jogador == 2:
        print("Empate")
    else:
     print("JOGADA INVALIDA")

