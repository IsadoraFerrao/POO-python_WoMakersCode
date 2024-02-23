from abc import ABC, abstractmethod

class Animal(ABC):  # Classe abstrata Animal
    def __init__(self, nome, idade, cor):
        self.__nome = nome
        self.__idade = idade
        self.__cor = cor
        self.__adotado = False
        
    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_cor(self):
        return self.__cor

    @abstractmethod
    def fazer_som(self):  # Método abstrato que deve ser implementado nas subclasses
        pass

class Gato(Animal):
    def __init__(self, nome, idade, cor, raca):
        super().__init__(nome, idade, cor)
        self.__raca = raca
        
    def get_raca(self):
        return self.__raca
    
    def fazer_som(self):  # Implementação do método abstrato fazer_som para a classe Gato
        return "Miau"

class Adotante:
    def __init__(self, nome):
        self.nome = nome

class AdocaoGatinho:
    def __init__(self, animal, adotante):
        self.animal = animal
        self.adotante = adotante

############## TESTES ###################
#gatinho1 = Animal("Bolinha", 2, "branco")
#gatinho2 = Animal("Frajola", 1, "preto e branco")

# Testando os métodos da classe Gato
#print("Nome do gatinho 1:", gatinho1.get_nome())
#print("Idade do gatinho 1:", gatinho1.get_idade())
#print("Cor do gatinho 1:", gatinho1.get_cor())

# Testando herança simples
#gatinho3 = Gato("Bolinha", 2, "branco", "Siamês")
#gatinho4 = Gato("Frajola", 1, "preto e branco", "Vira-lata")
#print("Raça do gatinho 3:", gatinho3.get_raca())

# Testando herança múltipla

# Criando uma instância de Animal e Adotante
#animal01 = Animal("Whiskers", 2, "branco")
#adotante01 = Adotante("João")

# Criando uma instância de AdocaoGatinho
#adocao = AdocaoGatinho(animal01, adotante01)

# Acessando os atributos do animal e do adotante na instância de AdocaoGatinho
#print("Nome do gatinho adotado:", adocao.animal.get_nome())
#print("Idade do gatinho adotado:", adocao.animal.get_idade())
#print("Cor do gatinho adotado:", adocao.animal.get_cor())
#print("Nome do adotante:", adocao.adotante.nome)

# Testando o método fazer_som() para classes abstratas

#gatinho3 = Gato("Bolinha", 2, "branco", "Siamês")
#gatinho4 = Gato("Frajola", 1, "preto e branco", "Vira-lata")

#print("Som do gatinho 3:", gatinho3.fazer_som())
#print("Som do gatinho 4:", gatinho4.fazer_som())

