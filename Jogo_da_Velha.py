# Variaveis Globais
import random

# Variaveis globais em comum para Modo 1 e 2
rodadas = 0
tipo_vitoria = None
fim_jogo = False
formato_jogo = ["-","-","-",
                "-","-","-",
                "-","-","-"]

# Variaveis globais p/ Modo 2
jogador_1 = "X"
jogador_2 = "O"
contador_jogador = 0
jogador_atual = None
posicao_modo1 = 0

# Variaveis globais p/ Modo 2
posicoes_disponiveis =[1, 2, 3, 4, 5, 6, 7, 8, 9]
posicao_modo2 = 0

# Algoritimos em Comum para Modo 1 e 2
def tela():
    print(formato_jogo[0] + " | " + formato_jogo[1] + " | " + formato_jogo[2])
    print(formato_jogo[3] + " | " + formato_jogo[4] + " | " + formato_jogo[5])
    print(formato_jogo[6] + " | " + formato_jogo[7] + " | " + formato_jogo[8])
    return

def vitoria ():
    colunas()
    linhas()
    diagonais()
    return

def colunas():
    global tipo_vitoria
    global fim_jogo

    coluna1 = formato_jogo[0] == formato_jogo[3] == formato_jogo[6] != "-"
    coluna2 = formato_jogo[1] == formato_jogo[4] == formato_jogo[7] != "-"
    coluna3 = formato_jogo[2] == formato_jogo[5] == formato_jogo[8] != "-"

    if coluna1 or coluna2 or coluna3:
        tipo_vitoria = 'por coluna.'
        fim_jogo = True
    return

def linhas():
    global tipo_vitoria
    global fim_jogo

    linha1 = formato_jogo[0] == formato_jogo[1] == formato_jogo[2] != "-"
    linha2 = formato_jogo[3] == formato_jogo[4] == formato_jogo[5] != "-"
    linha3 = formato_jogo[6] == formato_jogo[7] == formato_jogo[8] != "-"

    if linha1 or linha2 or linha3:
        tipo_vitoria = 'por linha.'
        fim_jogo = True

    return

def diagonais():
    global tipo_vitoria
    global fim_jogo

    diagonal1 = formato_jogo[0] == formato_jogo[4] == formato_jogo[8] != "-"
    diagonal2 = formato_jogo[6] == formato_jogo[4] == formato_jogo[2] != "-"

    if diagonal1 or diagonal2:
        tipo_vitoria = 'por diagonal.'
        fim_jogo = True
    return

def reiniciar_variaveis():
    global fim_jogo
    global rodadas
    global formato_jogo
    global jogador_atual
    global posicoes_disponiveis
    global posicao_modo2

    # Comuns
    fim_jogo = False
    rodadas = 0
    formato_jogo = ["-", "-", "-",
                    "-", "-", "-",
                    "-", "-", "-"]
    # Modo 1
    jogador_atual = 0

    # Modo 2
    posicoes_disponiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    posicao_modo2 = 0

# Modo 1 - Player vs Player
def jogador_x_jogador():

    global rodadas
    global jogador
    global formato_jogo
    global fim_jogo
    global contador_jogador
    global jogador_atual
    while fim_jogo == False or rodadas > 9:
        tela()
        rodar_turnopvp()
        rodadas = rodadas + 1
        contador_jogador = contador_jogador + 1
        vitoria()

    tela()
    print('Vitória ' + tipo_vitoria)
    print('Parabéns!! Jogador ' + jogador_atual )

    reiniciar_variaveis()

    while True:
        jogar_novamente = str(input('Querem jogar de novo? S/N ... '))
        if jogar_novamente.upper() == 'S':
            jogador_x_jogador()
        elif jogar_novamente.upper() == 'N':
            escolher_modo()

def rodar_turnopvp():
   global posicao_modo1
   global jogador_atual
   global contador_jogador

   if (contador_jogador % 2) == 0:
       jogador_atual = jogador_1
   else:
       jogador_atual = jogador_2

   print('Turno de ' + jogador_atual)
   posicao_modo1 = int(input('Escolha uma posição ainda não ocupada entre 1 - 9 ... '))
   posicao_modo1 = (posicao_modo1 - 1)

   if formato_jogo[posicao_modo1] == "X" or formato_jogo[posicao_modo1] == "O":
       tela()
       rodar_turnopvp()
   else:
       formato_jogo[posicao_modo1] = jogador_atual
   return

# Modo 2 - IA vs Player
def jogandor_vs_ia():
    global posicao_modo2
    global posicoes_disponiveis
    global rodadas
    global formato_jogo
    global fim_jogo

    while fim_jogo == False or rodadas > 9:
        tela()
        turno_Player()
        vitoria()
        rodadas = rodadas + 1
        if fim_jogo == True:
            break
        turno_IA()
        rodadas = rodadas + 1
        vitoria()

    tela()
    reiniciar_variaveis()
    while True:
        jogar_novamente = str(input( "Quer jogar de novo?(S/N)"))

        if jogar_novamente.upper() == 'S':
            jogandor_vs_ia()
        elif jogar_novamente.upper() == 'N':
            escolher_modo()

def turno_Player():
    global posicao_modo2
    global posicoes_disponiveis

    print('Turno do Player')
    posicao_modo2 = int(input('Escolha uma posição ainda não ocupada entre 1 - 9 ... '))
    posicao_modo2 -= 1

    if formato_jogo[posicao_modo2] == "X" or formato_jogo[posicao_modo2] == "O":
        tela()
        turno_Player()
    else:
        formato_jogo[posicao_modo2] = "X"
    return

def turno_IA():
    global posicao_modo2
    global posicoes_disponiveis

    posicao_modo2 = random.choice(posicoes_disponiveis)

    if formato_jogo[posicao_modo2] == "X" or formato_jogo[posicao_modo2] == "O":
        turno_IA()
    else:
        formato_jogo[posicao_modo2] = "O"
    return

# Iniciar - Roda o jogo
def iniciar():
    print('Bem Vindo! Este é o meu jogo da Velha!')
    escolher_modo()

def escolher_modo():
    while True:
        print('(Para sair, escreva QUIT)')
        modo_de_jogo = str(input('Você quer jogar no modo multiplayer local ou contra a IA? (LOCAL/IA) ... '))
        if modo_de_jogo.upper() == 'LOCAL':
            jogador_x_jogador()

        elif modo_de_jogo.upper() == 'IA':
            jogandor_vs_ia()

        elif modo_de_jogo.upper() == "QUIT":
            print("O algoritimo deste jogo foi desenvolvido por Gabriel Galvão de Lacerda.")
            quit()

iniciar()