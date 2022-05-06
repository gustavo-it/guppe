"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os.

os -> Operating System

"""
# Fazer o import
import os

# Verificar qual é o diretório corrente
# getcdw() -> Pega o current work directory - diretório de trabalho corrente(onde você está)
# Retorno o path (caminho) absoluto
print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir()
os.chdir('..')  # Voltando um diretório

print(os.getcwd())

# Podemos checar se um diretório é absoluto ou relativo
print(os.path.isabs('/home/geek/'))

# OBS para usuários Windows
# Se você usar o sistema windows, terá que ter cuidado ao verificar diretórios.
print(os.path.isabs('c:\\Users\\gustavo.adm'))

# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # Em windows ira retornar nt. Em linux ira retornar posix

# Podemos ter mais detalhes no sistema operacional
# print(os.uname()) Checando no linux

print(os.getcwd())  # Nos mostra a localização do diretório de trabalho atual

res = os.path.join(os.getcwd(), 'guppe', 'Html - Fundamentos')  # acrescentando ao caminho essa pasta

os.chdir(res)  # mudando o diretório

print(os.getcwd())

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o
# diretório que será juntado ao atual.

# Podemos listar os arquivos e diretórios com o listdir()
print(os.listdir())

# listando a quantidade de arquivos
print(len(os.listdir('C://')))

# Podemos listar os arquivos e diretório com mais detalhes com scander()
scanner = os.scandir()

arquivos = list(scanner)

print(arquivos)

#  Checando os valores do arquivo
print(dir(arquivos[0]))
print(arquivos[0].inode())  # verificando o endereço na memória
print(arquivos[0].is_dir())  # verificando se é um diretório
print(arquivos[0].is_file())  # verificando se é um arquivo
print(arquivos[0].name)  # verificando o nome
print(arquivos[0].stat())  # Informações do arquivo/pasta
print(arquivos[0].path)  # O caminho
print(arquivos[0].is_symlink())
print(arquivos[0].name)  # pegando o nome do arquivo

# OBS: quando utilizamos a função scandir() nós precisamos fechá-lá, assim quando abrimos um arquivo.
scanner.close()
