from operator import itemgetter  # É feito a importação do método itemgetter da biblioteca operator, método esse que

# servirá para ordenar a lista com base no value da key codigo.

listaTemporaria = []  # Declarei uma lista vazia, que irá receber o dicionário do usuário contendo as keys e values na
# sequência das entradas.
print('-*' * 42)
print('-*' * 10, 'CADASTRO DE PRODUTOS E CONTROLE DE ESTOQUE',
      '-*' * 10)  # Apenas um cabeçalho para o programa ficar mais
# intuitivo
print('-*' * 10, ' Entre com código 0 para sair do programa ', '-*' * 10)
while True:  # Parte principal do programa, onde eu coloquei em um loop com while True, que o usuário somente sairá do
    # loop caso ele entre com o valor 0 para a variável código, caso contrário será sempre solicitado a ele que informe
    # um valor para a variável codigo e os values para as keys estoque e minimo.
    print('-*' * 42)
    codigo = int(input('Digite o codigo do produto: '))  # Variável codigo que receberá algum valor do usuário, valor
    # esse que será adicionado a key 'codigo' no dicionário caso a condição não for suprida, caso a entrada do usuário
    # for barrada pelo IF o programa será interrompido pelo comando BREAK.
    if codigo == 0:
        break
    leituraDicio = {'codigo': codigo,  # leituraDicio será o dicionário que receberá os values pelo usuário para a keys
                    # predefinidas, exceto a key codigo que receberá como value o valor da variavel codigo, inserida e
                    # testada anteriormente  pelo IF.
                    'estoque': int(input('Digite a quantidade em estoque: ')),
                    'minimo': int(input('Informe a quantidade mínima no estoque: '))}

    listaTemporaria.append(leituraDicio)  # Nesta linha do programa, chamei a listaTemporaria[] que até o momento estava
    # vazia e chamei também a função append que irá adicionar no final dessa lista um novo dicionário a cada passagem do
    # while.
print('Lista: \n', listaTemporaria)  # Apenas dei um print da lista com os valores na sequência que o usuário inseriu
# para que seja feita uma comparação com a lista ordenada.
listaOrdenada = sorted(listaTemporaria, key=itemgetter('codigo'))  # Declarei uma variável que chama o método SORTED,
# método esse que irá ordenar a listaTemporaria, usando como parâmetro o value das keys codigo, values que a
# função itemgetter chamou quando foi declarado a key('codigo') como parâmetro de itemgetter.
print('lista Ordenada: \n', listaOrdenada)  # Print da lista ordenada de forma crescente, tendo como base os values das
# keys 'codigo'.
