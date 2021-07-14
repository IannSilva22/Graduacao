# Primeiro foi declarado uma variável para a string '@algoritmos.com.br', logo em seguida é pedido ao usuário que
# insira seu nome, note que foram chamadas três funções, lower() que irá transformar toda o input do usuário
# em minúsculo caso ele entre com algum caractere maiúisculo, na função strip() será eliminado todos os espaços
# desnecessários, caso ela não fosse declarada o programa não funcionaria da maneira correta, a função split()
# irá retornar uma lista da string, como não foi declarado um separador, ela separará a string sempre que um espaço ' '
# for identificado, exemplo, pegando como input 'Iann Oliveira Silva' o output seria ['Iann', 'Oliveira, 'Silva'],
# e por ultimo é solicitado ao usuário que informe seu RU.
def email_aluno():
    nomeReservado = str()  # Uma variável string que declarei e deixei vazia, para utilizar como reserva do nome do
    # usuário.
    padrao = '@algoritmos.com.br'
    nome = input('Digite seu nome e sobrenome: ').lower().strip().split()
    ru = input('Digite seu RU: ')
    aluno = nome[0][0] + nome[1]  # aluno receberá como valor a primeira letra da primeira string da lista nome[0][0] e
    # fará a concatenação com a segunda string da lista na posição nome[1].
    posiRU = ru[len(ru) - 2]  # Nesse momento len irá fazer a contagem da variavel RU, encontrado o tamanho da variável,
    # logo após é subtraído 2, encontrando assim a penúltima posição do RU do aluno, posiRU recebe o valor
    # referente a penúltima posição.
    posiRU_dois = ru[len(ru) - 1]  # Aqui é encontrado a última posição do RU e o seu valor é atribuído a posiRU_dois.
    email = aluno + posiRU + posiRU_dois + padrao  # Nessa linha será feita apenas a concatenação de todos os elementos
    # encontrados aluno+posiRU+posiRU_dois+padrao.
    for i in range(len(nome)):  # Fiz um FOR que usará o tamanho da lista nome como range, usando a função len. A cada
        # instância do FOR nomeReservado receberá o valor de nome na posição i e logo em seguida acréscentrara um
        # espaço ' ' entre os valores recebidos pois foram recebidos como string e para evitar que fiquem colados,
        # utilizei esse artificio.
        nomeReservado += nome[i]
        nomeReservado += ' '
    nomePrint = nomeReservado.strip().title() # Depois do for, eu atribui como valor para a variável nomePrint, a
    # variável nomeReservado chamando as funções strip() para eliminar o ultimo espaço ' ' e a função title(), que irá
    # retornar maiúsculo os primeiros caracteres de cada string.
    print('Sr(a) {}, seu email é {} '.format(nomePrint, email)) # Esse é o ultimo print, que usando a função format
    # e utilizando como parametros as variaveis nomePrint e email para reproduzir na tela a frase completa do exércicio.


email_aluno()  # Linha que somente irá chamar a função.
