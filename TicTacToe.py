import random
import time
from os import system, name

valores = [0,0,0,0,0,0,0,0,0]
valores_2 = []
conta_vez = 0
primeira_vez = 0

def clear():
    if name == 'nt':
        _ = system('cls')

def regras():
    print("\t===========")
    print("\t1 | 2 | 3")
    print("\t4 | 5 | 6")
    print("\t7 | 8 | 9")
    print("\t===========")

def reiniciar():
    global valores, conta_vez, lado_jogador
    if primeira_vez==0:
        verifica = "y"
    else:
        verifica = input("Deseja reiniciar? y/n \t")
    if verifica == "y" or verifica == "Y":
        clear()
        regras()
        valores = [0,0,0,0,0,0,0,0,0]
        conta_vez = 0
        sel_dif_bot()
        if sel_bot!=0:
            lado_jogador = input("Escolha o lado que deseja jogar (x/o):")            
            if lado_jogador == "o" or lado_jogador == "O":
                lado_jogador = 2
            else:
                lado_jogador = 1
    else:
        exit()

def turno():
    global vez, zev, vez_forma
    #Verifica quem é o jogador nessa rodada
    vez = conta_vez%2+1
    
    if vez==1:
        vez_forma = "x"
        zev = 2
    elif vez==2:
        vez_forma = "o"
        zev = 1

def jogada():
    global novo, valores, conta_vez
    #Recebe a jogada
    if sel_bot==0 or vez == 1 == lado_jogador or vez == 2 == lado_jogador:
        novo = int(input("Digite a posição do seu próximo movimento: "))-1

    elif sel_bot==1:
        novo = random.randint(0,8)
    elif sel_bot==2:
        bot_medio()
    elif sel_bot==3:
        bot_dificil()
    elif sel_bot==4:
        bot_impossivel()

    #Verifica se é um movimento legal e muda na lista valores
    if valores[novo] == 0:
        valores[novo] = vez
        conta_vez += 1
    elif valores[novo] != 0:
        jogada()
    time.sleep(0.2)

def winner():
        #Verifica se algum jogador venceu a rodada
    for i in range(0,7,3):
        if valores[i]==valores[i+1]!=0 and valores[i]==valores[i+2]!=0:
            win()
    for i in range(3):
        if valores[i]==valores[i+3]!=0 and valores[i]==valores[i+6]!=0:
            win()
    if valores[0]==valores[4]!=0 and valores[0]==valores[8]!=0 and valores[0]!=0:
            win()
    if valores[2]==valores[4]!=0 and valores[2]==valores[6]!=0:
            win()

def win():
    print("O vencedor da parida é:", vez_forma)
    screen()
    reiniciar()

def tie():
    acum = 0
    #verificar se o tabuleiro está cheio
    for j in valores:
        if j != 0:
            acum+=1
    if acum==9:
        print('A rodada terminou em empate')
        screen()
        reiniciar()

def screen():
    desenho = []

    #atribui x e o
    for n in range(9):
        if valores[n]==1:
            desenho.append("x")
        elif valores[n]==2:
            desenho.append("o")
        else:
            desenho.append(" ")

    #Desenha graficamente o jogo
    print("===========")
    print(desenho[0],'|',desenho[1],'|',desenho[2])
    print(desenho[3],'|',desenho[4],'|',desenho[5])
    print(desenho[6],'|',desenho[7],'|',desenho[8])
    print("===========")

def sel_dif_bot():
    global sel_bot   
    sel_bot = 0 
    sel_bot = (input('''Selecione o nível do bot:
    (0 - sem bot, 2 players)
    (1 - bot fácil)
    (2 - bot médio)
    (3 - bot difícil)
    (4 - bot impossível)
    '''))
    try:
        sel_bot = int(sel_bot)
    except ValueError:
        sel_bot = 1

def bot_medio():
    global novo
    #inimigo
    novo = random.randint(0,8)
    #Valores verticais
    for i in range(0,7,3):
        if (valores[i]==valores[i+1]==zev or valores[i]==valores[i+2]==zev or valores[i+1]==valores[i+2]==zev):
            for n in range(i,i+3,1):
                if valores[n]==0:
                    novo = n 
    #Valores horizontais
    for i in range(3):
        if (valores[i]==valores[i+3]==zev or valores[i]==valores[i+6]==zev or valores[i+3]==valores[i+6]==zev):
            for n in range(i,i+7,3):
                if valores[n]==0:
                    novo = n
    #Valores diagonais
    if valores[0]==valores[4]==zev or valores[0]==valores[8]==zev or valores[4]==valores[8]==zev:
        for n in range(0,9,4):
            if valores[n]==0:
                novo = n
    if valores[2]==valores[4]==zev or valores[2]==valores[6]==zev or valores[4]==valores[6]==zev:
        for n in range(2,7,2):
            if valores[n]==0:
                novo = n
   
    #aliados
    #Valores verticais
    for i in range(0,7,3):
        if (valores[i]==valores[i+1]==vez or valores[i]==valores[i+2]==vez or valores[i+1]==valores[i+2]==vez):
            for n in range(i,i+3):
                if valores[n]==0:
                    novo = n 
    #Valores horizontais
    for i in range(3):
        if (valores[i]==valores[i+3]==vez or valores[i]==valores[i+6]==vez or valores[i+3]==valores[i+6]==vez):
            for n in range(i,i+7,3):
                if valores[n]==0:
                    novo = n
    #Valores diagonais
    if valores[0]==valores[4]==vez or valores[0]==valores[8]==vez or valores[4]==valores[8]==vez:
        for n in range(0,9,4):
            if valores[n]==0:
                novo = n
    if valores[2]==valores[4]==vez or valores[2]==valores[6]==vez or valores[4]==valores[6]==vez:
        for n in range(2,7,2):
            if valores[n]==0:
                novo = n

