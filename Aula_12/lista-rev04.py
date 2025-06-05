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
        
# QUESTÃO 02
class Pais: 
    def __init__(self):
        self.__nome = ''
        self.__pop = 0
        self.__area = 0.0
    def set_nome(self, pais):
        if pais == '': raise ValueError('Necessário informar o nome do país')
        self.__nome = pais
    def set_populacao(self, hab):
        if hab >= 0: self.__pop = hab
        else: ValueError()
    def set_area(self, km):
        if km >= 0: self.__area = km
        else: ValueError()
    def get_nome(self): return self.__nome
    def get_populacao(self): return self.__pop
    def get_area(self): return self.__area

    def densidade(self): return self.__pop / self.__area
    
class ParcialUI: 
    @staticmethod
    def menu():
        op_2 = int(input('1- Calcular, 2- Fim'))
        return op_2
    @staticmethod
    def main():
        op_2 = 0
        while op_2 != 2:
            op_2 = ParcialUI.menu()
            if op_2 == 1: ParcialUI.calculo()
    @staticmethod
    def calculo():
        x = Pais()
        x.set_nome(input('Informe o nome do país: '))
        x.set_populacao(int(input('Informe o nº de habitantes do país: ')))
        x.set_area(float(input('informe a área em km2: ')))
        print(f'A densidade demográfica é de {x.densidade()} km2')

ParcialUI.main()

