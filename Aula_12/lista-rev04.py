# QUESTÃO 01
class Viagem:
    def __init__(self):
        self.__destino = ''
        self.__distancia = 0
        self.__litros = 0
    def set_destino(self, local):
        if local == '': raise ValueError('Informe um destino')
        self.__destino = local
    def set_distancia(self, d):
        if d >= 0: self.__distancia = d
        else: ValueError()
    def set_litros(self, l):
        if l >= 0: self.__litros = l
        else: ValueError()
    def get_destino(self): return self.__destino
    def get_distancia(self): return self.__distancia
    def get_litros(self): return self.__litros

    def consumo(self):
        return self.__distancia / self.__litros
    
class ViagemUI: 
    @staticmethod
    def menu():
        op = int(input('1- Calcular, 2- Fim'))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = ViagemUI.menu()
            if op == 1: ViagemUI.calculo()
    @staticmethod
    def calculo():
        x = Viagem()
        x.set_destino(input('Informe seu destino: '))
        x.set_distancia(float(input('Informe a distancia em Km: ')))
        x.set_litros(float(input('Informe os litros: ')))
        print(f'O consumo foi de {x.consumo()}')

ViagemUI.main()
        
    
