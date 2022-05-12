"""
POO — Atributos

— Atributos ≥ Representam as características do objeto, ou seja, pelos atributos
    conseguimos representar computacionalmente os estados de um objeto. No caso da lâmpada,
    por exemplo, possivelmente iríamos querer saber se a lâmpada é 110 ou 220 ‘volts’, se ela
    é branca, amarela, vermelha ou outra cor, qual é a luminosidade dela, etc.

Em Python, dividimos os atributos em 3 grupos:
    — Atributos:
    — de instância;
    — de classe;
    — dinâmicos;

# Atributos de instância: São atributos declarados dentro método construtor.

# OBS: método construtor: é um método especial utilizado para a construção do objeto.

Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da própria classe onde está declarado,
utiliza-se __duplo underscore no início de seu nome.

Isso é conhecido também como Name Mangling (É a junção do nome da class + nome do atributo).

"""
# Classes com Atributo de Instância Público


class Lampada:
    """
    Atributos de instância
    __init__ = é o método construtor do Python e é nele que fazemos a declaração dos atributos.
    self(pode ser usada qualquer palavra no lugar) = Estamos nos referindo ao próprio objeto que executa o método.
    """

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False  # Definindo um valor padrão para objeto


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    """
    Com self quero dizer que:
    O objeto usuário no atributo nome, irá receber nome, fazendo o mesmo para os outros atributos.
    """

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


ps4 = Produto('ps4', 'videogame', 1400)  # É o método __init__sendo executado

# Atributos Públicos e Atributos Privados (visibilidade dos atributos)


class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        return self.__senha

    def mostra_email(self):
        return self.email


# OBS: lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplo

user = Acesso("user@gmail.com", "123456")  # user é uma instância, ou seja, um objeto da class Acesso.

print(user.email)
# print(user.__senha)  AttributeError
# print(dir(user))

print(user._Acesso__senha)  # Temos acesso. Mas não deveríamos fazer este acesso. (Name Mangling)
print(user.mostra_senha())  # Executando um método que está em uma class
print(user.mostra_email())

# O que significa atributos de instância?
# Significa, que ao criarmos instâncias/objetos de uma classe, todas as instâncias
# terão estes atributos. Cada instância terá os seus próprios valores

user1 = Acesso("user1@gmail.com", "12345")
user2 = Acesso("user2@gmail.com", "6789")

print(user1.mostra_email())
print(user2.mostra_email())

# Atributos de Classe

p1 = Produto("PlayStation 4", "Vídeo Game", 2999.99)
p2 = Produto("Xbox Series S", "Video Game", 2000.00)


# Atributos de classe, são atributos, claro, declarados diretamente na classe, ou seja,
# Fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre
# todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter os seus próprios
# valores, como é o caso dos atributos de instância, com os atributos de classe todas as
# instâncias terão o mesmo valor para este atributo.

# Refatorando a classe Produto:


class Produto2:
    # Atributo de class
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        """
        Criando o parâmetro de classe "contador"
        definindo que id irá receber o parâmetro contador + 1
        para cada objeto criado o valor de contador será alterado, recebendo o id como novo valor.
        """
        self.id = Produto2.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto2.imposto)  # Chamando um atributo de class
        Produto2.contador = self.id


p3 = Produto2("Mesa digitalizadora", "Mesa para desenhar", 999.99)
p4 = Produto2("Kit talheres", "Kit com facas, colheres e garfos", 445.62)

print(p3.imposto)  # Acesso possível, mas incorreto de um atributo de class
print(p4.imposto)  # Acesso possível, mas incorreto de um atributo de class

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe
print(Produto2.imposto)  # Acesso correto de um atributo de class
print(p3.id)
print(p4.id)

# OBS: Em linguagens como o java, os atributos conhecidos como atributos de classe aqui em Python
# são chamados atributos estáticos;

# Atributos Dinâmicos ≥ atributos de instância que pode ser criado em tempo de execução.
# OBS: O atributo dinâmico será exclusivo da instância que o criou.

p5 = Produto2("biscoito", "biscoito de chocolate", 2.88)
p6 = Produto2("danone", "danone de morango", 8.65)

# Criando um atributo dinâmico em tempo de execução.

p5.peso = "5.gramas"  # Note que na classe Produto não existe o atributo peso
print(f"Produto: {p5.nome}, Descrição: {p5.descricao}, Valor: {p5.valor}, Peso: {p5.peso}")

# Deletando atributos
print(p5.__dict__)  # imprimindo a estrutura dos objetos
print(p6.__dict__)

del p5.peso  # deletandoo atributo dinâmico do produto
# Posso deletar atributos de instâncias também

print(p5.__dict__)
