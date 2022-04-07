# for numero in range(0, 100+1):
   # print(numero)
# Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída cada um dos algarismos.

# numero = int(input('Digite um número: '))

# for num in range(0, numero+1):
    # if num % 2 == 0:
        # print(num)
#numero = int(input('Digite um número: '))
#n = str(numero)


#if numero > 100 and numero < 999:
   # print(n[0])
   # print(n[1])
   # print(n[2])

# Escreva um programa que leia um número e calcule a soma de todos os divisores desse número
nome = 'Docker Container'

for letra in enumerate(nome):
    print(letra)

impar = 0

valor_inical, valor_final = [int(x) for x in input('Digite o valor inicial e valor final: ').split()]

for i in list(range(valor_inical, valor_final)):
    if i % 2 != 0:
        impar = impar + i
print(f'A soma é {impar}')

inicio = int(input('Digite o valor inicial: '))
fim = int(input('Digite o valor final: '))
soma = 0

for numero in range(inicio, fim):
    if numero % 2 == 1:
        soma = soma + numero
print(f'A soma é {soma}')
