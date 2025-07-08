# 1)

class Paciente: 
    def __init__(self, n, c, t, nas):
        self.__nome = n
        self.__cpf = c
        self.__telefone = t
        self.__nascimento = nas
        
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_telefone(self): return self.__telefone
    def get_nascimento(self): return self.__nascimento


        
