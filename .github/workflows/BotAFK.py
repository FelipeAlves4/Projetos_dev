#importando as blibiotecas que seram usadas 
import pyautogui as py
import random 
import time 

#criando a condição para sempre rodar o codigo 
while True: 
    x = random.randint(500,700)
    y = random.randint(100,1000)
    py.moveTo(x,y,0.5) #comando para mover o mouse nas direções x e y em 0,5 segundos 
    time.sleep(random.random()*2) #o tempo será gerando em um numero aleatorio e será multiplicado por 2
