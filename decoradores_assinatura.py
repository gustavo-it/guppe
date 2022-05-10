"""
Decorators com diferentes assinaturas

# A Função ordernar recebe dois parâmetros, mas a função aumentar() que está dentro de gritar()
recebe apenas 1 parâmetro, isso ocasiona em um TypeError.
# Para resolver, utilizamos um padrão de projeto chamado Decorator Pattern (utilizando *args e **kwargs)

A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.
"""
# Relembrando


def gritar(funcao):
    """
    gritar() recebe como parâmetro uma função
    A função interna aumentar recebe uma string. Essa string será colocada em caixa alta.
    gritar() retorna a função aumentar()
    """
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar  # Irá executar a função gritar
def saudacao(nome):
    """
    Essa função recebe o parâmetro nome e retorna a string + nome.
    Além de executar a função gritar()
    """
    return f"Olá, eu sou o/a {nome}"


@gritar
def ordernar(principal, acompanhamento):
    return f"Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor."

# Testando


print(saudacao("Angélica"))

# print(ordernar("Hambúrguer", "batata frita"))

# Refatorando


def gritar2(funcao):
    """
    A função interna aumentar() tratando dos elementos extrar com args e kwargs
    """
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar2
def saudacao2(nome):
    return f"Olá, eu sou a {nome}"


@gritar2
def ordernar2(principal, acompanhamento):
    return f"Olá eu gostaria de {principal} acompanhado de {acompanhamento}, por favor."


print(saudacao2("Maria"))
print(ordernar2("Hambúrguer", "batata frita"))


# OBS: Vale lembrar quie podemos utilizar parâmetros nomeados
print(ordernar2(acompanhamento="Batata frita", principal="Bife de fígado"))

# Decorator com argumentos


def verifica_primeiro_argumento(valor):
    """
    lembrando que args retornar uma tupla
    interna() recebe uma funcao como parâmetro, em seguida outra() irá tratar os nossos valores extras
    if o argumento(args) e argumento na posição 0 for diferente do valor pré definido no decorator,
    retorna "valor incorreto....", caso contrário, retorna os valores recebidos pelo usuário.
    depois retorne a função outra e por último retorna a função interna que recebe uma funcao.
    """
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f"Valor incorreto! Primeiro argumento precisa ser {valor}"
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')  # O primeiro argumento tem que ser pizza
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)  # O primeiro argumento tem que ser 10
def soma_dez(num1, num2):
    return num1 + num2


print(soma_dez(10, 12))
print(soma_dez(22, 10))

print(comida_favorita("pizza", "churrasco"))
print(comida_favorita("churrasco", "pizza"))
