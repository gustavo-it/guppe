"""
Levantando os próprios erros com raise

raise _> Lança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra
em Python.

Para simplificar, pense no raise como sendo útil para criar as nossas próprias
exceções e mensagens de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')

OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.
"""
# Exemplo real


def colore(texto, cor):
    cores = ('Azul', 'Branco', 'Verde', 'Amarelo')
    if type(texto) is not str:  # Se não é uma 'string'
        raise TypeError('Texto precisa ser uma string.')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string.')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Docker', 'Azul')
