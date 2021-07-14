def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def sair():
    return 0

def menu_principal(opç = 0): # Função que chama o menu principal novamente caso o usuario queira
    print('------------------Menu Principal------------------')
    print('1 - Videogames')
    print('2 - Jogos')
    print('3 - Listar Videogames e Jogos')
    print('4 - Sair do programa')
    print('-'*51)
    opç = int(input())
    if opç == 1: #chama a função com o menu de videogames
        menu_videogames() 
    elif opç == 2: # chama a função com o menu de jogos
        menu_jogos()
    elif opç == 3:
        menu_JV()
    elif opç == 4: # chama a função para sair do programa
        sair()
        
def menu_videogames(opç = 0): #menu dos videogames
    print('------------------Menu Videogames------------------')
    print('1 - Cadastrar videogame')
    print('2 - Listar videogame')
    print('3 - Remover videogame')
    print('4 - Voltar')
    print('5 - Sair do programa')
    print('-'*50)
    opç = int(input())
    if opç == 1:   # chama a função que cadastra os videogames na lista
        cad_videogames()
    elif opç == 2: # chama a função que mostra a lista de videogames 
        list_videogames()
    elif opç == 3: # chama a função que remove videogames da lista
        remove_videogames()
    elif opç == 4: # chama a função que retorna ao menu principal
        menu_principal()
    elif opç == 5: # chama a função que sai do programa
        sair()
        
def menu_jogos(opç = 0):
    print('------------------Menu Jogos------------------')
    print('1 - Cadastrar jogo')
    print('2 - Listar jogos')
    print('3 - Remover jogos')
    print('4 - Voltar')
    print('5 - Sair do programa')
    print('-'*50)
    opç = int(input())
    if opç == 1:
        cad_jogos()
    elif opç == 2:
        list_jogos()
    elif opç == 3:
        remove_jogos()
    elif opç == 4:
        menu_principal()
    elif opç == 5:
        sair()

def menu_JV():
    print('Seus Videogames {}'.format(jogos))
    print('Seus jogos {}'.format(videogames))
    return menu_principal()
    
def cad_videogames():
    videogames.append(str(input('Digite o videogame a ser adicionado: ')))
    return menu_videogames()

def list_videogames():
    print(videogames)
    return menu_videogames()

def remove_videogames():
    videogames.remove(input('Digite o nome do videogame a ser removido: '))
    return menu_videogames()

def cad_jogos():
    jogos.append(str(input('Digite o jogo a ser adicionado: ')))
    return menu_jogos()

def list_jogos():
    print(jogos)
    return menu_jogos()

def remove_jogos():
    jogos.remove(input('Digite o nome do jogo a ser removido: '))
    return menu_jogos()

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))
    
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
#PROGRAMA PRINCIPAL

arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo Localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)
    
videogames = []
jogos = []
JV = []

while True:
    print('------------------Menu Principal------------------')
    print('Digite o valor correspondente a opção')
    print('1 - Videogames')
    print('2 - Jogos')
    print('3 - Listar Videogames e Jogos')
    print('4 - Sair do programa')
    print('-'*51)
    menu = valida_int('Menu: ', 1, 4)
    if menu == 1:
        menu_videogames()
    elif menu == 2:
        menu_jogos()
    elif menu == 3:
        sair()
