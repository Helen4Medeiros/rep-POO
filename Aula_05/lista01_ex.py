# 01)
class Circulo:
    def __init__(self):
        self.r = 0
    def area(self):
        return 3.14 * (self.r**2)
    def circun(self):
        return 2 * 3.14 * self.r

x = Circulo()
x.r = 2
print(x.area())
print(x.circun())

# 02)
class Velocidade:
    def __init__(self):
        self.d = 0 
        self.th = 0
        self.tm = 0
    def vel(self):
        t_total = self.th + self.tm / 60
        return self.d / t_total
    
y = Velocidade()
y.d = 10
y.th = 2
y.tm = 20
print(f'Velocidade: {y.vel()}')

# 03)
