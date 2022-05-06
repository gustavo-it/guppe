"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo (seek=procurar)

posso colocar um limite em read() ≥ ex.: print(arquivo.read(50))
"""

arquivo = open("python.txt", encoding="utf-8")
print(arquivo.read())  # Quando executo o print() cursor ficará no final do documento
# Logo, se for executado mais uma vez não irá retornar nada.
# seek() -> A função seek é utilizada para movimentação do cursor pelo arquivo. Ela recebe um
# parâmetro que indica onde queremos colocar o cursor.
# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(20)  # seek(0) irá retornar o cursor a primeira linha do arquivo
print(arquivo.read())
arquivo.seek(0)

# readline() -> Função que lê o arquivo linha a linha (readline -> lê linha)
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
arquivo.seek(0)

# readlines()
print(arquivo.readlines())  # Pega cada linha e coloca em uma lista
# Descobrindo a quantidade de linhas num texto:
# linhas = arquivo.readlines()
# print(len(linhas))
# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo
# no disco do computador e o seu programa. Essa conexão é chamada de streaming. Ao finalizar
# os trabalhos com o arquivo devemos fechar essa conexão. Para isso utilizamos a função close()
"""
Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;
arquivo = open("python.txt")

2 - Trabalhar o arquivo;
print(arquivo.read())

3 - Fechar o arquivo;
arquivo.close()
"""
print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado

arquivo.close()

print(arquivo.closed)
