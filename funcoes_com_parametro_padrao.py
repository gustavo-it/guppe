"""
Funções com Parâmetro Padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional

print('Docker Container')

print()

"""
# Exemplo de função onde a passagem de parâmetro seja obrigatória


def quadrado(numero):
    return numero ** 2


print(quadrado(22))


def exponecial(numero=4, potencia=2):  # Passando um valor padrão para o parâmetro
    return numero ** potencia


print(exponecial(2, 3))
print(exponecial(3, 2))
print(exponecial(5))
print(exponecial())


# OBS: Se o usuário passar somente 1 argumento, este será atribuido ao parâmetro número,
# e será calculado o quadrado deste número;
# Se o usuário passar 2 argumentos. O primeiro será atribuído ao parâmetro número e o segundo
# ao parâmetro potência. Então será calculada esta potência.

# OBS: em funções Python, os parâmetros com valores 'default' (padrão) DEVEM sermpre estar ao final
# da declaração.

# ERRO !
# def teste(num=2, potencia):
#    return num ** potencia

#  Exemplo mais complexo


def mostra_informacao(nome='docker', instrutor=False):
    if nome == 'docker' and instrutor:
        return 'Bem vindo instrutor Docker!'
    elif nome == 'docker':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('teste'))
print(mostra_informacao('estephy'))

# Por quê utilizar parâmetro com valor default ?
# - Nos permite ser mais flexíveis nas funções;
# - Evita erros com parâmetros incorretos;
# = Nos permite trabalhar com exemplos legíveis de código;


# Quais tipos de dados podemos utilizar como valores default para parâmetros?
# Qualquer tipo de dados:
# - Números, string, floats, booleans, tuplas, dicionários, funções, etc...

# Exemplos

def soma(numero1, numero2):
    return numero1 + numero2


def mat(numero1, numero2, fun=soma):  # Estou definindo como padrão a função soma (somar)
    return fun(numero1, numero2)  # Irá somar o valor entre os parênteses. Valores que serão passados pelo usuário.


def subtracao(numero1, numero2):
    return numero1 - numero2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões....

# Variáveis globais
# Variáveis locais

instrutor = 'Docker'


def diz_oi():
    instrutor = 'Python'  # Variável local. Só é reconhecida no bloco onde foi declarada
    return f'oi {instrutor}'


print(diz_oi())
# OBS: se tivermos uma variável local com o mesmo nome de uma variável global, a variável local
# terá preferência.


def diz_oi():
    prof = 'Geek'  # variável local
    return f'olá {prof}'


print(diz_oi())

# Se puder, evite variáveis globais

# utilizando uma variável global na função
total = 0


def incrementa():
    global total  # Avisando que queremos utilizar a variável global
    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de
# escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador  # Não é uma variável global e nem local, ela está na função de cima.
        contador = contador + 1
        return contador
    return dentro()


print(fora())
