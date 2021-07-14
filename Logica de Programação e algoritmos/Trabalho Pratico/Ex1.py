# Cabeçalho do programa
print('-' * 50)
print('-------- Exercício 1 da Atividade Prática --------')
print('-' * 50)


# Função para validar a entrada do usuario, uma entrada diferente da esperada, irá retornar uma mensagem e solicitará
# uma nova entrada. Peguei como base o algoritmo de validação apresentado na Aula 5
def entrada():
    entrada = int(input('Selecione uma opção: '))
    while (entrada < 1) or (entrada > 2):
        print('Opção inválida... Tente novamente ')
        entrada = int(input('Selecione uma opção: '))
        print('-' * 50)
    return entrada


# Função que irá receber o nome do aluno e sua nota. O strip() irá apagar espaços desnecessários na entrada do usuario.
# No IF o programa irá comparar a Nota Final do aluno com as condições apresentadas, se ela não for suprida, passará
# para a proxima condição. Se a condição for suprida, mostrará na tela o print com a mensagem informando o Nome, Nota e
# Conceito do aluno. Se o valor da nota inserido for maior que 10 o ELSE irá mostrar uma mensagem de erro e solicitará
# novos dados ao usuario, chamando novamente a função func_notas().
def func_notas():
    nome = str(input('Nome do aluno: ')).strip()
    nota = float(input('Nota do final: '))
    if 9 <= nota <= 10:
        print('-' * 50)
        print('Nome do aluno: {}\n'
              'Nota final: {}\n'
              'O aluno {} tirou nota {} e se enquadra no conceito A.'.format(nome, nota, nome, nota))
        print('-' * 50)
    elif 7 <= nota <= 8.9:
        print('-' * 50)
        print('Nome do aluno: {}\n'
              'Nota final: {}\n'
              'O aluno {} tirou nota {} e se enquadra no conceito B.'.format(nome, nota, nome, nota))
        print('-' * 50)
    elif 5 <= nota <= 6.9:
        print('-' * 50)
        print('Nome do aluno: {}\n'
              'Nota final: {}\n'
              'O aluno {} tirou nota {} e se enquadra no conceito C.'.format(nome, nota, nome, nota))
        print('-' * 50)
    elif 3 <= nota <= 4.9:
        print('-' * 50)
        print('Nome do aluno: {}\n'
              'Nota final: {}\n'
              'O aluno {} tirou nota {} e se enquadra no conceito D.'.format(nome, nota, nome, nota))
        print('-' * 50)
    elif 0 <= nota <= 2.9:
        print('-' * 50)
        print('Nome do aluno: {}\n'
              'Nota final: {}\n'
              'O aluno {} tirou nota {} e se enquadra no conceito E.'.format(nome, nota, nome, nota))
        print('-' * 50)
    else:
        print('-' * 50)
        print('Valor da nota excede o limite. Insira os dados novamente.')
        print('-' * 50)
        func_notas()


# Laço de repetição que manterá o usuario no programa até que ele deseje sair, selecionando a opção
# '2 - Sair do programa'. Enquanto o laço for verdadeiro 'True', ele continuará sendo executado. A variavel 'menu'
# receberá 1 ou 2, que foi recebido pela função entrada(), e acionará uma opção do menu do programa. Algo diferente
# não é aceito. Se o valor recebido pela variavel menu, for igual a 1, o IF chamará a função func_notas().
# Se a entrada for igual a 2, o programa irá encerrar.
while True:
    print(' 1 - Inserir dados.')
    print(' 2 - Sair do programa.')
    print('-' * 50)
    menu = entrada()
    if menu == 1:
        func_notas()
    else:
        break
