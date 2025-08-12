from models import Cliente, ClienteDAO

class View:
    @staticmethod # método estático - pode ser chamado sem precisar criar um objeto
    def cliente_inserir(nome, email, fone):
        ClienteDAO.inserir(Cliente(0, nome, email, fone))
        # chama a op no DAO e instância a classe Cliente
    @staticmethod
    def cliente_listar(): 
        return ClienteDAO.listar()
    @staticmethod
    def cliente_atualizar(id, novo_nome, novo_email, novo_fone):
        ClienteDAO.atualizar(Cliente(id, novo_nome, novo_email, novo_fone))
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO.excluir(Cliente(id))
