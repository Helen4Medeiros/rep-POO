# 01 
def maior(x, y):
    return (x+y+abs(x-y))/2

a= int(input('Digite o 1º valor: '))
b= int(input('Digite o 2º valor: '))

print(f'Maior valor: {maior(a,b)}')

# 02 
def maior(x, y): 
    return (x+y+abs(x-y))/2

a= int(input('Digite o 1º valor: '))
b= int(input('Digite o 2º valor: '))
c= int(input('Digite o 3º valor: '))

maior_ab= maior(a,b)
maior_abc= maior(maior_ab, c)

print(f'Maior: {maior_abc}')

# 03
def iniciais(nome):
    partes = nome.split()
    letras = []

    for parte in partes:
        letras.append(parte[0])
    
    return '.'.join(letras) + '.'

nome= input('Digite aqui seu nome completo: ')

print(f'Iniciais: {iniciais(nome)}')

# 04
def aprovado(n1, n2):
    media= n1+n2/2
    return media >= 60

n1= int(input('Digite a nota 1: '))
n2= int(input('Digite a nota 2: '))

if aprovado(n1, n2):
     print('Aluno aprovado')
else: 
     print('Aluno reprovado')

# 05
def formatar_nome(nome):
    return nome.title()

nome= input('Digite aqui seu nome completo: ')

print(f'Nome formatado: {formatar_nome(nome)}')