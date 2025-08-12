import json

class Cliente:
    def __init__(self, id, n, e, f):
        self.set_id(id)
        self.set_nome(n)
        self.set_email(e)
        self.set_fone(f)
    
    # sets
    def set_id(self, id):
        try: id = int(id)
        except: raise ValueError("O id deve ser um valor inteiro.")
        self.__id = id
    def set_nome(self, n): 
        if n == "": raise ValueError("O nome não pode ser vazio.")
        else: self.__nome = n
    def set_email(self, e):
        if e == "": raise ValueError("O email não pode ser vazio.")
        else: self.__email = e
    def set_fone(self, f):
        if f == "": raise ValueError("O telefone não pode ser vazio.")
        else: self.__fone = f
    
    # gets
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone

    def __str__(self):
        return (
            f"Id: {self.__id}\n"
            f"Nome: {self.__nome}\n"
            f"Email: {self.__email}\n"
            f"Fone: {self.__fone}\n"
        )
    
    def to_dict(self):
        return {
            "id": self.get_id(),
            "nome": self.get_nome(),
            "email": self.get_email(),
            "telefone": self.get_fone()
        }

class ClienteDAO:
    __objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.__abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1) # define o id novo como 1a+ 
                        # que o maior encontrado: garante que o id seja único e sequencial
        cls.__objetos.append(obj)
        cls.__salvar()
    @classmethod
    def listar(cls):
        cls.__abrir()
        return cls.__objetos
    @classmethod
    def listar_id(cls, i):
        for obj in cls.__objetos:
            if obj.get_id() == i:
                return obj
        return None
    @classmethod
    def atualizar(cls, obj):
        cls.__abrir()
        c_e = cls.listar_id(obj.get_id())
        if c_e: 
            for i, c in enumerate(cls.__objetos):
                if c.get_id() == obj.get_id():
                    cls.__objetos[i] = obj
                    cls.__salvar()
                return True
        return False
    @classmethod
    def excluir(cls, obj):
        cls.__abrir()
        c_e = cls.listar_id(obj)
        if c_e:
            cls.__objetos.remove(c_e)
            cls.__salvar()
            return True
        return False
    @classmethod
    def __abrir(cls): # método de acesso privado
        cls.__objetos = []
        try: 
            with open("clientes.json", mode="r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    obj = Cliente(dic["id"], dic["nome"], dic["email"], dic["telefone"])
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass
    @classmethod
    def __salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump([obj.to_dict() for obj in cls.__objetos], arquivo)
