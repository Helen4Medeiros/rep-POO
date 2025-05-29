# QUESTÃO 01: ÁREA CÍRCULO
class Circulo: 
    def __init__(self):
        self.__r = 0
    def set_raio(self, i):
        if i >= 1: self.__r = i
        else: ValueError()
    def get_raio(self):
        return self.__r
    def area(self):
        return 3.14 * (self.__r**2)
    def circunferencia(self):
        return 2 * 3.14 * self.__r
    
# QUESTÃO 02: A VIAGEM
class Velocidade:
    def __init__(self):
        self.__d = 0
        self.__t = 0
    def set_d(self, i):
        if i >= 0: self.__d = i
        else: ValueError()
    def set_t(self, i):
        if i >= 0: self.__t = i
        else: ValueError()
    def get_d(self):
        return self.__d
    def get_t(self):
        return self.__t
    def velocidade(self):
        return self.__d / self.__t

# QUESTÃO 03: CONTA BANCÁRIA

# QUESTÃO 04: ENTRADA DO CINEMA 

# UI
class UI:
    @staticmethod
    def menu():
        op = int(input('Informe uma opção: 1- Círculo, 2- Velocidade Viagem, 3- Conta Bancária, 4- Entrada Cinema, 9- Fim'))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.circulo()
            if op == 2: UI.velocidade()
    @staticmethod
    def circulo():
        x = Circulo()
        x.set_raio(float(input('Informe o raio: ')))
        print(f'A área do seu círculo é {x.area()} e a sua circunferência é {x.circunferencia()}')
    @staticmethod
    def velocidade():
        x = Velocidade()
        x.set_d(float(input('Informe a distância percorrida: ')))
        x.set_t(float(input('Informe o tempo: ')))
        print(f'A velocidade média percorrida foi de {x.velocidade()}km/h')

UI.main()