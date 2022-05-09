"""
Geradores

- Geradores (Generators) são Iterators (Iteradores);

OBS: O contrário não é verdadeiro, ou seja, nem todo iterator é um generator.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions

---------------------------------------------------------------------------------------
| Funções                                     | Generator Functions                   |
---------------------------------------------------------------------------------------
| Utilizam return                             | Utilizam yield                        |
---------------------------------------------------------------------------------------
| Retorna uma vez                             | podem utilizar yield N vezes          |
---------------------------------------------------------------------------------------
| quando executada, retorna um valor          | quando executada, retorna um generator|
---------------------------------------------------------------------------------------
"""
# Exemplo Generator Function


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


gen = conta_ate(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# OBS: Uma Generator Function não é um Generator, ela gera um generator, ok?
