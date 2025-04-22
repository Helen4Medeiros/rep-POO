import math
import random

# 1036 - FÓRMULA DE BHASKARA
a, b, c = map(float, input().split())

if a == 0:
   print('Impossível calcular')   
else:
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print('Impossível calcular')
    else:
        r_delta = math.sqrt(delta)

        x1= (-b + r_delta) / (2*a)
        x2= (-b - r_delta) / (2*a)

        print(f'R1 = {x1:.5f}')
        print(f'R2 = {x2:.5f}')

# 1044 - MÚLTIPLOS
a, b = map(int, input().split())

if a % b == 0 or b % a == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')

# 1049 - ANIMAL 
animais = {
    'vertebrado': {
        'ave': {
            'carnivoro': 'aguia',
            'onivoro': 'pomba'
        },
        'mamifero': {
            'onivoro': 'homem',
            'herbivoro': 'vaca'
        }
    }, 
    'invertebrado': {
        'inseto': {
            'hematofago': 'pulga',
            'herbivoro': 'lagarta'
        },
        'anelideo': {
            'hematofago': 'sanguessuga',
            'onivoro': 'minhoca'
        }
    }
}

c1= input()
c2= input()
c3= input()

print(animais[c1][c2][c3])

# 1050 - DDD
ddd = int(input())

ddd_cid = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte'
}

if ddd in ddd_cid:
    print(ddd_cid[ddd])
else:
    print('DDD nao cadastrado')

# 2424 - TIRA-TEIMA
x, y = map(int, input().split())

if 432 >= x >= 0 and 0 <= y <= 468:
     print('dentro')
else:
    print('fora')

# 2670 - MÁQUINA DE CAFÉ
a1 = int(input())
a2 = int(input())
a3 = int(input())

tempo_a1= a2 * 2 + a3 * 4
tempo_a2= a1 * 2 + a3 * 2
tempo_a3= a1 * 4 + a2 * 2

min_t = min(tempo_a1, tempo_a2, tempo_a3)

print(min_t)

# 1059 - NÚMEROS PARES
for n in range(1, 101):
    if n % 2 == 0:
        print(n)

# 1080 - MAIOR E POSIÇÃO
maior = -1 
pos = -1
for n in range(1, 101):
    valor = int(input())
    if valor > maior:
        maior = valor
        pos = n

print(maior)
print(pos)

# 1094 - EXPERIÊNCIAS (?)

# 1114 - SENHA FIXA
while True:
    senha = int(input())
    if senha == 2002:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")

# 1116 - DIVIDINDO X POR Y
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    
    if y == 0:
        print("divisao impossivel")
    else:
        resultado = x / y
        print(f"{resultado:.1f}")

# 1151 - FIBONACCI FACIL
n = int(input())

fibonacci = []

a, b = 0, 1

for i in range(n):
    fibonacci.append(a)
    a, b = b, a + b

print(" ".join(map(str, fibonacci)))