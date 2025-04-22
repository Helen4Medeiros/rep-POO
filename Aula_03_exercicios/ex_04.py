import math
# 1036 - FÓRMULA DE BHASKARA
# a, b, c = map(float, input().split())

# if a == 0:
#    print('Impossível calcular')   
# else:
#     delta = b**2 - 4*a*c
    
#     if delta < 0:
#         print('Impossível calcular')
#     else:
#         r_delta = math.sqrt(delta)

#         x1= (-b + r_delta) / (2*a)
#         x2= (-b - r_delta) / (2*a)

#         print(f'R1 = {x1:.5f}')
#         print(f'R2 = {x2:.5f}')

# 1044 - MÚLTIPLOS
# a, b = map(int, input().split())

# if a % b == 0 or b % a == 0:
#     print('Sao Multiplos')
# else:
#     print('Nao sao Multiplos')

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
