import json

class Profissional: 
    def __init__(self, id, n, e, c):
        self.set_id(id)
        self.set_nome(n)
        self.set_esp(e)
        self.set_cons(c)

    # sets
    def set_id(self, id):
        if id < 0: raise ValueError('Id inválido')
        self.__id = id
    def set_nome(self, n):
        if id == ' ': raise ValueError('Nome inválido')
        self.__nome = n
    def set_esp(self, e):
        if e == ' ':  raise ValueError('Especialidade inválida')
        self.__esp = e
    def set_cons(self, c):
        if c == ' ': raise ValueError('Conselho inválido')
        self.__cons = c

    # gets
    def get_id(self): return self.__id 
    def get_nome(self): return self.__nome
    def get_esp(self): return self.__esp
    def get_cons(self): return self.__cons

    def __str__(self):
        return f'ID - {self.__id} | NOME: {self.__nome} | ESPECIALIDADE: {self.__esp} | CONSELHO: {self.__cons}'
    
    def to_json(self): 
        dic = {
            'id': self.__id,
            'nome': self.__nome,
            'especialidade': self.__esp,
            'conselho': self.__cons,
        }
        return dic
    
    @staticmethod
    def from_json(dic):
        return Profissional(
            dic['id'],
            dic['nome'], 
            dic['especialidade'],
            dic['conselho'],
        )
    
class ProfissionalDAO:
    __objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.__abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id: 
                id = aux.get_id()
        obj.set_id(id + 1)
        cls.__objetos.append(obj)
        cls.__salvar()
    
    @classmethod
    def listar(cls):
        cls.__abrir()
        return cls.__objetos
    
    @classmethod
    def listar_id(cls, id):
        cls.__abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id: return obj
        return None
    
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.__objetos.append(obj)
            cls.__salvar()

    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.__salvar()

    @classmethod
    def __abrir(cls):
        cls.__objetos = []
        try:
            with open("profissional.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Profissional.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass
    
    @classmethod
    def __salvar(cls):
        with open("profissional.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Profissional.to_json)