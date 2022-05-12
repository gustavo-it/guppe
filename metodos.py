"""
POO — Métodos

— Métodos (funções) ≥ que representam os comportamentos do objeto, ou seja, as ações que
    este objeto pode realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum
    que muito provavelmente iríamos querer representar no nosso sistema é o de ligar e desligar a mesma.

Em Python, dividimos os métodos, assim como os atributos, em 2 grupos: métodos de instância
e Métodos de Classe.

# Métodos de Instância

# O método dunder init __init__ é um método especial chamado construtor e a sua função
é construir o objeto a partir da classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

ATENÇÃO! Por mais que possamos criar nossas próprias funções utilizando dunder (underline no inicio e fim)
não é aconselhado. Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento
dessas funções mágicas internas de linguagem. Então, evite ao máximo. De preferência nunca o faça.

# Méotodos são escritos em letras minúscula. Se o nome for composto, o nome terá as palavras
separadas por underline.

# Métodos de Classe em Python são conhecidos como Métodos Estáticos em outras linguagens.
"""
from passlib.hash import pbkdf2_sha256 as cryp
"""
Utilizando uma biblioteca para criptografia de senha
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False  # Definindo valor inicial padrão


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limites = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return self.__valor * (100 - porcentagem) / 100


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        """
        Utilizando a função encrypt
        passando a string que quero encriptar, no caso, a senha.
        passando 2 parâmetros extras, que vai definir quão forte será essa senha.
        rounds irá embaralhar a senha, salt_size é o tamanho da parte do texto que será juntada
        a outra para criptografar.
        """
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

    def checa_senha(self, senha):
        """
        Irá verificar se a senha recebida é igual a senha do objeto instanciado
        """
        if cryp.verify(senha, self.__senha):
            return True
        return False


# p1 = Produto("Bolacha", "Bolacha maria", 3.20)
# print(p1.desconto(20))  # 2.56
# print(Produto.desconto(p1, 40))  # p1 = self; desconto

# user1 = Usuario("Maria", "Braga", "braga_maria@gmail.com", "123456")
# user2 = Usuario("Fernanda", "Silva", "fernandaaa_s@gmail.com", "rasd55")

# print(user1.nome_completo())
# print(user2.nome_completo())

nome = input("Informe o nome: ")
sobrenome = input("Informe o sobrenome: ")
email = input("Informe o email: ")
senha = input("Informe a sua senha: ")
confirma_senha = input("Confirme a senha: ")

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print("Senha não confere...")
    exit(1)

print("Usuário criado com sucesso!")

senha = input("Informe a senha para acesso: ")

if user.checa_senha(senha):
    print("Acesso permitido")
else:
    print("Acesso negado")

print(f"Senha User criptografada: {user._Usuario__senha}")


# Métodos de Classe
# Refatorando a class Usuario
# Para criar um método de class, precisamos utilizar o decorator @classhmethod
# O parâmetro que colocamos na função após o @classmethod é 'cls' que vem de class. É a própria class


class Usuario2:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        """
        Para criar um método de class, precisamos utilizar o decorator @classmethod
        O parâmetro que colocamos na função após @classmethod é 'cls' que vem de class. É a própria class
        """
        print(f"Classe: {cls}")  # Passando o nome da class
        return f"Temos {cls.contador} usuário(s) no sistema"  # Passamos o valor de contador

    @staticmethod
    def definicao():
        """
        Método estático
        Note que não temos acesso a class, diferente do método de class.
        """
        return 'Código qualquer'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario2.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        """
        Utilizando a função encrypt
        passando a string que quero encriptar, no caso, a senha.
        passando 2 parâmetros extras, que vai definir quão forte será essa senha.
        rounds irá embaralhar a senha, salt_size é o tamanho da parte do texto que será juntada
        a outra para criptografar.
        """
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario2.contador = self.__id
        """
        Utilizando o método __gera.usuario() para retornar o nome do usuario
        """
        print(f"Usuário criado: {self.__gera_usuario()}")

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

    def checa_senha(self, senha):
        """
        Irá verificar se a senha recebida é igual a senha do objeto instanciado
        """
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        """
        Método privado
        """
        return self.__email.split('@')[0]


usuario2 = Usuario2("Teste", "Testando", "test@gmail.com", "98765")

print(Usuario2.conta_usuarios())  # Forma correta
print(usuario2.conta_usuarios())  # Forma incorreta

# Quando deverei usar método de class ou instância
# Criamos métodos de instância quando precisa fazer acesso a atributos de instância
# Quando não faço acesso a nenhum atributo de instância, posso utilizar os métodos de class.

# Método Estático

print(Usuario2.definicao())  # Acessando definição
print(usuario2.definicao())  # Acessando definição
