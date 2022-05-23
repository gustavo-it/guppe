"""
POO - Métodos mágicos

Métodos mágicos, são todos os métodos que utilizam dunder.

dunder init -> __init__()

Dunder > Double Underscore

__repr__ -> Representação do objeto

__str__ -> Apresenta ao usuário final o objeto (Tem preferência sobre o __repr__).

__len__ -> retorna a quantidade de elementos

__del__ -> Irá exibir uma mensagem, dizendo que o objeto foi excluido.

__add__ -> Permite a união de dois valores

__mul__ -> Multiplicar, o segundo valor precisa ser um inteiro (int)
"""


from ast import Try


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return self.titulo

    def __str__(self):
        return self.titulo

    def __len__(self):  # definindo que o len do meu livro, será o número de páginas, podendo ser qualquer outro valor
        #return self.paginas
        return (len(self.titulo))

    def __del__(self):
        print('Um objeto do tipo livro foi deletado da memória')

    def __add__(self, outro):  # Juntando dois valores
        """Recebe o primeiro parâmetro (livro) e o outro (livro2)"""
        return f"{self} - {outro}"

    def __mul__(self, outro):
        if isinstance(outro, int):
            """isinstance retorna true se o objeto for do tipo especificado, no caso int"""
            msg = ''
            for n in range(outro):
                msg = msg + ' ' +str(self)
            return msg
        return "Não posso multiplicar"

livro = Livro("Python programação", "Da vinci", 400)
livro2 = Livro("PHP", "Da vinci", 450)

print(livro)
print(livro2)
print(len(livro))
print(livro + livro2)
print(livro * 3)

"""
OBS: Irá aparecer a mensagem do método __del__ 
isso acontece porque depois que o programa é finalizado, o python automaticamente exclui
da memória os valores.
"""
