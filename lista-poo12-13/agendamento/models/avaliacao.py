class Avaliacao:
    def __init__(self, id, nota, comentario, id_cliente, id_profissional):
        self.set_id(id)
        self.set_nota(nota)
        self.set_comentario(comentario)
        self.set_id_cliente(id_cliente)
        self.set_id_profissional(id_profissional)
    
    def __str__(self):
        return f'{self.__id} - {self.__nota} - {self.__comentario} - {self.__id_cliente} - {self.__id_profissional}'

    def get_id(self): return self.__id
    def get_nota(self): return self.__nota
    def get_comentario(self): return self.__comentario
    def get_id_cliente(self): return self.__id_cliente
    def get_id_profissional(self): return self.__id_profissional

    def set_id(self, id): self.__id = id
    def set_nota(self, nota): 
        if nota == '': raise ValueError("Uma nota de 0-5 é obrigatória.")
        self.__nota = nota
    def set_comentario(self, comentario): self.__comentario = comentario
    def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
    def set_id_profissional(self, id_profissional): self.__id_profissional = id_profissional

from models.dao import DAO
import json

class AvaliacaoDAO(DAO):
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("avaliacoes.json", mode ="r") as arquivo: 
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Avaliacao.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("avaliacoes.json", mode ="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Avaliacao.to_json)
    
    @classmethod
    def verificar_avaliacao_existente(cls, id_cliente, id_profissional):
        cls.abrir()
        for av in cls._objetos:
            if (av.get_id_cliente() == id_cliente and av.get_id_profissional() == id_profissional):
                return True
        return False
        
    @classmethod
    def listar_por_profissional(cls, id_profissional):
        cls.abrir()
        return [av for av in cls._objetos if av.get_id_profissional() == id_profissional]

    @classmethod
    def calcular_media_profissional(cls, id_profissional):
        avaliacoes = cls.listar_por_profissional(id_profissional)
        if not avaliacoes:
            return 0.0
        soma_notas = sum(av.get_nota() for av in avaliacoes)
        return round(soma_notas / len(avaliacoes), 2)