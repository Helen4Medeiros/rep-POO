from datetime import datetime
from enum import Enum

# 1) UM PACIENTE
class Paciente: 
    def __init__(self, n, c, t, nasc):
        self.__nome = n
        self.__cpf = c
        self.__telefone = t
        self.__nascimento = datetime.strptime(nasc, '%d/%m/%Y')
        
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_telefone(self): return self.__telefone
    def get_nascimento(self): return self.__nascimento

    def idade(self):
        hoje = datetime.now()
        dv = hoje - self.__nascimento
        anos = dv.days // 365
        meses = dv.days % 365 // 30
        return f'{anos} anos e {meses} meses'

    def __str__(self):
        return f'Nome: {self.__nome} - CPF: {self.__cpf} - Telefone: {self.__telefone} - Data de nascimento: {self.__nascimento} - Idade: {self.idade()}'

class PacienteUI: 
    __pacientes = []
    @classmethod
    def main(cls):
        op = 0
        while op != 5: 
            op = PacienteUI.menu()
            if op == 1: PacienteUI.cadastrar()
            if op == 2: PacienteUI.listar()
            if op == 3: PacienteUI.atualizar()
            if op == 4: PacienteUI.idades()
    @classmethod
    def menu(cls):
        print('1- Cadastrar, 2- Listar, 3- Atualizar, 4- Idade, 5- Fim')
        return int(input('Informe nº do serviço que deseja realizar: '))
    @classmethod
    def cadastrar(cls):
        nome = input('Informe o nome do paciente: ')
        cpf = input('Insira o CPF: ')
        telefone = input('Insira o telefone: ')
        data_n = input('Insira a data de nascimento (XX/XX/XXXX): ')
        p = Paciente(nome, cpf, telefone, data_n)
        cls.__pacientes.append(p)
    @classmethod
    def listar(cls):
        for p in cls.__pacientes:
            print(p)
    @classmethod
    def atualizar(cls):
        cpf = input('Informe o CPF que deseja atualizar: ')
        for p in cls.__pacientes:
            if p.get_cpf() == cpf:
                print(p)
                nome = input('Informe o nome do paciente: ')
                cpf = input('Insira o CPF: ')
                telefone = input('Insira o telefone: ')
                data_n = input('Insira data de nascimento (XX/XX/XXXX): ')
                novo = Paciente(nome, cpf, telefone, data_n)
                cls.__pacientes.remove(p)
                cls.__pacientes.append(novo)

PacienteUI.main()

# 2) UM BOLETO
class Pagamento(Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 3

class Boleto:
    def __init__(self, codbarras, e, v, va ):
        self.__codBarras = codbarras
        self.__dateEmissao = datetime.strptime(e, '%d/%m/%Y')
        self.__dataVencimento = datetime.strptime(v, '%d/%m/%Y') 
        self.__dataPagto = None
        self.__valorBoleto = va
        self.__valorPago = 0.0
        self.__situacaoPagamento = Pagamento.EmAberto

    def get_codbarras(self): return self.__codBarras
    def get_data_emissao(self): return self.__dateEmissao
    def get_data_vencimento(self): return self.__dataVencimento
    def get_data_pagamento(self): return self.__dataPagto
    def get_valor_boleto(self): return self.__valorBoleto
    def get_valor_pago(self): return self.__valorPago
    def get_situ_pagamento(self): return self.__situacaoPagamento

    def pagar(self, v_pago):
        if v_pago <= 0: raise ValueError('Insira um valor válido para pagamento.')
        self.__valorPago += v_pago
        self.__dataPagto = datetime.now()

        if self.__valorPago == 0: 
            self.__situacaoPagamento = Pagamento.EmAberto
        elif self.__valorPago < self.__valorBoleto:
            self.__situacaoPagamento = Pagamento.PagoParcial
        elif self.__valorPago == self.__valorBoleto:
            self.__situacaoPagamento = Pagamento.Pago

    def situacao(self):
        return self.__situacaoPagamento
    
    def __str__(self):
        return (
            f'Código de barras: {self.__codBarras}'
            f'Data de emissão: {self.__dateEmissao.strftime('%d/%m/%Y')}'
            f'Data de vencimento: {self.__dataVencimento.strftime('%d/%m/%Y')}'
            f'Data de pagamento: {self.__dataPagto}'
            f'Valor do boleto: {self.__valorBoleto}'
            f'Valor do pago: {self.__valorPago}'
            f'Situação: {self.__situacaoPagamento.name}'
        )
    
class B_PUI:
    __boleto = []
    def main(cls):
        op = 0
        while op != 5:
           op = B_PUI.menu()
           if op == 1: B_PUI.inserir()
           if op == 2: B_PUI.detalhes()
           if op == 3: B_PUI.pagar()
           if op == 4: B_PUI.situ()
           print('Fim')
    @classmethod
    def menu(cls):
        print('1- Inserir, 2- Detalhes, 3- Pagar, 4- Situação, 5- Fim')
        return int(input('O que deseja? '))
    @classmethod
    def inserir(cls):
        print('CADASTRO BOLETO')
        cod = input('Insira o cósigo de barras: ')
        emissao = input('Data de emissão DD/MM/AAAA: ')
        vencimento = input('Data de vencimento DD/MM/AAAA: ')
        valor = float(input('Valor do boleto: '))
        
        b = Boleto(cod, emissao, vencimento, valor)
        cls.__boleto.append(b)
    @classmethod
    def detalhes(cls):
        if cls.__boleto: print(cls.__boleto)
        else: print('Não cadastrado.')
    @classmethod
    def pagar(cls):
        if cls.__boleto:
            valor_pago = float(input('Informe o valor a pagar: '))
            cls.__boleto.pagar(valor_pago)
            print('Pagamento registrado.')
        else: print('Nenhum boleto cadastrado.')
    @classmethod
    def situ(cls):
        if cls.__boleto:
            print(f'Situação atual: {cls.__boleto.situacao().name}')
        else: print('Nenhum boleto cadastrado.')

B_PUI.main()

    



