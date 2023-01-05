"""
`Python é uma linguagem de programação de tipagem dinâmica.`

A frase acima, significa que diferente de outras linguagens, você não precisa avisar o python sobre qual é o tipo da variável que você criou.

A tipagem no python serve mais como guia para desenvolvedores que forem ler, do que como algum tipo de validação do código.

Único ou um dos poucos cenários onde a tipagem é obrigatória, é na criação de schemas.
Essa informação é um pouco mais avançada, confira no conteúdo de API mais informações sobre.
"""

# Tipos primitivos em python
# str, int, float, list, dict

variavel_string = "texto" # contém um valor string
variavel_string = 1234 # a mesma variável, agora contém um valor tipo integer
variavel_float = 123.45

variavel_lista = []

# para incluir valores na lista, usa-se o append
variavel_lista.append(123456)


variavel_dicionario = {}

# dicionário tem mais peculiaridades
# usa-se o update para incluir e alterar valores de uma chave dentro do dicionário,
# caso ela não exista, será criada.
# Também pode ser passado várias chaves ao mesmo tempo para o update
variavel_dicionario.update({"chave": 8904}) 