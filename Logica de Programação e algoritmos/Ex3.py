from random import shuffle, choice  # Importei da biblioteca random duas funções para auxiliar no sorteio do vencedor
from time import sleep  # Da biblioteca time, chamei a função sleep() que faz pausas no código, e me ajudou a
# personalizar um pouco o programa.
from sys import exit  # A função exit da bibioteca sys, foi uma das formas que encontrei para finalizar o código
# independente do que viria depois, se essa função não fosse chamada o 'while True', continuaria a rodar, o que não
# faria muito sentido, pois o sorteio teria terminado, e o vencedor declarado.


def menu_adm(): # Nessa função eu elaboro um menu para o administrador do sorteio, onde so ele através de senha tem
    # acesso.
    print('1 - Embaralhar lista')
    print('2 - Verificar lista embaralhada')
    print('3 - Sortear ganhador')
    print('4 - Voltar')
    print('-*' * 40)

    select = entrada() # Select vai receber um valor válido para o menu, valor esse recebido pela função entrada() que
    # recebe um valor do usúario e verifica se ele é válido ou não.
    if select == 1: # Se select receber 1, eu irei fazer um shuffle na listaSorteio e retornarei para a função
        # menu_adm().
        shuffle(listaSorteio)
        print('-*' * 40)
        return menu_adm()
    elif select == 2: # Fiz um elif que caso select for igual a 2, faço somente o print da lista listaSorteio e
        # retorno para a função menu_adm().
        print(listaSorteio)
        return menu_adm()
    elif select == 3: # Nesse elif será feito o sorteio do vencedor, é declarado uma lista X = ['.'] e printará
        # 'SORTEANDO', logo em seguida.
        x = ['.']
        print('SORTEANDO ')
        for i in range(0, 3): # Esse for irá fazer uma pequena personalização na saída, chamei a função sleep() e
            # declarei como parâmetro 1, esse 1 corresponde ao total de segundos que o programa ficará pausado.
            # o FOR funcionará assim, quando ele passar o primeiro valor de range, o codigo irá pausar por 1s e printará
            # na tela um '.' valor correspondente a x[0], como foi colocado um end="" no print, a quebra de linha não
            # ocorrerá e o for se manterá na mesma linha. No fim o for terminará assim.
            # sleep(1)'.'sleep(1)'..'sleep(1)'...'.
            sleep(1)
            print(x[0], end="")
        sleep(1) # Pausei o codigo por 1s novamente.
        print(' O sorteado foi... ', end="") # Print um cabeçalho sem a quebra de linha.
        sleep(1) # Programa pausado novamente.
        print('{}!!! PARABÉNS!'.format(choice(listaSorteio))) # E faço o print do vencedor atraves do format que recebe
        # como valor, o valor da função choice na ListaSorteio.
        sleep(1) # Outra pausa de 1s.
        print('-*' * 40)
        print('-*' * 7, 'A EQUIPE DO CANAL AGRADECE A CONTRIBUIÇÃO DE TODOS', '-*' * 7) # Aqui é printado um cabeçalho,
        # agradecendo a todos pela contribuição
        print('-*' * 40)
        exit() # Logo após o cabeçalho eu chamo a função exit() da biblioteca sys, que irá finalizando o programa e
        # e evitando que ele volte para o while True.
    elif select == 4:
        return 0 # Caso o usúario insira 4, chamará esse elif e ele retornará 0 para a função menu_adm() e o programa
    # retornará para o while True, onde está o programa principal.


def adm(): # Essa função irá servir para que só os administradores do programa tenha acesso a função menu_adm().
    # funcionando da seguinte forma, uma senha predefinida é declarada 123. O usuário ao selecionar a opção
    # '3 - Preparar sorteio', o programa pedirá a ele que insira a senha, no IF é feito a comparação da senha entrada
    # pelo usuario e a senha predefinada, caso eles coincidirem será printado um cabeçalho informando acesso
    # liberado e logo em seguida será feito a chamada da função menu_adm(). Caso a senha informada pelo usúario não
    # for igual ele será jogado no ELSE, que retornará para o usúario a mensagem 'Senha incorreta', e ele será jogado
    # no programa principal.
    senha = 123
    print('Digite a senha para ter acesso: ')
    senhaUsu = int(input())
    if senha == senhaUsu:
        print('-*' * 40)
        print('  ' * 15, 'ACESSO LIBERADO')
        print('-*' * 40)
        menu_adm()
    else:
        print('Senha incorreta')


