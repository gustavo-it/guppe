"""
Trye / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuer é DESTRUIR O SEU sistema.
"""
# Else _> É executado somente se não ocorrer o erro.

try:
    numero = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:  # Caso esteja certo, imprima o número que digitei.
    print(f'Você digitou {numero}')

# Finally

try:
    numero = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {numero}')
finally:
    print('Executando o finally')

# OBS: O bloco finally é SEMPRE executado. Independente se houver exceção ou não.

# O finally, geralmente, é utilizado para fechar ou desalocar recursos.

# Exemplo mais complexo
# O programador é responsável pelas entradas das suas funções. Então, trate-as!


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except (ZeroDivisionError, TypeError) as err:  # Passando mais de dois erros
        return f'Não é possível realziar uma divisão por zero: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
