"""
Escrevendo em arquivos

# OBS: ao abrir um arquivo para leitura, não podemos realizar a escrita nele, apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

#OBS: ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

# OBS: para escrevermos dados num arquivo, após abrir o arquivo utilizamos a função write().
Está função recebe uma 'string' como parâmetro, caso contrário teremos um 'TypeError'.

Abrindo um arquivo para escrita com o modo "w", se o arquivo não existir será criado, caso ele
já exista, o anterior será apagado e um novo será criado. Dessa forma, todo o conteúdo no arquivo
anterior é perdido.
"""

# Exemplo de escrita - modo "w" - write(escrita ou escrever)

with open("novo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Escrever dados em arquivo é muito fácil. \n")
    arquivo.write("Podemos colocar quantas linhas quisermos. \n")
    arquivo.write("Esta é a última linha.")

# Recebendo dados do usuário

with open("frutas.txt", "w", encoding="utf-8") as arquivo2:
    while True:  # Enquanto for True, execute o código
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo2.write(fruta)
            arquivo2.write('\n')
        else:
            break
