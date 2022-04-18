"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta perfomance.

"""
# import
from collections import deque
deq = deque('Docker')

print(deq)

# Adicionando elementos no deque

deq.append('z')  # Adiciona no final
print(deq)

deq.appendleft('k')  # Adiciona no começo da lista
print(deq)

# Remover elementos
print(deq.pop())  # Retorna o último elemento (além de remover)
print(deq)

print(deq.popleft())  # Retorna o primeiro elemento (além de remover)
print(deq)
