"""
Mapas também conhecidos em Python como dicionários

"""
receita = {
    'janeiro': 100,
    'fevereiro': 200,
    'março': 300
}
print(receita)
# Interar sobre dicionários


for chave in receita:  # Pra cada chave dentro de receita
    print(chave)  # Imprima a chave

for valor in receita:  # Pra cada valor dentro de receita
    print(receita[valor])  # Imprima o valor da receita. Passando primeiro o dicionário e entre parênteses o valor

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')  # '{receita[chave]}' pega o valor da chave.

# Ter acesso a todas as chaves
print(receita.keys())  # Retornará um dicionário de chaves

# Retornando o valor (Maneira mais recomendada)
for valor in receita.keys():
    print(receita[valor])

# Acessando os valores (Maneira mais recomendada)
print(receita.values())  # Retornará um dicionário de valores

for valor in receita.values():
    print(valor)

# Desenpacotamento de dicionários

print(receita.items())

for chave, valor in receita.items():  # Para cada chave e valor em receita, imprima chave e valor
    print(f'chave={chave} e valor={valor}')

# Soma*, valor máximo*, valor mínimo*, tamanho

# Elementos com o '*' só podemos obter se os valores forem todos inteiros ou reais

print(f'A soma total é: {sum(receita.values())}')
print(f'O maior valor é: {max(receita.values())}')
print(f'O menor valor é: {min(receita.values())}')
print(f'O tamanho do dicionário é: {len(receita)}')
