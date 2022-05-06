"""
StringIO

ATENÇÃO: para ler ou escrever dados em arquivos do sistema operacional o 'software' precisa ter
permissão:
    — Permissão de Leitura ≥ Para ler o arquivo.
    — Permissão de Escrita ≥ Para escrever o arquivo.

StringIO ≥ Utilizado para ler e criar arquivos em memória(Não irá gravar no disco).
"""

# Primeiro fazemos o import
from io import StringIO

mensagem = "Está é apenas uma string normal"

# Podemos criar um arquivo em memória já com uma 'string' inserida ou mesmo vazio para inserirmos textos depois.
arquivo = StringIO(mensagem + '\n')

# Agora tendo o arquivo, podemos utilizar tudo que já sabemos sobre arquivos
print(arquivo.read())

# Escrevendo outros textos
arquivo.write("Outro texto")

# Podemos inclusive movimentar o cursor
arquivo.seek(0)
print(arquivo.read())
