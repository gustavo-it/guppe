"""
Estruturas condicionais
if, else, elif
"""

idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem 18 anos")
elif idade == 26:
    print("Tem 26 anos")
else:
    print("Maior de idade")


