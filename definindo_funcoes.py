"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções desde que iniamos este curso:
- print()
- len()
- max()
- min()
- count()

"""
# Exemplo de utilização de funções:
# cores = ['branco', 'azul', 'rosa', 'preto']

# Utilizando uma função integrada (Built-in) do Python print()
# print(cores)

# cores.append('roxo')
# print(cores)

# DRY - Dont't Repeat Yourself

# Mas então, como definir funções ?
"""
Em python, a forma geral de definir uma função é:

def nome_da_função(parametros_de_entrada):
    bloco da função
    
Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado po underline (Snake Case);
parâmetros de entrada -> São opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser
opcionais_ou_não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que 
estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos : que é 
utilizado em Python para definir blocos;
"""

# Definindo a primeira função

# Definição


def diz_oi():
    print('oi!')


"""
OBS:

1 - Veja que dentro das nossa funções podemos utilizar outras funções;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer "oi!";
3 - Veja que está função não recebe nenhum parâmetro de entrada;
4 - Veja que está função não retorna nada;
"""

# Utilizando funções

# Chamada de execução
diz_oi()

"""
ATENÇÃO:

Nunca esqueça de utilizar o parênteses ao executar uma função.

Exemplo:

# Errado!
diz_oi

# Certo
diz_oi()

# Errado!
diz_oi ()

"""

# Exemplo 2


def cantar_parabens():
    print('Parabéns pra você'),
    print('No seu aniversário')
    print('Muitas felicidades'),
    print('Muitos anos de vida')


cantar_parabens()

# for n in range(5):
#   print(n)
# cantar_parabens()

# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através
# da variável.

canta = cantar_parabens


canta()
