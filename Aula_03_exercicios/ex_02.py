import math
# 01
nome= input('Digite seu nome completo: ')
lista= nome.split()
p_nome= lista[0]
print(f'Bem-vindo(a) ao Python, {p_nome}')

# 02
p_bim= int(input('Digite a nota do primeiro bimestre da disciplina: '))
s_bim= int(input('Digite a nota do segundo bimestre da disciplina: '))
media= (p_bim*2 + s_bim*3)//5
print(f'Média parcial: {media}')

# 03
print('Digite a base e a altura do retângulo:')
b= int(input())
a= int(input())
print(f'Área: {b*a:.2f} - Perímetro: {2*(b+a):.2f} - Diagonal: {math.sqrt(b**2+a**2):.2f}')

# 04
frase= input('Digite uma frase: ')
u_palavra= frase.rsplit(maxsplit=1)[-1]
print(u_palavra)


