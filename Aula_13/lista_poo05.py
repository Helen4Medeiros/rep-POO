# 1)
from datetime import datetime

class Paciente: 
    def __init__(self, n, c, t, nasc):
        self.__nome = n
        self.__cpf = c
        self.__telefone = t
        self.__nascimento = nasc
        
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_telefone(self): return self.__telefone
    def get_nascimento(self): return self.__nascimento

    def idade(self):
        hoje = datetime.now()
        d = int(input('Informe sua data de nascimento: '))
        self.__nascimento = datetime.strptime(d, '%d/%M/%Y')
        dv = hoje - self.__nascimento
        return dv.days // 365, 'anos', dv.days % 365 // 30, 'meses', dv.days % 365 % 30, 'dias'

    def __str__(self):
        f'Nome: {self.__nome} - CPF: {self.__cpf} - Telefone: {self.__telefone} - Data de nascimento: {self.__nascimento} - Idade: {self.__idade()}'

class PacienteUI: 
    __pacientes = []
    @classmethod
    def main(cls):
        op = 0
        while op != 5: 
            op = Paciente.menu()
            if op == 1: Paciente.cadastrar()
            if op == 2: Paciente.listar()
            if op == 3: Paciente.atualizar()
            if op == 4: Paciente.idade()
            else: print('Fim')
    @classmethod
    def menu(cls):
        print('1- Cadastrar, 2- Listar, 3- Atualizar, 4- Idade, 5- Fim')
        op = int(input('Informe nº do serviço que deseja realizar: '))
    @classmethod
    def cadastrar():

