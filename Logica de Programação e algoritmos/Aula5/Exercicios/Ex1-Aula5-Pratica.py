def valida_int(pergunta, nin, max): # Criando uma função que compara se o valor de entrada é valido 
    x = int(input(pergunta))
    while ((x < nin) or (x > max)):
        x = int(input(pergunta))
    return x
    
def fatorial(num): # Função que calcula o fatorial
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num+1):
        fat *= i # fat = fat * i
    return fat



"""
Calcula a fatorial
"""

x = valida_int('Digite um valor para calcular a fatorial: ', 0, 99)
print('O fatorial de {} é {}'.format(x, fatorial(x)))