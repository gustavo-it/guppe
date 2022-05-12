"""
POO — Classes

Em POO, 'Classes' nada mais são do que modelos dos objetos reais sendo
representados computacionalmente.

Imagine que queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
    — Atributos ≥ Representam as características do objeto, ou seja, pelos atributos
    conseguimos representar computacionalmente os estados de um objeto. No caso da lâmpada,
    por exemplo, possivelmente iríamos querer saber se a lâmpada é 110 ou 220 ‘volts’, se ela
    é branca, amarela, vermelha ou outra cor, qual é a luminosidade dela, etc.

    — Métodos (funções) ≥ que representam os comportamentos do objeto, ou seja, as ações que
    este objeto pode realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum
    que muito provavelmente iríamos querer representar no nosso sistema é o de ligar e desligar a mesma.

Em Python, para definir uma classe utilizamos a palavra reservada class.

OBS: utilizamos a palavra 'pass.' em Python, quando temos um bloco de código que ainda não
está implementado.

OBS: quando nomeamos as nossas classes em Python, utilizamos por convenção o nome com inicial
em maiúsculo. Se o nome for composto, definimos as iniciais de ambas as palavras em maiúsculo,
todas juntas.

Dica: em computação não utilizamos: acentuação, caracteres especiais, espaços ou similares
para nomes de classes, atributos, métodos, arquivos, diretórios e, etc.

OBS: quando estamos planejando um 'software' e definimos quais classes teremos que ter no sistema,
chamamdos estes objetos que serão mapeados para classes de entidade.
"""


class Lampada:
    pass


lamp = Lampada()
print(type(lamp))


class ContaCorrente:
    pass
