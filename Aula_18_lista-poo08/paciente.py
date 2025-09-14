from datetime import datetime

class Paciente: 
    def __init__(self, n, c, t, nasc):
        self.set_nome(n)
        self.set_cpf(c)
        self.set_telefone(t)
        self.set_nascimento(nasc)
    
    # SETS
    def set_nome(self, n):
        if n == "": raise ValueError()
        else: self.__nome = n
    def set_cpf(self, c):
        if c == "": raise ValueError()
        else: self.__cpf = c
    def set_telefone(self, t):
        if t == "": raise ValueError()
        else: self.__telefone = t
    def set_nascimento(self, nasc):
        if nasc > datetime.now(): raise ValueError()
        else: self.__nascimento = nasc

    # GETS
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_telefone(self): return self.__telefone
    def get_nascimento(self): return self.__nascimento

    # IDADE
    def idade(self):
        hj = datetime.now()
        dv = hj - self.__nascimento
        anos = dv.days // 365
        meses = dv.days % 365 // 30
        return f'{anos} anos e {meses} meses'
    
    def __str__(self):
        return (
            f'Nome: {self.__nome}\n'
            f'CPF: {self.__cpf}\n'
            f'Telefone: {self.__telefone}\n'
            f'Data de nascimento: {self.__nascimento}\n'
            f'Idade: {self.idade()}'
        )
    
    