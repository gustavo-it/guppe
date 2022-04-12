# produtos_da_lista = ''
# lista = []

# while produtos_da_lista != 'parar':
# print('Insira na lista o produto: ')
# produtos_da_lista = input()
# if produtos_da_lista != 'parar':
# lista.append(produtos_da_lista)
# print('\n')
# for produtos_da_lista in lista:
# print(produtos_da_lista)

#  Verificando se existe o elemento na lista
lista_de_cores = []
adicionar_cores = ''
verificar_cores = ''


# Adicionando cores em uma lista com laço de repetição
while adicionar_cores != 'parar':
    print('Insira as cores na lista.')
    adicionar_cores = input('')
    if verificar_cores != 'parar':
        lista_de_cores.append(adicionar_cores)
        print('Sua cor foi adicionada. \n')


# Verificando cores em uma lista com laço de repetição
while verificar_cores != 'sair':
    verificar_cores = input('Digite aqui o elemento que deseja verificar: ')
    if verificar_cores in lista_de_cores:
        print(f'Encontrei a cor {verificar_cores} na lista. \n')
    else:
        print(f'Não encontrei a {verificar_cores} na lista. \n')
    if verificar_cores == 'sair':
        print('Finalizando programa.....')

lista_de_numeros = []
inserir_numeros_na_lista = ''

# inserindo elementos em uma lista
while inserir_numeros_na_lista != 'parar':
    inserir_numeros_na_lista = input('Digite aqui o número que deseja inserir: ')
    if inserir_numeros_na_lista != 'parar':
        lista_de_numeros.append(inserir_numeros_na_lista)
        print('Número inserido.')
    if inserir_numeros_na_lista == 'parar':
        print(f'Aqui está a lista originalmente: {lista_de_numeros} \n')
        # Utilizando a função map para transformar lista de string em inteiros
        lista_de_numeros_inteiro = list(map(int, lista_de_numeros))
        lista_de_numeros_inteiro.sort()
        print(f'Aqui está a lista depois de ordernada e ser transformada em inteiro: {lista_de_numeros_inteiro}')


# adicionando produtos e valores
lista = []
produto = ''
valor_produto = float()
deseja_cadastrar_produto = ''
barra = '|'

while deseja_cadastrar_produto != 'sair':
    print('Castre o produto..')
    produto = input('Digite o nome do produto: ')
    valor_produto = float(input('Digite o valor do produto: '))
    if deseja_cadastrar_produto != 'sair':
        lista.append(produto)
        lista.append(valor_produto)
        print('Produto cadastrado.')
        deseja_cadastrar_produto = input('Deseja cadastrar outro produto ? ')
        if deseja_cadastrar_produto == 'sair':
            for produtos in lista:
                print(f'{produtos}', end=' ')

# Acrescentando números em listas:
insira_numero = int()
numeros = []

while insira_numero >= 0:
    insira_numero = int(input('Insira o número: '))
    if insira_numero >= 0:
        numeros.append(insira_numero)
        print('Número acrescententado')
    if insira_numero < 0:
        print('Valor inválido.')
        print('Programa encerrado.')
for n in numeros:
    print(n)


# Acrescentando produtos em um dicionário
carrinho = []
nome = ''
quantidade = int()
preco = float()
acrescentar_produtos = ''

lista = {
    'Nome': nome, 'Quantidade': quantidade, 'Preço': preco
}

while acrescentar_produtos != 'não':
    nome = input('Acrescente o nome do produto: ')
    quantidade = int(input('Acrescente a quantidade: '))
    preco = float(input('Acrescente o preco: '))
    acrescentar_produtos = input('Deseja cadastra mais produtos ?')
    if acrescentar_produtos != 'não':
        lista['Nome'] = nome  # Acrescentar a chave Nome a variável nome
        lista['Quantidade'] = quantidade # Acrescentar a chave Quantidade a variável quantidade
        lista['Preço'] = preco # Acrescentar a chave Preço a variável preco
        carrinho.append(lista) # Acrescentando os produtos ao carrinho
    if acrescentar_produtos == 'não':
        print(carrinho)


# Calculando valores em uma tupla
numero1 = int(input('Digite o número 1: '))
numero2 = int(input('Digite o número 2: '))
numero3 = int(input('Digite o número 3: '))
tuplas = (numero1, numero2, numero3)
tuplas2 = tuplas + (1, 18, 22)

print('A soma dos valores é: ',sum(tuplas2))
print('O menor valor é: ', min(tuplas2))
print('O maior valor é: ', max(tuplas2))
print(tuplas2)

# Acrescentando números em listas com extend
numero1 = int(input('Digite o número 1: '))
numero2 = int(input('Digite o número 2: '))
numero3 = int(input('Digite o número 3: '))
lista = []
lista.extend([numero1, numero2, numero3])
print(lista)

# Acrescentando palavras em listas com extend
curso1 = input('Digite o curso 1: ')
curso2 = input('Digite o curso 2: ')
curso3 = input('Digite o curso 3: ')
cursos = []
cursos.extend([curso1, curso2, curso3])
print(cursos)