def entrada(): # Essa função fará a validação da entrada do usúario.
    entrada = int(input()) # O usúario entra com um valor inteiro, que servirá como parâmetro para a seleção de opções
    # no menu do programa principal e o menu da função menu_adm().
    while entrada > 4 or entrada < 1: # Nesse while é verificado se o valor inserido pelo usúario está fora do intervalo
        # aceito que seria (1, 4). Caso esteja será printado na tela 'Entrada inválida, tente novamente!' e será
        # solicitado uma nova entrada, e fazendo a comparação novamente. Caso o valor estiver dentro do intervalo
        # definido a função entrada() receberá esse valor.
        print('Entrada inválida, tente novamente!')
        entrada = int(input())
        print('--' * 40)
    return entrada


def main(): # A função main() irá trabalhar da seguinte forma, foram declaradas duas variáveis uma recebe o
    # nome da pessoa a outra o valor doado. A variável nomeDoador ao receber o nome, irá transformar todos os caracteres
    # para minúsculo com a função lower(), em seguida será excluído todos os espaços desnecessários da string com o
    # a função strip(), para fins de formatação foi chamada a função title() que irá retornar as strings com o primeiro
    # caractere maiúsculo, e por último é retornado uma lista da string recebida por nomeDoador com a função split().
    nomeDoador = str(input('Digite seu nome: ')).lower().strip().title().split()
    valorDoado = float(input('Quanto você deseja doar: '))
    print('-*' * 40)
    qtdvezes = int(valorDoado / 10) # A variável qtdvezes irá receber a quantidade de vezes que o nome do doador será
    # adicionado a lista, conforme o valor doado, que é dado pelo valor doado divido por 10.
    for i in range(qtdvezes): # Nesse FOR é feito a adição do nome do doador na lista do sorteio, o range do FOR é
        # definido através da variável que recebe a quantidade de vezes que o nome do doador será adicionado a lista,
        # fazendo assim um append do primeiro nome do doador caso ele tenha colocado nome e sobrenome na lista do
        # sorteio.
        listaSorteio.append(nomeDoador[0])
    print('Obrigado por contribuir!!') # Logo após a adição do nome na lista é printado um cabeçalho agradecendo
    # pela contribuição e mostrando também a quantidade de vezes que o nome dele foi adicionado a lista do sorteio.
    print('Seu nome foi adicionado {} vezes na lista para o sorteio.'.format(qtdvezes))
    print('-*' * 40)


listaSorteio = ['Ruth', 'Ruth', 'Maria', 'Maria', 'Maria', 'Fernando', 'Fernando',
                'Fernando', 'Fernando', 'Fernando']
# Declarei a lista, que irá receber o nome dos doadores, para efetuar o sorteio.
while True: # Para elaboração do menu principal do programa eu utilizei um while True, que ficará sempre executando,
    # caso alguma forma de interrupção não for feita.
    print('SELECIONE UMA OPÇÃO ABAIXO: ') # Nessa e nas 5 linhas abaixo, é feito o menu principal para o usúario,
    # informando o número de cada opção.
    print('1 - Fazer doação')
    print('2 - Ver lista de sorteio')
    print('3 - Preparar para sorteio')
    print('4 - Sair')
    print('-*' * 40)
    select = entrada() # A variável select irá receber o valor da função entrada(), que expliquei anteriormente como é
    # dado esse valor, correspondente a alguma opção do menu, entre (1, 4).
    if select == 1: # Somente é feita a chamada para a função main(), caso o valor do select for igual a 1.
        main()
    elif select == 2: # Caso o valor do select for igual a 2, será printado um cabeçalho e a lista contendo os
        # participantes do sorteio.
        print('-*' * 40)
        print(listaSorteio)
        print('-*' * 40)
    elif select == 3: # Se select for igual a 3, o usuário será direcionado a função adm(), onde será solicitado a ele
        # a senha de acesso para poder acessar o menu do administrador do sorteio. Senha = 123.
        adm()
    elif select == 4: # Se o usúario resolver sair do programa, será mostrado pra ele um agradecimento da equipe
        # do canal e logo em seguida é feito um break no loop while True.
        print('*-' * 40)
        print('-*' * 7, 'A EQUIPE DO CANAL AGRADECE A CONTRIBUIÇÃO DE TODOS', '-*' * 7)
        print('*-' * 40)
        break
