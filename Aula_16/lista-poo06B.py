from datetime import datetime
import json

class Contato:
    def __init__(self, i, n, e, f, d):
        self.set_id(i)
        self.set_nome(n)
        self.set_email(e)
        self.set_fone(f)
        self.set_nascimento(d)
    
    # sets
    def set_id(self, i):
        if i == 0: raise ValueError("O id não pode ser zero (0).")
        else: self.__id = i
    def set_nome(self, n):
        if n == "": raise ValueError("Não pode ser vazio.")
        else: self.__nome = n
    def set_email(self, e):
        if e == "": raise ValueError("Não pode ser vazio.")
        else: self.__email = e
    def set_fone(self, f):
        if f == "": raise ValueError("Não pode ser vazio.")
        else: self.__fone = f
    def set_nascimento(self, d):
        if d > datetime.now(): raise ValueError("Não pode ser no futuro.")
        else: self.__nascimento = d

    # gets
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_nascimento(self): return self.__nascimento

    def __str__(self):
        return (
            f"Id: {self.__id}\n"
            f"Nome: {self.__nome}\n"
            f"Email: {self.__email}\n"
            f"Fone: {self.__fone}\n"
            f"Nascimento: {self.__nascimento}\n"
        )
    
    def to_json(self): 
        dic = {}
        dic["id"] = self.__id
        dic["nome"] = self.__nome
        dic["email"] = self.__email
        dic["fone"] = self.__fone
        dic["nascimento"] = self.__nascimento.strftime("%d/%m/%Y")
        return dic

class ContatoUI:
    __contatos = []
    @classmethod
    def main(cls):
        op = 0 
        while op != 9:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()
            if op == 6: ContatoUI.aniversario()
            if op == 7: ContatoUI.abrir()
            if op == 8: ContatoUI.salvar()
    @classmethod
    def menu(cls):
        print("1- Inserir, 2- Listar, 3- Atualizar, 4- Excluir, 5- Pesquisar, 6- Aniversário, 7- Abrir, 8- Salvar, 9- Fim")
        return int(input("Escolha uma opção: "))
    @classmethod
    def inserir(cls):
        id = int(input("Insira o id do contato: "))
        nome = input("Insira o nome: ")
        email = input("Insira o email: ")
        fone = input("Insira o telefone: ")
        d_nasc = datetime.strptime(input("Informe sua data de nascimento: "), "%d/%m/%Y")
        c = Contato(id, nome, email, fone, d_nasc)
        cls.__contatos.append(c)
    @classmethod
    def listar(cls):
        for c in cls.__contatos: print(c)
    @classmethod
    def atualizar(cls):
        id = int(input("Digite o id que deseja atualizar: "))
        for c in cls.__contatos:
            if c.get_id() == id:
                print(c)
                cls.__contatos.remove(c)
                nome = input("Insira o nome: ")
                email = input("Insira o email: ")
                fone = input("Insira o telefone: ")
                d_nasc = datetime.strptime(input("Informe sua data de nascimento: "), "%d/%m/%Y")
                c = Contato(id, nome, email, fone, d_nasc)
                cls.__contatos.append(c)
            else: print("O id não foi encontrado.")
    @classmethod
    def excluir(cls): 
        id = int(input("Digite o id que deseja excluir: "))
        for c in cls.__contatos:
            if c.get_id() == id:
                cls.__contatos.remove(c)
                print("O contato foi removido.")
            else: print("O id não foi encontrado.")
    @classmethod
    def pesquisar(cls):
        nome = input("Informe o nome: ")
        for c in cls.__contatos:
            if c.get_nome().startswith(nome): print(c)
            else: print("O nome não foi encontrado.")
    @classmethod
    def aniversario(cls):
        mes = input("Digite o nº do mês: ")
        e = False
        for c in cls.__contatos:
            if c.get_nascimento().month == mes: 
                print(c)
                e = True
            if not e: print("Nenhum contato faz aniversário neste mês.")
    @classmethod
    def abrir(cls):
        with open("contatos.json", mode="r") as arquivo:
            contatos_json = json.load(arquivo)
            cls.__contatos = []
            for obj in contatos_json:
                nascimento = datetime.strptime(obj["nascimento"], "%d/%m/%Y")
                c = Contato(obj["id"], obj["nome"], obj["email"], obj["fone"], nascimento)
                cls.__contatos.append(c)
    @classmethod
    def salvar(cls):
        with open("contatos.json", mode="w") as arquivo:
            json.dump(cls.__contatos, arquivo, default= Contato.to_json)

ContatoUI.main()

