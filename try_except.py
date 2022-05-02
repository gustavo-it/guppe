"""
O bloco try/except

Utilizamos o bloco tryp/except para tratar erros que podem ocorrer no nosso código. Previnindo
assim que o programa pare de funcionar e o user receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problemas
"""
# Exemplo 1 - Tratando um erro genérico (qualquer tipo de erro)

try:
    docker()
except:
    print('Deu algum problema.')
# Tente executar a função docker(), caso encontre erros, imprima a mensagem de erro.

# OBS: tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal
# é SEMPRE tratar de forma específica.

# Exemplo 3 - Tratando um erro específico
try:
    docker()
except NameError:
    print('Você está utilizando uma função inexistente')

# Exemplo 4 - Tratando um erro específico com detalhes do erro
try:
    docker()
except NameError as err:  # Captura uma exceção do tipo NameError e chame ela de err
    print(f'A aplicação gerou o seguinter erro: {err}')

# Casos em que teremos diferentes tipos de error
# OBS: podemos efetuar diversos tratamentos de erros de uma vez.
try:
  # len(5)
  # geek()
    print('Docker'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return 'Não encontrei a chave'
    except TypeError:
        return 'TypeError'


dic = {'nome': 'docker'}

print(pega_valor(dic, 'nome'))
print(pega_valor(dic, 'idade'))
print(pega_valor(74, 'idade'))
