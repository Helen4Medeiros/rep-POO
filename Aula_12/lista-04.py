import random
class Bingo:
    def __init__(self):
        self.__num_bolas = 0
        self.__bolas_sorteadas = []
        self.__all_bolas = []

    def iniciar(self, num_bolas):
        self.__num_bolas = num_bolas
        self.__bolas_sorteadas = []
        self.__all_bolas = list(range(1, num_bolas + 1))
        random.shuffle(self.__all_bolas)

    def sortear(self):
        if not self.__all_bolas:
            return -1 

        bola = self.__all_bolas.pop()
        self.__bolas_sorteadas.append(bola)
        return bola
    
    def sorteados(self):
        return self.__bolas_sorteadas.copy()
    
    def fim(self):
        return len(self.__bolas_sorteadas) >= self.__num_bolas
    
class BingoUI:
    __bingo = None

    @classmethod
    def main(cls):
        op = 0
        while op != 4:
            op = cls.menu()
            if op == 1: BingoUI.iniciar()
            if op == 2: BingoUI.sortear()
            if op == 3: BingoUI.sorteados()
    @classmethod
    def menu(cls):
        print('1- Iniciar, 2- Sortear, 3- Números sorteados, 4- Sair')
        return int(input('Escolha uma opção: '))
    @classmethod
    def iniciar(cls):
        num = random.randint(50, 90)
        cls.__bingo = Bingo()
        cls.__bingo.iniciar(num)
        print(f'Jogo iniciado com {num} bolas')
    @classmethod
    def sortear(cls): 
        if cls.__bingo is None:
           return print("Inicie um jogo primeiro.")
            
        bola = cls.__bingo.sortear()
        if bola == -1:
            print("Todas as bolas já foram sorteadas. O jogo terminou!")
        else:
            print(f"Bola sorteada: {bola}")
    @classmethod
    def sorteados(cls):
        if cls.__bingo is None:
           return print("Você precisa iniciar um jogo primeiro.")
            
        bolas = cls.__bingo.sorteados()
        if not bolas:
            print("Nenhuma bola foi sorteada ainda.")
        else:
            print("Bolas sorteadas até agora:", sorted(bolas))

BingoUI.main()
