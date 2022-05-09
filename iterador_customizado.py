"""
Escrevendo um iterador customizado


"""


class Contador:
    def __init__(self, menor, maior):
        """__init__ é o construtor. Responsável por criar os objetos a partir da classe
        self representa o próprio objeto. É sempre o primeiro parâmetro na função que está dentro da classe.
        """
        self.menor = menor  
        self.maior = maior

    def __iter__(self):  # Transformando o objeto em iterable. Depois disso posso utilizar a função iter()
        return self

    def __next__(self):  # Todo valor recebe a função next()
        """
        Enquanto o número menor for menor que o número maior, irei dizer que o número menor é igual a número menor
        mais 1. Esse valor será armazenado na variável número em cada volta e irá me retornar a variável número.
        Tratando o erro que acontece quando não tenho mais valores com 'raise StopIteration'.
        """
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


com = Contador(1, 61)
it = iter(com)

print(com.menor)
print(com.maior)
print(next(it))
print(next(it))

for n in Contador(1, 10):
    print(n)
