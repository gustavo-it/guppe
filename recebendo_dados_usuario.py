""""
recebendo dados do usuário

input() -> todo dado recebido via input é do tipo string

em python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples duplas;
- Aspas duplas triplas;

- Aspas simples -> 'nome';
- Aspas duplas -> "nome";
- Aspas simples duplas -> ''nome''

"""
# Entrada de dados
nome = input("Digite seu nome: \n")

print(f'Seja bem vindo(a) {nome}')

idade = int(input("Qual sua idade: \n"))

# Processamento

# Saída de dados

print(f'O {nome} tem {idade} anos') # outra forma de imprimir print('O {0} tem {1} anos'.format(nome, idade))

"""
# int(idade) => cast

cast é a conversão de um tipo de dado para outro

"""

print(f'O {nome} nasceu em {2022 - int(idade)}')
# Maneira mais atual



