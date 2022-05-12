"""
Programação Orientada a Objetos — POO

— POO é um paradigma de programação que utiliza que mapeamento de objetos do mundo real
para modelos computacionais.

— Paradigma de programação é a forma/metodologia utilizada para pensar/desenvolver sistemas

Principais elementos da Orientação a Objetos:
— Classe ≥ Modelo do objeto real sendo representado computacionalmente;
— Atributo ≥ Característica do objeto.
— Método ≥ Comportamento do objeto (funções).
— Construtor ≥ Método especial utilizado para criar os objetos;
— Objeto ≥ Instância da classe.
"""


class Produto:
    pass  # Quer dizer que não tenho nenhum método


ps4 = Produto()  # Utilizando o construtor padrão da class. Que é o seu próprio nome()

print(ps4)
print(type(ps4))
