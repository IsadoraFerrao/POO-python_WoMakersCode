# Importa a classe ABC (Abstract Base Class) e o decorador abstractmethod
from abc import ABC, abstractmethod

# Escopo global para armazenar os gatinhos disponíveis
gatinhos_disponiveis = []

# Classe principal para os gatinhos
class Gatinho:
    # Inicializa um objeto Gatinho com nome, idade e cor
    def __init__(self, nome, idade, cor):
        self.__nome = nome  # Atributo privado para o nome do gatinho
        self.__idade = idade  # Atributo privado para a idade do gatinho
        self.__cor = cor  # Atributo privado para a cor do gatinho
        self.__adotado = False  # Atributo privado para indicar se o gatinho foi adotado

    # Retorna o nome do gatinho
    def get_nome(self):
        return self.__nome

    # Retorna a idade do gatinho
    def get_idade(self):
        return self.__idade

    # Retorna a cor do gatinho
    def get_cor(self):
        return self.__cor

    # Retorna True se o gatinho foi adotado, False caso contrário
    def adotado(self):
        return self.__adotado

    # Marca o gatinho como adotado
    def adotar(self):
        self.__adotado = True  # Define o atributo adotado como True
        print(f"{self.__nome} foi adotado!")  # Imprime uma mensagem informando que o gatinho foi adotado

# Classe para adoção de gatinhos
class AdocaoGatinho:
    # Inicializa um objeto de adoção com o nome do adotante
    def __init__(self, adotante):
        self.adotante = adotante  # Atributo público para o nome do adotante

    # Adota um gatinho
    def adotar_gatinho(self, gatinho):
        if not gatinho.adotado():  # Verifica se o gatinho não foi adotado
            gatinho.adotar()  # Marca o gatinho como adotado
            print(f"{self.adotante} adotou {gatinho.get_nome()}")  # Imprime uma mensagem informando sobre a adoção
        else:
            print(f"{gatinho.get_nome()} já foi adotado.")  # Imprime uma mensagem informando que o gatinho já foi adotado

# Subclasse de Gatinho com características especiais
class GatinhoEspecial(Gatinho):
    # Inicializa um objeto GatinhoEspecial com nome, idade, cor e característica especial
    def __init__(self, nome, idade, cor, caracteristica_especial):
        super().__init__(nome, idade, cor)  # Chama o construtor da classe base Gatinho
        self.caracteristica_especial = caracteristica_especial  # Atributo público para a característica especial do gatinho

# Classe abstrata para animais
class Animal(ABC):
    # Método abstrato que deve ser implementado pelas subclasses
    @abstractmethod
    def fazer_som(self):
        pass

# Classe Gato que herda de Gatinho e implementa Animal
class Gato(Gatinho, Animal):
    # Inicializa um objeto Gato com nome, idade, cor, raça
    def __init__(self, nome, idade, cor, raca):
        Gatinho.__init__(self, nome, idade, cor)  # Chama o construtor da classe base Gatinho
        self.__raca = raca  # Atributo privado para a raça do gato

    # Retorna o som emitido pelo gato
    def fazer_som(self):
        return "Miau"  # Retorna uma string representando o som de um gato

# Exemplo de uso do sistema
if __name__ == "__main__":
    # Criando alguns gatinhos
    gato1 = Gatinho("Bolinha", 2, "branco")
    gato2 = GatinhoEspecial("Frajola", 1, "preto e branco", "Manchas pretas")
    gato3 = Gato("Whiskas", 3, "amarelo", "Persa")

    # Criando uma lista de gatinhos disponíveis
    gatinhos_disponiveis.extend([gato1, gato2, gato3])

    # Adotando um gatinho
    adocao1 = AdocaoGatinho("João")
    adocao1.adotar_gatinho(gato1)

    # Tentando adotar um gatinho já adotado
    adocao2 = AdocaoGatinho("Maria")
    adocao2.adotar_gatinho(gato1)

    # Testando herança e método abstrato
    print(gato3.fazer_som())  # Imprime "Miau"
