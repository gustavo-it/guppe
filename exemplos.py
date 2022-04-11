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
