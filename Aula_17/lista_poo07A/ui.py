from views import View

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.atualizar()
            if op == 4: UI.excluir()
    @staticmethod
    def menu():
        print("1- Inserir, 2- Listar, 3- Atualizar, 4- Excluir, 5-Fim")
        return int(input("Informe a opção: "))
    @staticmethod
    def inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o telefone: ")
        View.cliente_inserir(nome, email, fone)
        print("Cliente inserido com sucesso.")
    @staticmethod
    def listar():
        for cliente in View.cliente_listar():
            print(cliente)
    @staticmethod
    def atualizar():
        id = int(input("Informe o id que deseja atualizar: "))
        novo_nome = input("Insira o novo nome: ")
        novo_email = input("Insira o novo email: ")
        novo_fone = input("Insira o novo telefone: ")
        View.cliente_atualizar(id, novo_nome, novo_email, novo_fone)
        print("Cliente atualizado com sucesso.")
    @staticmethod
    def excluir():
        id = int(input("Informe o id que deseja excluir: "))
        View.cliente_excluir(id)
        print('Cliente excluído com sucesso.')

UI.main()

