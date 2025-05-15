class Triangulo: # ENCAPSULAMENTO
    def __init__(self):
        self.__b = 0
        self.__h = 0
    def set_b(self, v): 
        if v < 0: raise ValueError('O valor da base deve ser positivo.')
        self.__b = v
    def set_h(self, v): 
        if v < 0: raise ValueError('O valor da altura deve ser positivo.')
        self.__h = v
    def get_b(self): 
        return self.__b
    def get_h(self):
        return self.__h
    def calc_area(self):
        return self.b * self.h / 2
    
class UI: 
    @staticmethod
    def menu():
        op = int(input('Informe uma opção: 1- Triângulo, 9- Fim'))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
    @staticmethod
    def triangulo():
        x = Triangulo()
        x.b = int(input('Informe o valor da base: '))
        x.h = int(input('Informe o valor da altura: '))
        print(f'O triângulo de base {x.b} e altura {x.h} tem área {x.calc_area()}')

UI.main()