"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python, utilizamos a função integrada open().
Que literalmente significa 'abrir.'

open() _> Na forma simples de utilização nós passamos apenas um parâmetro de entrada, que neste caso é
o caminho para o arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele
que trabalhamos então.

https://docs.Python.org/3/library/functions.html#open

#OBS: Por padrão a função open() abre o arquivo para leitura, este arquivo deve existir, ou então
teremos o erro FileNotFoundError.

<_io.TextIOWrapper name='python.txt' mode='r' encoding='cp1252'>

mode 'r' _> Modo de Leitura, r _> read() _> ler
"""
arquivo = open("python.txt", encoding="utf-8")  # Definindo encoding como "utf-8" (acentuação)
# print(arquivo)
# print(type(arquivo))

ret = arquivo.read()
print(type(ret))
print(ret)

# Para ler o conteúdo de um arquivo, após a sua abertura, devemos utilizar a função read()

print(arquivo.read())
# OBS: O Python, utiliza um recurso para trabalhar, com arquivos chamando cursor.
# Funciona como o cursor quando estamos escrevendo.
# print(arquivo.read())

# OBS: A função read() lê todo o conteúdo do arquivo.
