"""
O bloco with

Passos para se trabalhar com arquivos:
1 - Abrimos o arquivo;
2 - Trabalhamos com o arquivo;
3 - Fechamos o arquivo;

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados
são fechados após o bloco with.
"""

# O bloco with - Forma Pythônica de manipular arquivos
with open('segundo_texto.txt', encoding="utf-8") as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)
