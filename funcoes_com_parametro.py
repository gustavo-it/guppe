"""
Funções com parâmetro (de entrada):

- Funções que recebem dados para serem processados na mesma;

Se nós pensarmos num programa qualquer, geralmente temos:

entrada _> processamento _> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada, mas possuem saída;
- Possuem entrada e saída;

"""


# Refatorando uma função quadrado_de_7


def quadrado(numero):
    # return numero * numero
    return numero ** 2


print(quadrado(4))  # Preciso passar o parâmetro
print(quadrado(5))
print(quadrado(6))


# Refatorando cantar_parabens


def cantar_parabens(aniversariante):
    return f'\n Parabéns para você \n nesta data querida, \n {aniversariante}'


print(cantar_parabens('Maria'))
print(cantar_parabens('Patrícia'))


# Funções podem ter N parãmetros de entrada, ou seja, podemos receber como entrada
# Numa função quantos parâmetros forem necessários. Eles são separados por vírgula.


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(multiplica(10, 10))
print(outra(1, 2, 'Python '))


# OBS: Se nós informarmos um número errado de parâmetro ou argumentos, teremos TypeError

# A diferença entre Parâmetros e Argumentos
# ---- Parâmetros são variáveis declaradas na definição de uma função;
# ---- Argumentos são dados passados durante a execução de uma função;

# A ordem dos parâmetros importa!

# Argumentos nomeados (KeyWord Arguments)

# Caso utilizemos nomes dos parãmetros nos argumentos para informá-los, podemos utilizar
# qualquer ordem.

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é: {nome} {sobrenome}'


print(nome_completo(nome='Testando', sobrenome='Teste'))
print(nome_completo(sobrenome='Invertendo', nome='nome'))


# Erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for numero in numeros:  # Para cada número em numeros
        if numero % 2 != 0:  # Se ele for diferente de par (Ímpar)
            total = total + numero  # O total irá receber total + número
    return total  # Retornando o valor final (Lembrando que devo executar o retorno fora do bloco).


lista = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(lista))