def bot_dificil():
    global novo
    #inimigo
    if valores[4]==0:
        novo = 4
    elif valores[0]==0 or valores[2]==0 or valores[6]==0 or valores[8]==0:
        novo = random.choice([0,2,6,8])
    elif True:
	    novo = random.randint(0,8) 
    #Valores verticais
    for i in range(0,7,3):
        if (valores[i]==valores[i+1]==zev or valores[i]==valores[i+2]==zev or valores[i+1]==valores[i+2]==zev):
            for n in range(i,i+3,1):
                if valores[n]==0:
                    novo = n 
    #Valores horizontais
    for i in range(3):
        if (valores[i]==valores[i+3]==zev or valores[i]==valores[i+6]==zev or valores[i+3]==valores[i+6]==zev):
            for n in range(i,i+7,3):
                if valores[n]==0:
                    novo = n
    #Valores diagonais
    if valores[0]==valores[4]==zev or valores[0]==valores[8]==zev or valores[4]==valores[8]==zev:
        for n in range(0,9,4):
            if valores[n]==0:
                novo = n
    if valores[2]==valores[4]==zev or valores[2]==valores[6]==zev or valores[4]==valores[6]==zev:
        for n in range(2,7,2):
            if valores[n]==0:
                novo = n
   
    #aliados
    #Valores verticais
    for i in range(0,7,3):
        if (valores[i]==valores[i+1]==vez or valores[i]==valores[i+2]==vez or valores[i+1]==valores[i+2]==vez):
            for n in range(i,i+3):
                if valores[n]==0:
                    novo = n 
    #Valores horizontais
    for i in range(3):
        if (valores[i]==valores[i+3]==vez or valores[i]==valores[i+6]==vez or valores[i+3]==valores[i+6]==vez):
            for n in range(i,i+7,3):
                if valores[n]==0:
                    novo = n
    #Valores diagonais
    if valores[0]==valores[4]==vez or valores[0]==valores[8]==vez or valores[4]==valores[8]==vez:
        for n in range(0,9,4):
            if valores[n]==0:
                novo = n
    if valores[2]==valores[4]==vez or valores[2]==valores[6]==vez or valores[4]==valores[6]==vez:
        for n in range(2,7,2):
            if valores[n]==0:
                novo = n
            
def bot_impossivel():
    global novo
    #inimigo
    if (valores[0]==valores[8]!=0 and conta_vez<=3) or (valores[2]==valores[6]!=0 and conta_vez<=3):
        novo = random.choice([1,3,5,7]) 
    elif valores[4]==0:
        novo = 4
    elif valores[0]==0 or valores[2]==0 or valores[6]==0 or valores[8]==0:
        novo = random.choice([0,2,6,8])
    elif True:
        novo = random.randint(0,8) 
    #Valores verticais
    for i in range(0,7,3):
        if (valores[i]==valores[i+1]==zev or valores[i]==valores[i+2]==zev or valores[i+1]==valores[i+2]==zev):
            for n in range(i,i+3,1):
                if valores[n]==0:
                    novo = n 
    #Valores horizontais
    for i in range(3):
        if (valores[i]==valores[i+3]==zev or valores[i]==valores[i+6]==zev or valores[i+3]==valores[i+6]==zev):
            for n in range(i,i+7,3):
                if valores[n]==0:
                    novo = n
    #Valores diagonais
    if valores[0]==valores[4]==zev or valores[0]==valores[8]==zev or valores[4]==valores[8]==zev:
        for n in range(0,9,4):
            if valores[n]==0:
                novo = n
    if valores[2]==valores[4]==zev or valores[2]==valores[6]==zev or valores[4]==valores[6]==zev:
        for n in range(2,7,2):
            if valores[n]==0:
                novo = n

    #aliados
    #Valores verticais
    for i in range(0,7,3):
        if (valores[i]==valores[i+1]==vez or valores[i]==valores[i+2]==vez or valores[i+1]==valores[i+2]==vez):
            for n in range(i,i+3):
                if valores[n]==0:
                    novo = n 
    #Valores horizontais
    for i in range(3):
        if (valores[i]==valores[i+3]==vez or valores[i]==valores[i+6]==vez or valores[i+3]==valores[i+6]==vez):
            for n in range(i,i+7,3):
                if valores[n]==0:
                    novo = n
    #Valores diagonais
    if valores[0]==valores[4]==vez or valores[0]==valores[8]==vez or valores[4]==valores[8]==vez:
        for n in range(0,9,4):
            if valores[n]==0:
                novo = n
    if valores[2]==valores[4]==vez or valores[2]==valores[6]==vez or valores[4]==valores[6]==vez:
        for n in range(2,7,2):
            if valores[n]==0:
                novo = n

reiniciar()

primeira_vez = 1

#main loop
while True:
    #Verifica quem é o jogador nessa rodada
    turno()

    #colocar a tela
    screen()

    if vez==2 and sel_bot!=0:        
        print("Turno da máquina")

    #Faz a jogada do jogador ou do bot
    jogada()

    #Verifica se alguem venceu
    winner()

    #Verifica se empatou
    tie()
