"""
Len, Abs, Sum, Round

# Len

len() _> Retorna o tamanho (ou seja, o número de itens) de um iterável

abs() _> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria
o seu valor real sem o sinal.

sum() _> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna
a soma dos elementos. Incluindo o valor inicial.

#OBS: Inicial 'default' = 0

round() _> Retorna um número arredondado para 'n' digito de precisão após a casa decimal.
Se a prcisão não for informada retorna o inteiro mais próximo da entrada.
"""
# Dunder len
print('Docker Cointainer'.__len__())

# Abs
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# sum
print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 5))

print(sum({'a': 5, 'b': 10}.values()))

# round
print(round(10.2))

print(round(10.5))

print(round(10.6))

print(round(1.212121212121, 2))  # Estou pasando quantas casas decimais quero que o número tenha

print(round(1.219999999, 2))  # Estou pasando quantas casas decimais quero que o número tenha
