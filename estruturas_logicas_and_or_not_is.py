"""
Booleanos
Estruturas lógica: and (e), or (ou), not (não), is( é)

Operadores unários:
    -Not, is

Operadores binários:
    -And, or

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False,
se for False vira True
Para o 'is', o valor é comparado com um segundo.
"""

ativo = True
logado = False

if ativo:
    print("Bem vindo usuário")
else:
    print("Ative sua conta")

print(ativo is True)
# if logado is False: utilizando a variável is
    # print("Você precisa ativar sua conta.")
# else:
    # print("Bem-vindo usuário")


#if ativo and logado:
   # print("Bem-vindo usuário!")
#else:
   # print("Você precisa ativar sua conta")

# nota1 = float(input("Digite a nota 1: "))
# nota2 = float(input("Digite a nota 2: "))

# if nota1 >= 0.0 and nota1 <= 10.0 and nota2 >= 0.0 and nota2 <= 10.0:
   #  print((nota1 + nota2) / 2)
# else:
    # print("Valores inválidos")

#print("Digite algum dos seguintes valores \n somar \n subtrair \n divisão \n multiplicar")
#operacao = input("Digite aqui a operação: ")

#if operacao == "somar":
      #  numero1 = int(input("Digite aqui o número 1: "))
      #  numero2 = int(input("Digite aqui o número 2: "))
      #  print(f"A soma dos valores é {numero1 + numero2}")

#elif operacao == "subtrair":
       # numero1 = int(input("Digite aqui o número 1: "))
       # numero2 = int(input("Digite aqui o número 2: "))
       # print(f"A subtracao dos valores é {numero1 - numero2}")

#elif operacao == "divisão":
     #   numero1 = int(input("Digite aqui o número 1: "))
      #  numero2 = int(input("Digite aqui o número 2: "))
      #  print(f"A divisão dos valores é {numero1 / numero2}")

#elif operacao == "multiplicar":
      #  numero1 = int(input("Digite aqui o número 1: "))
       # numero2 = int(input("Digite aqui o número 2: "))
       # print(f"A multiplicação dos dois números é {numero1 * numero2}")

# ter pelo menos 65 anos/ ou ter trabalhado pelo menos 30 anos/ ou ter pelo menos 60 anos e trabalho pelo menos 25

# idade = int(input("Digite aqui sua idade: "))
# tempo_de_trabalho = int(input("Digite os anos trabalhados: "))

# if idade >= 65 or tempo_de_trabalho >= 30:
    # print("Parabéns, você pode se aposentar")

# elif idade >= 60 and tempo_de_trabalho >= 25:
    # Print("Parabéns, você pode se aposentar")


# else:
    # Print("Você não pode se aposentar")


salario = float(input("Digite seu salário: "))
emprestimo = float(input("Digite o valor do seu empréstimo: "))
prestacao = (emprestimo/salario) * 100
# Transformando em porcentagem


if prestacao >= 20.0:
    print("Empréstimo não concedido")

else:
    print("Empréstimo concedido")
