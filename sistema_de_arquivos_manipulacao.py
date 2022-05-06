"""
Sistema de arquivos — Manipulação


"""
import os
import tempfile
# Descobrindo se um arquivo

# Paths relativos
print(os.path.exists('arquivos.txt'))  # Verificando no diretório atual se existe esse arquivo

# Diretorio
print(os.path.exists('geek/university'))  # Verificando se existe esse diretório

# Paths absolutos (Raiz)
print(os.path.exists('c://users'))

# Criando arquivos
# forma 1
open("arquivos.txt", "w").close()

# forma 2
open("arquivos2.txt", "a").close()

# forma 3
with open("arquivo3.txt", "w") as arquivo:
    pass  # pass = Não faz nada
try:
    os.mknod("arquivo4.txt")  # Podemos passar também em qual pasta queremos criar
except AttributeError:
    print("Arquivo já existe")
# OBS: se você utilizar no Mac OS, pode haver um erro de PermissionError

# OBS: criando um arquivo via mknod() se o arquivo já existir teremos o erro FileExistsError

# Criando diretórios (Preciso passar o nome dentro de uma variável)
diretorio = "templates"
try:
    diretorio = 'templates'
    os.mkdir(diretorio)
except FileExistsError:
    print("esta pasta já existe.")

# OBS: a função mkdir() cria um diretório se esse não existir. Caso exista, teremos
# FileExistsError

# OBS: se não tivermos permissão para criar o diretório teremos um PermissionError

# Criando vários diretórios
diretorios = 'teste/complemento'
try:
    diretorios = 'teste/complemento'
    os.makedirs(diretorios)
except FileExistsError:
    print("Diretórios já existem")

# OBS: se já existir, teremos um FileExistsError
os.makedirs(diretorios, exist_ok=True)  # Esse comando faz com que não apresente erro caso já exista o dir

# Renomear arquivos e diretório
try:
    os.rename(diretorio, "templates2")  # Primeiro passo o nome atual, nome que quero colocar
except FileExistsError:
    print("Este diretório já teve seu nome alterado.")
# OBS: se o diretório que queremos renomear não estiver vazio, teremos um OSError

# Alterando o nome de um arquivo
try:
    arquivo2 = "novo.txt"
    os.rename(arquivo2, 'novo2.txt')
except FileNotFoundError:
    print("Este arquivo já teve seu nome alterado.")

# Deletando arquivos
# ATENÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório
# eles não vão para a lixeira.
try:
    os.remove("novo2.txt")
except FileNotFoundError:
    print("O arquivo não foi encontrado.")

# OBS: se você estiver no windows e o arquivo que você for deletar estiver em uso,
# você terá um erro.

# OBS: Caso o arquivo não exista, teremos o FileNotFoundError

# OBS: se você informar um diretório ao invés de um arquivo, teremos um IsADirectoruError

# Removendo diretórios vazios


deletar_dir = 'templates2'  # Se o diretório tiver conteudo teremos o OSError
os.rmdir(deletar_dir)


# OBS: se o diretório tiver qualquer conteúdo teremos um OSError

# OBS: se o diretório não existir teremos um FileNotFoundError

"""
# Removendo uma árvore de diretórios
for arquivo in os.scandir('teste'):
    print(f"{arquivo.name}")
    if arquivo.is_file():  # Se é um arquivo
        os.remove(arquivo.path)  # Remova esse arquivo

    if not arquivo.is_file():  # Se não é um arquivo
        os.rmdir(arquivo.path)  # Remova diretório
"""

# Podemos remover uma árvore de diretórios vazios
# os.removedirs('teste//pasta//subpasta')  # removendo pasta e subpasta

# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.

# ATENÇÃO: ao remover arquivos e diretórios com Python eles não vão para a lixeira.

# Posso utilizar a biblioteca send2trash (pip install send2trash) assim os arquivos vão para lixeira

# Trabalhando com arquivos e diretórios temporários (import tempfile)
# Criando um diretório temporário
with tempfile.TemporaryDirectory() as tmp:
    print(f"Criei o diretório temporário em {tmp}")
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), "w", encoding="utf-8") as arquivo:
        # Adiciona ao caminho o arquivo_temporario.txt
        arquivo.write('Curso de python\n')
        # Escrevendo uma nova linha
    input()  # Serve para deixar o código aberto, pois o arquivo só é mantido enquanto o bloco está aberto.

# Criando um diretório temporário, abrindo o mesmo e dentro dele
# criando um arquivo para escrevermos um texto. No final. Usamos um input() só para mantermos os
# arquivos temporários 'vivos' nos blocos with.

# Criando um arquivo temporário
with tempfile.NamedTemporaryFile() as tmp:
    tmp.write(b'curso python\n')  # Escrevendo no arquivo (o 'b' converte a 'string' para binário)
    print(tmp.name)
    tmp.seek(0)  # Voltando o cursor para o início
    print(tmp.read())  # Imprimindo o texto
    input()

# SEM O BLOCO WITH
arquivo32 = tempfile.NamedTemporaryFile()
arquivo32.write(b'curso python2022\n')
print(arquivo32.name)
print(arquivo32.read())
input()
arquivo32.close()

# OBS: em arquivos temporários só conseguimos escrever bit, por isso, utilizamos b''
