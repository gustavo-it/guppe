lista = ['Maria', 'Barbosa', 22, 1.58, 'Andressa', 'Ramirez', 18, 1.58, 'Fernanda', 'Maria', 19, 1.62]
n = 4


saida = [lista[i:i + n] for i in range(0, len(lista), n)]
print(saida)
