A = 1
B = 2
C = 3
X = 20
Y = 10
Z = 1
V1 = True
V2 = False
nome = 'Pedro'
Rua = 'Pedrinho'
letra_a = A + C / B
letra_b = C / B / A
letra_c = -X ** B
letra_d = (-X) ** B
letra_e = V1 or V2
letra_f = V1 and not V2
letra_g = V2 and not V1
letra_h = not nome == Rua
letra_i = V1 and not V2 or V2 and not True
letra_j = X > Y and C <= B
letra_k = C - 3 * A < X + 2 * Z
print('a) A + C / B\nb) C / B / A\nC) -X ** B\nd) (-X) ** B\ne) V1 or V2\nf) V1 and not V2\ng) V2 and not V1\nh) not Nome == Rua\ni) V1 and not V2 or V2 and not True\nj) X > Y and C <= B\nk) C - 3 * A < X + 2 * Z')
escolha = input('Escolha a expressão atraves do indice da questao: ')
if escolha == 'a':
    print(letra_a)
elif escolha == 'b':
    print(letra_b)
elif escolha == 'c':
    print(letra_c)
elif escolha == 'd':
    print(letra_d)
elif escolha == 'e':
    print(letra_e)    
elif escolha == 'f':
    print(letra_f)
elif escolha == 'g':
    print(letra_g)
elif escolha == 'h':
    print(letra_h)
elif escolha == 'i':
    print(letra_i)
elif escolha == 'j':
    print(letra_j)
elif escolha == 'k':
    print(letra_k)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    