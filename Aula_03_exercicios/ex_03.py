import math
# 1004 - PRODUTO SIMPLES
a= int(input())
b= int(input())
prod= a*b
print(f'PROD= {prod}')

# 1005 - MÉDIA 1
a= float(input())
b= float(input())
media= (a*3.5 + b*7.5)/ 11
print(f'MEDIA = {media:.5f}')

# 1011 - ESFERA 
r = float(input())
pi = 3.14159

vol = (4/3) * pi * r ** 3

print(f'VOLUME = {vol:.3f}')

# 2416 - CORRIDA

# 1015 - DISTÂNCIA ENTRE DOIS PONTOS 
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f'{d:.4f}')

# 1930 - TOMADAS
t1, t2, t3, t4 = map(int, input().split())

total = t1 + t2 + t3 + t4 - 3

print(f'{total}')
