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
class Banco:
    def __init__(self, titular, numero_conta, saldo = 0.0):
        self.nome = titular
        self.conta = numero_conta
        self.saldo = saldo
    
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else: 
            print('Não foi feito nenhum valor p/ depósito.')
    
    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        elif valor > self.saldo:
            print('Saldo insuficiente.')
        else: 
            print('Valor de saque deve ser positivo.')
    def consultar_saldo(self):
        print(f"Saldo atual de {self.titular} ({self.numero_conta}): R${self.saldo:.2f}")

nome = input('Digite o nome do titular da conta: ')
n_conta = int(input('Digite o número da conta do titular: '))
saldo = int(input('Digite o valor em R$ do seu saldo: '))

conta = Banco(nome, n_conta, saldo)

print("\nOperações disponíveis:")
print("1. Depósito")
print("2. Saque")
print("3. Consultar Saldo")
print("4. Sair")
        
opcao = input("Escolha uma opção: ")

if opcao == '1':
    valor_deposito = float(input("Digite o valor do depósito: R$ "))
    conta.deposito(valor_deposito)
elif opcao == '2':
    valor_saque = float(input("Digite o valor do saque: R$ "))
    conta.saque(valor_saque)
elif opcao == '3':
    conta.consultar_saldo()
elif opcao == '4':
    print("Saindo...")
else:
    print("Opção inválida. Tente novamente.")


