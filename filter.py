"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.
"""
# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f"Média: {media}")

# OBS: Assim como a função map(), a filter(), recebe dois parâmetros, sendo
# uma função e um iterável.

# Declaro uma entrada x que ira retornar o x somente se ele for maior que a média
# na lista de dados. valor irá receber os valores que tenho no iterável dados.
res = filter(lambda valor: valor > media, dados)  # Retorna True(vai integrar os dados em filter) ou False
print(type(res))  # Um filter object
print(list(res))
print(f'Novamente: {list(res)}')

# OBS: Assim como na função map() após serem utilizados os dados de filter() eles são
# excluídos da memória.

# Checando dados faltantes com filter
times = ['',
         'Paysandu', '',
         'Castanhal', '',
         'Palmeiras',
         'Atlético Mineiro',
         '',
         '',
         'América Mineiro']

res2 = filter(None, times)  # None faz com que os dados vazios sejam eliminados
print(list(res2))

# 2° forma: filter(lambda pais: len(pais) > 0, paises)
# Nesse caso, para cada posição, ele irá pegar a quantidade de posições do valor
# E caso seja menor que 0 irá eliminar o valor.

# 3° forma: filter(lambda pais: pais !='', paises)

# A diferença entre map() e filter() é:

# Na map() -> recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando
# Para cada elemento do iterável.

# O filter() -> recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas
# Os elementos de acordo com a função.

# Exemplo mais complexo

usuarios = [
    {"username": 'Teste', "tweets": ['Vários', 'Testes', 'de', 'tweets']},
    {"username": 'zeni', "tweets": ['Vários', 'de', 'tweets']},
    {"username": 'zeri', "tweets": []},
    {"username": 'sion', "tweets": []},
    {"username": 'garen', "tweets": ['Vários', 'tweets']},
    {"username": 'samira', "tweets": ['de', 'tweets']}
]

# Filtrar os usuários que estão inativos no twitter
# Estou verificando se a chave tweets está vazia. Se ela estiver vazia, irei acrescentar
# a inativos os usuarios que não tem nada em tweet
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)

# Forma 2: inativos = list(filter(lambda usuario: Not usuario['tweets'], usuarios))

# Combinar filter() e map()

nomes = ['Vanessa', 'Luara', 'Lua', 'Fernanda', 'Ana']

# Devemos criar uma lista contendo 'Sua instrutora é:' + nome_da_instrutora, desde que
# cada nome tenha menos de 5 caracteres.
# Estou passando o map() para pegar cada namo e filtrando com o filter() para me retornar somente
# nomes que tem menos de 5 letras
lista = list(map(lambda nome: f'Sua instrutora é: {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)

# Encontrar a música mais e menos tocada sem usar max() e min()
