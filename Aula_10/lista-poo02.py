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
class Banco:
    def __init__(self):
        self.__nome = ""
        self.__conta = ""
        self.__saldo = 0.00
    def set_conta(self, id):
        if id == "": raise ValueError("ID inválido")
        self.__conta = id
    def set_titular(self, titular):
        if titular == "": raise ValueError
        self.__nome = titular
    def set_saldo(self, saldo):
        if not saldo >= 0 or saldo == "": raise ValueError ('Saldo Inválido')
        self.__saldo = saldo
    def get_conta(self): return self.__conta
    def get_titular(self): return self.__nome
    def get_saldo(self): return self.__saldo
    
    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else: print('Não foi feito nenhum valor p/ depósito.')
    def saque(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        elif valor > self.__saldo: print('Saldo insuficiente.')
        else: print('Valor de saque deve ser positivo.')

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
            if op == 3: UI.banco()
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
    @staticmethod
    def banco():
        x = Banco()
        x.set_titular(input("Qual seu nome?"))
        x.set_conta(input("Qual o seu id? "))
        x.set_saldo(float(input("Qual o seu saldo inicial? R$")))
        x.deposito(float(input("Faça seu primeiro depósito! => R$")))
        print(f"[!]          Titular {x.get_titular()} fez um depósito. Saldo atual = {x.get_saldo():.2f} reais")
        x.saque(float(input("Faça o seu primeiro saque! => ")))
        print(f"[!]          Titular {x.get_titular()} fez um saque. Saldo atual = {x.get_saldo():.2f} reais")

UI.main()