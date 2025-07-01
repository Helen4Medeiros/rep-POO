class Pais:
    def __init__(self, i, n, p, a):
        self.__id = i
        self.__nome = n
        self.__pop = p
        self.__area = a

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_pop(self): return self.__pop
    def get_area(self): return self.__area
    
    def densidade(self): return self.__pop / self.__area
    
    def __str__(self):
        return f'id: {self.__id} | nome: {self.__nome} | população: {self.__pop} | área: {self.__area} | densidade: {self.densidade():.1f}'
    
class PaisUI:
    __pais = []
    @classmethod
    def main(cls):
        op = 0
        while op != 7:
            op = PaisUI.menu()
            if op == 1: PaisUI.inserir()
            if op == 2: PaisUI.listar()
            if op == 3: PaisUI.atualizar()
            if op == 4: PaisUI.excluir()
            if op == 5: PaisUI.mais_pop()
            if op == 6: PaisUI.mais_pov()
    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5- Mais Populoso, 6- Mais Povoado, 7- Fim")
        return int(input("Escolha uma opção: "))
    @classmethod
    def inserir(cls):
        id = int(input("Insira o id do país: "))
        nome = input("Insira o nome: ")
        pop = int(input("Insira a população: "))
        area = int(input("Insira a área: "))
        c = Pais(id, nome, pop, area)
        cls.__pais.append(c)
    @classmethod
    def listar(cls):
        for c in cls.__pais:
            print(c)
    @classmethod   
    def atualizar(cls):
        id = int(input('Digite o id do país que deseja atualizar: '))
        for c in cls.__pais:
            if c.get_id() == id:
                print(c)
                nome = input("Informe o novo nome: ")
                pop = input("Informe a nova população: ")
                area = input("Informe a nova área: ")
                d = Pais(id, nome, pop, area)
                cls.__pais.remove(c)
                cls.__pais.append(d)

        else: print('O id não consta na lista de países.')  
    @classmethod
    def excluir(cls):
        id = int(input('Informe o id: '))
        for c in cls.__pais:
            if c.get_id() == id:
                cls.__pais.remove(c)
                print('País removido.')
    @classmethod
    def mais_pop(cls):
        mais_pop = max(cls.__pais, key= lambda c: c.get_pop())
        print(mais_pop)
    @classmethod
    def mais_pov(cls):
        mais_pov = max(cls.__pais, key= lambda c: c.densidade())
        print(mais_pov)

PaisUI.main()
    
