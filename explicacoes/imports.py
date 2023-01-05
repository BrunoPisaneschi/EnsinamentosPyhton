"""
Para realizar imports no python, basta escrever:
`import <nome_lib>`

Caso queira importar apenas um módulo específico da lib, use:
`from <nome_lib> import <nome_modulo>`

É fortemente recomendado que use apenas o segundo caso.
O motivo disso é que voce torna mais leve o seu projeto e evita conflitos de informações que podem existir na lib e que você também pode ter criado localmente.abs

JAMAIS realizar o seguinte import:
from `<nome_lib>` import *

Esse caso acima parecido, mas um pouco pior que o primeiro, pois voce além de trazer todo o conteúdo da lib pra dentro do seu projeto, voce também `ativa` esse conteúdo, podendo gera muitos conflitos desnecessários.

Caso queira, renomear um import, pra facilitar seu uso dentro do projeto, usa-se o `as`.
Exemplo:
import numpy as np

Libs que não estão instaladas e/ou não são nativas do python, precisam ser instaladas préviamente com o comando `pip install`.

O site pypi.org é o maior e nativo repositório de libs do python. É possível alterar isso para algum privado de sua escolha, mas é um caso bem específico.
Dentro desse site, é possível pesquisar a lib e encontrar o comando para instalar e até mesmo alguns passos de como utilizá-la.
"""
from json import dumps, loads
