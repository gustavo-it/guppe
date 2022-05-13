class Pessoa:

    lista = []

    def __init__(self, nome, sobrenome, idade, altura):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade
        self.__altura = altura

    def mostrar_nome(self):
        return f"Nome completo: {self.__nome} {self.__sobrenome}"

    def mostrar_idade(self):
        return f"Idade: {self.__idade}"

    def mostrar_altura(self):
        return f"Altura: {self.__altura}"

    @classmethod
    def adicionar_a_lista(cls):
        Pessoa.lista.append(usuario.__nome)
        Pessoa.lista.append(usuario.__sobrenome)
        Pessoa.lista.append(usuario.__idade)
        Pessoa.lista.append(usuario.__altura)

    """
    def __repr__(self):
        return f"Dados do usuário Nome Completo: {self.__nome} {self.__sobrenome} Idade: {self.__idade} " \
               f"'Altura: {self.__altura}
    """
    @classmethod
    def exibir_todos_usuarios(cls):
        n = 4
        saida = [Pessoa.lista[i:i + n] for i in range(0, len(Pessoa.lista), n)]
        for linha in saida:
            print(f"Nome completo: {linha[0]} {linha[1]} │ Idade: {linha[2]} │ Altura: {linha[3]}")
        return ''

    """@classmethod
    def mostrar_usuarios(cls):
        for valor in Pessoa.lista:
            while valor in Pessoa.lista:
                nome, sobrenome, idade, altura = Pessoa.lista[0], Pessoa.lista[1], Pessoa.lista[2], Pessoa.lista[3]
                Pessoa.lista.pop(0)
                Pessoa.lista.pop(0)
                Pessoa.lista.pop(0)
                Pessoa.lista.pop(0)
                print(f"Nome completo: {nome} {sobrenome} │ Idade: {idade} │ Altura: {altura}")
        return ''"""
    def __str__(self):
        return f"\nDados do usuário \nNome Completo: {self.__nome} {self.__sobrenome} \nIdade: {self.__idade} " \
               f"\nAltura: {self.__altura}"


usuario = Pessoa("Maria", "Barbosa", 22, 1.58)
usuario.adicionar_a_lista()
print(usuario.mostrar_nome())
usuario1 = Pessoa("Andressa", "Fernandes", 18, 1.58)
usuario1.adicionar_a_lista()
print(usuario1.mostrar_nome())
usuario = Pessoa("Fernanda", "Maria Pereira da Silva", 19, 1.62)
usuario.adicionar_a_lista()
# print(usuario)
# print(usuario1)
#print(usuario.__str__())
variavel = usuario.__str__()
variavel2 = usuario1.__str__()
print(variavel)
print(variavel2)

"""
Método __str__()
* Torna o objeto legível, podendo armazenar em uma variável, por exemplo.
* Gera a saída para o usuário final

Método __repr__()
* Quando precisa do código que reproduz o objeto
* Gera a saída para o desenvolvedor

2022 566003
"""
