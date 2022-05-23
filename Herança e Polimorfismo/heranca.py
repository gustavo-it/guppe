"""
POO - Herança (Inheritance)

A ideia de herança é reaproveitar o código. Também extender nossas classes.

OBS: Com a herança a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

Imagine um banco:

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionário
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

Perguntar: Existe alguma entidade genérica o suficiente par encapsular os atributos
e métodos comuns a outras entidades?

class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


cliente1 = Cliente("Maria", "Fernanda", "123.456.298-54", 5000)
funcionario1 = Funcionario("Amanda", "Maria", "546.254.256-65", 56987)
print(cliente1.nome_completo())
print(funcionario1.nome_completo())

OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e métodos
da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super classe;
    - Classe mãe;
    - Classe pai;
    - Classe base;
    - Classe genérica;

Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionario]
    - Sub classe;
    - Classe filha;
    - Classe específica;

Sobrescrita de método, ocorre quando reescrevemos um método presente na super classe
em classes filhas.
"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):  # Aqui entra a herança. Esse cliente é do tipo Pessoa.
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
#       Pessoa.__init__(self, nome, sobrenome, cpf) segunda maneira de chamar a Super classe        
        super().__init__(nome, sobrenome, cpf)  # Super é o modo como faço acesso a Super classe (Pessoa)
        self.__renda = renda


class Funcionario(Pessoa): 
    """Funcionário herda de Pessoa."""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())  # Acessando o método nome_completo() em Pessoa
        print(self._Pessoa__cpf)  # Acessando o cpf
        return f"Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}"  # Chamando o nome na classe Pessoa


cliente1 = Cliente("Maria", "Fernanda", "123.456.298-54", 5000)
funcionario1 = Funcionario("Amanda", "Maria", "546.254.256-65", 56987)
print(cliente1.nome_completo())  # chamando método que está na classe Pessoa
print(funcionario1.nome_completo())

# Sobrescrita de métodos (Overriding)
# Reemplementar o método da classe pai na classe filha
# COM SUPER, CONSIGO FAZER ACESSO A QUALQUER ATRIBUTO OU MÉTODO DA SUPER CLASSE
