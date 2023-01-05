"""
Laços de repetições no python, basicamente, sempre serão um foreach.

Existem algumas formas de fazer um laço, sendo elas:

- Básico;
- Intermediário;
- Avançado;

Os níveis acima, são de complexidade de escrita e leitura humana, mas não necessáriamente, representam a complexidade e leitura da máquina.

Demonstrarei os três níveis com o mesmo loop, percorrendo uma lista de 10 itens.
"""

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] # essa mesma lista, também poderia ter sido gerada da seguinte maneira: range(10)

# Básico - Laço de repetição comum - Não retorna nada
for numero in lista_numeros:
  print(numero)

# Intermediário - List Comprehension - Retorna uma lista
[print(numero) for numero in lista_numeros]

# Avançado - Map/Lambda - Retorna uma lista
list(map(lambda numero: print(numero), lista_numeros))

"""
Em termos de performânce, o laço de repetição básico, será o mais lento e os outros dois dependerá do que for fazer.
"""
