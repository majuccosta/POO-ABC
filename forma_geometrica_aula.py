"""
ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

Teoria:
- Uma classe abstrata deve herdar de ABC (Abstract Base Classes)
- A superclasse abstrata precisa ter pelo menos um método abstrato
- As subclasses concretas tem que implementar todos os métodos
  abstratos da superclasse abstrata.
- Precisa importar o módulo abc (abstract base classes)
from abc import ABC, abstractmethod

- O problema da figura geométrica e o cálculo da área e do perímetro.
O gerente do sistema precisa implantar a RN (regra de negócio) que toda
subclasse incluida no sistema precisa ter a funcionalidade de cálculo
da área e de cálculo do perímetro.

- Implemente os itens:

1- A superclasse abstrata FormaGeometrica que herda de ABC (Abstract Base Classes)
2- Dois métodos abstratos: area e perímetro
3- Um objeto da superclasse abstrata FormaGeometrica, teste
4- A subclasse concreta Quadrado que herda da superclasse abatrata FormaGeometrica
5- O construtor com o atributo lado, teste
6- Os métodos get e set, teste
7- Sobreescreva o método abstrato area da superclasse abstrata FormaGeometrica
   area = lado ao quadrado.
8- Um objeto da subclasse Quadrado, teste. Porque deu erro?
9- Sobreescreva também o método abstrato perímetro da superclasse abstrata
   perimetro = 4 . lado
10- Crie um objeto da subclasse Quadrado, teste. Porque não deu erro.
11- Altere o valor do lado, teste
12- A subclasse Circulo que herda da superclasse abstrata FormaGeometrica
13- O construtor com o atributo raio, teste
14- Os métodos get e set, teste
15- Sobreescreva o método abstrato area da superclasse abstrata FormaGeometrica
    area = π . raio ao quadrado
16- Um objeto da subclasse Circulo, teste
17- Sobreescreva também o método perímetro da superclasse abstrata
    perimetro = 2 . π . raio
18- Um objeto da subclasse Circulo, teste
19- Refaça a subclasse Circulo com a constante pi do Python, mostre com duas casas decimais
20- Um método concreto na superclasse para mostrar uma menscagem fixa, teste
21- Mais um método concreto para mostrar uma mensagem na superclasse
    e identifique o objeto da subclasse que chamou o método, teste
22- Refaça o anterior sem mostrar o endereço hexadecimal, mostre só o nome da classe

"""


from abc import ABC, abstractmethod  # Importa o módulo abc (abstract base classes)
class FormaGeometrica(ABC):  # Classe abstrata, herda da classe ABC
    def __init__(self):
        ...  # pass
    # Método abstrato, obrigatório pelo menos um na superclasse abstrata
    @abstractmethod                  # Decorator
    def area(self):                  # Método abstrato
        ...                          # Equivalente: pass
    @abstractmethod                  # Decorator
    def perimetro(self):             # Método abstrato
        pass                         # Equivalente: ...
    def mensagem(self):              # Método concreto
        print('Método concreto da superclasse abstrata FormaGeometrica que herda de ABC')
    def mensagem2(self):             # Método concreto
        print('Método concreto da superclasse abstrata FormaGeometrica que herda de ABC')
        print('Dados do obejto:', self)
    def mensagem3(self):             # Método concreto
        print('Método concreto da superclasse abstrata FormaGeometrica que herda de ABC')
        print('Nome da classe:', self.__class__.__name__)  # nome_objeto.__class__.__name__


# A subclasse concreta Quadrado herda da superclasse abstrata FormaGeometrica
class Quadrado(FormaGeometrica):  # class NomeSubclasse(NomeSuperclasse):  (sintaxe)
    def __init__(self, lado):
        super().__init__()        # Opcional
        self.lado = lado
    def get_lado(self):
        return self.lado
    def set_lado(self, valor):
        self.lado = valor
    # Método obrigatório, sobrescreve o método abstrato da superclasse abstrata
    def area(self):
        vl_area = self.lado ** 2        # vl_area = self.lado * self.lado
        return vl_area
    # Método obrigatório, sobrescreve o método abstrato da superclasse abstrata
    def perimetro(self):
        vl_perimetro = 4 * self.lado
        return vl_perimetro


import math                     # Como usar:    math.pi
from math import pi             # Como usar:    pi
# A subclasse concreta Circulo herda da superclasse abstrata FormaGeometrica
class Circulo(FormaGeometrica):  # class NomeSubclasse(NomeSuperclasse):  (sintaxe)
    def __init__(self, raio=1):             # Construtor
        super().__init__()                  # Opcional
        self.raio = raio                    # Atributo
    def get_raio(self):
        return self.raio
    def set_raio(self, valor):
        self.raio = valor
    # Método obrigatório, sobrescreve o método abstrato da superclasse abstrata
    def area(self):                         # Obrigatório
        vl_area = 3.14 * pow(self.raio, 2)  # vl_area = 3.14 * self.raio ** 2
        return vl_area
    # Método obrigatório, sobrescreve o método abstrato da superclasse abstrata
    def perimetro(self):                    # Obrigatório
        vl_perimetro = 2 * 3.14 * self.raio
        return vl_perimetro
