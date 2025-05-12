# 01)
# print(1-2+3*4)
# print(1*2-3*4)
# print(1/2+3*4)
# print(1//2*3+4)
# print(1+2*3/4)

# 02)
print('Digite três números inteiros separados por espaços:')
x, y, z = map(int, input().split())
soma_pares = 0
if x % 2 == 0:
    soma_pares += x
if y % 2 == 0:
    soma_pares += y
if z % 2 == 0:
    soma_pares += z

print(f'Soma dos pares: {soma_pares}')

# 03)
frase = input('Digite uma frase: ')
letras = list(frase)

nova_frase = ''
for i in range(len(letras)):
    if i % 2 == 0:
        nova_frase += letras[i]

print(nova_frase)

# 04) 
class Agua: 
    def __init__(self):
        self.mes = 1
        self.ano = 2025 
        self.c = 0
    def Conta(self):
        if self.consumo == 10:
            return 38
        if 11 <= self.consumo <= 20:
            return 38 + (self.consumo - 10) * 5
        if self.consumo >= 21:
            return 88 + (self.consumo - 20) * 6
        
x = Agua()
x.mes = int(input('Qual mês da conta que você quer pagar?'))
x.ano = int(input('Qual o ano da conta que você quer pagar?'))
x.consumo = int(input('Qual foi o consumo de água do mês que você quer pagar?'))
print(x.Conta())
        
