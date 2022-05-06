"""
Modos de abertura de arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo SEMPRE. Não controlamos o cursor.
+ -> Abre para o modo de atualização: leitura e Escrita(Temos o controle do cursor).
#OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo
será adicionado ao final.
"""
try:
    with open("universo.txt", "x", encoding="utf-8") as universo:
        universo.write("Teste de conteúdo. \n")
except FileExistsError:
    print("Um arquivo com esse nome já existe.")

with open('frutas.txt', "a", encoding="utf-8") as frutas:
    while True:
        fruta = input("Digite uma frutaou sair: ")
        if fruta != 'sair':
            frutas.write(fruta)
            frutas.write('\n')
        else:
            break

# Acrescentando linhas
with open("frutas.txt", 'w+', encoding="utf-8") as arquivo:
    arquivo.write("segunda linha \n")
    arquivo.write("Inserindo valores na linha que eu quero \n")
