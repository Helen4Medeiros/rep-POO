import json

class Servico:
    def __init__(self, id, d, v):
        self.set_id(id)
        self.set_descricao(d)
        self.set_valor(v)

    # SETS
    def set_id(self, id): self.__id = id
    def set_descricao(self, d): self.__descricao = d
    def set_valor(self, v): self.__valor = v

    # GETS
    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_valor(self): return self.__valor

    def __str__(self):
        return (
            f'Id: {self.__id}\n'
            f'Descrição: {self.__descricao}\n'
            f'Valor: {self.__valor}'
        )
    
    def to_json(self):
        dic = {'id': self.__id, 'descrição': self.__descricao, 'valor': self.__valor}
        return dic
    
    @staticmethod
    def from_json(dic):
        return Servico(dic['id'], dic['descrição'], dic['valor'])
    
class ServicoDAO:
    __objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.__abrir()
        id = 0 
        for aux in cls.__objetos:
            if aux.get_id() > id: id = aux.get_id()
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
            with open('servicos.json', mode='r') as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Servico.from_json(dic)
                    cls.__objetos.append(obj)
        
        except FileNotFoundError:
            pass

    @classmethod
    def __salvar(cls):
        with open('servicos.json', mode='w') as arquivo:
            json.dump(cls.__objetos, arquivo, default= Servico.to_json)