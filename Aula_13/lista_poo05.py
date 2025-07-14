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
        return (
            f'Nome: {self.__nome}\n'
            f'CPF: {self.__cpf}\n'
            f'Telefone: {self.__telefone}\n'
            f'Nascimento: {self.__nascimento}\n'
            f'Idade: {self.idade()}'
        )

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
    @classmethod
    def menu(cls):
        print('1- Cadastrar, 2- Listar, 3- Atualizar, 5- Fim')
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
            f'Código de barras: {self.__codBarras}\n'
            f'Data de emissão: {self.__dateEmissao.strftime("%d/%m/%Y")}\n'
            f'Data de vencimento: {self.__dataVencimento.strftime("%d/%m/%Y")}\n'
            f'Data de pagamento: {self.__dataPagto}\n'
            f'Valor do boleto: {self.__valorBoleto}\n'
            f'Valor do pago: {self.__valorPago}\n'
            f'Situação: {self.__situacaoPagamento.name}\n'
        )
    
class BoletoUI:
    __boleto = []
    @classmethod
    def main(cls):
        op = 0
        while op != 5:
           op = BoletoUI.menu()
           if op == 1: BoletoUI.inserir()
           if op == 2: BoletoUI.detalhes()
           if op == 3: BoletoUI.pagar()
           if op == 4: BoletoUI.situ()
    @classmethod
    def menu(cls):
        print('1- Inserir, 2- Detalhes, 3- Pagar, 4- Situação, 5- Fim')
        op = int(input('O que deseja?'))
        return op
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
        if cls.__boleto: 
            for b in cls.__boleto:
                print(b)
        else: print('Não cadastrado.')
    @classmethod
    def pagar(cls):
        if not cls.__boleto:
            print('Nenhum boleto cadastrado.')
            return
        cod = input('Informe o código de barras do boleto a pagar: ')
        for b in cls.__boleto:
            if b.get_codbarras() == cod:
                try: 
                    valor_pg = float(input('Informe o valor a pagar: '))
                    b.pagar(valor_pg)
                    print('Pagamento registrado com sucesso.')
                except ValueError as e:
                    print(e)
                return
        print('Boleto não encontrado')
    @classmethod
    def situ(cls):
        if not cls.__boleto:
            print('Nenhum boleto cadastrado.')
            return
        cod = input('Informe o código de barras do boleto para consultá-lo: ')
        for b in cls.__boleto:
            if b.get_codbarras() == cod:
                print(f'Situação: {b.get_situ_pagamento().name}')

BoletoUI.main()

# 3) UMA AGENDA DE CONTATOS
class Contato:
    def __init__(self, i, n, e, f, d):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
        self.__nascimento = datetime.strptime(d, '%d/%m/%Y')
    
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_nascimento(self): return self.__nascimento

    def __str__(self):
        return(
            f'id: {self.__id}\n'
            f'nome: {self.__nome}\n'
            f'email: {self.__email}\n'
            f'fone: {self.__fone}\n'
            f'nascimento: {self.__nascimento}\n'
        )
    
class ContatoUI:
    __contatos = []
    @classmethod
    def main(cls): 
        op = 0
        while op != 7:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()
            if op == 6: ContatoUI.aniv()
    @classmethod
    def menu(cls):
        print('1- Inserir, 2- Listar, 3- Atualizar, 4- Excluir, 5- Pesquisar, 6- Aniversariantes, 7- Sair')
        op = int(input('Qual ação deseja realizar? '))
        return op 
    @classmethod
    def inserir(cls): 
        id = int(input("Insira o id do contato: "))
        nome = input("Insira o nome: ")
        email = input("Insira o e-mail: ")
        fone = input("Insira o fone: ")
        data_n = input('Insira a data de nascimento DD/MM/AAAA: ')
        c = Contato(id, nome, email, fone, data_n)
        cls.__contatos.append(c)
    @classmethod
    def listar(cls):
        for c in cls.__contatos:
            print(c)
    @classmethod
    def atualizar(cls):
        id = int(input('Digite o id que deseja atualizar: '))
        for c in cls.__contatos:
            if c.get_id() == id:
                print(c)
                cls.__contatos.remove(c)
                nome = input('Insira o novo nome do contato: ')
                email = input('Insira o novo email: ')
                fone = input('Insira o novo fone: ')
                data_n = input('Insira a nova datd de nascimento DD/MM/AAAA: ')
                novo = Contato(id, nome, email, fone, data_n)
                cls.__contatos.append(novo)
            else: print('O id não foi encontrado.')
    @classmethod
    def excluir(cls):
        id = int(input('Informe o id: '))
        for c in cls.__contatos:
            if c.get_id() == id:
                cls.__contatos.remove(c)
                print('Contato removido.')
            else: print('O id não foi encontrado.')
    @classmethod
    def pesquisar(cls):
        nome = input("Informe o nome: ")
        for c in cls.__contatos:
            if c.get_nome().startswith(nome): print(c)
            else: print('O nome não foi encontrado.')
    @classmethod
    def aniv(cls):
        mes = int(input('Digite o nº do mês: '))
        e = False
        for c in cls.__contatos:
            if c.get_nascimento().month == mes:
                print(c)
                e = True
        if not e: print('Nenhum contato faz aniversário neste mês.')

ContatoUI.main()

    
