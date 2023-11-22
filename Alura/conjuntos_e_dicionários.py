# -*- coding: utf-8 -*-
"""Conjuntos e dicionários.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VrSCDLxvf9ZroCVcf_pGq8sgYvuwNwK8
"""

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
assistiram

len(assistiram)

set(
    assistiram
)  # conjunto no Python é representado aqui por vários elementos, que não possuem elementos repetidos (sets)

set([1, 2, 3, 1])

{4, 1, 2, 3, 1}  # notação para criar um conjunto simples é a chaves

for usuario in set(assistiram):
    print(usuario)

usuarios_data_science = {
    15,
    23,
    43,
    56,
}  # tenta acessar aleatoriamente um conjunto, você não possui indexação. Um acesso aleatório à uma posição, porque o que eu falei: não existe posição, contrário à lista
usuarios_machine_learning = {13, 23, 56, 42}

usuarios_data_science | usuarios_machine_learning  # forma de juntar dois conjuntos, operação de "ou", união dos 2 conjuntos

(
    usuarios_data_science & usuarios_machine_learning
)  # Então eu quero quem fez o primeiro curso e o segundo curso, então é a operação de “e”

(
    usuarios_data_science - usuarios_machine_learning
)  # Eu quero mandar para quem enviou, para quem fez o Data Science menos quem já fez o Machine Learning

(
    usuarios_data_science ^ usuarios_machine_learning
)  # Então fez isso ou isso, mas não pode ter feito os dois ao mesmo tempo. Esse é o "ou" exclusivo

usuarios = {1, 5, 76, 34, 52, 13, 17}
len(usuarios)

usuarios.add(
    13
)  # adiciona no conjunto, mas nesse caso não add pq o 13 já tava lá /  Um conjunto, por padrão, em Python, ele é mutável. Podemos adicionar, remover, alterar, pode alterar conteúdos de dentro desse conjunto.
len(usuarios)

usuarios.add(765)
len(usuarios)

usuarios = frozenset(
    usuarios
)  # conjunto imutável, congelado, não dá pra add nada lá dentro
usuarios

type(usuarios)

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"

set(
    meu_texto.split()
)  # transformei o texto em um conjunto de palavras, ele tirou as palavras repetidas tb

"""Dicionário (Mapa): Então um dicionário é uma situação clássica, uma agenda telefônica também, procuro o nome, traz o telefone, procura o nome, traz o e-mail, podia ser uma agenda de e-mails. é comum fazermos esse tipo de mapa, que chamamos aqui de chave-valor, então o mapa, ele indica o caminho dessa chave para esse valor."""

aparicoes = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1,
}  # isso é um dicionário, conjunto de chave e valor

type(aparicoes)

aparicoes["Guilherme"]

aparicoes["cachorro"]

aparicoes["xpto"]  # dá erro pq não tá no dicionário

aparicoes = dict(
    Guilherme=2, cachorro=1
)  # instanciar pelo construtor dict(). Quando criamos pelo construtor dict(), usamos uma outra forma, que é a chave, por exemplo (Guilherme = 2, cachorro = 1)
aparicoes

aparicoes["Carlos"] = 1

aparicoes

aparicoes["Carlos"] = 2

aparicoes

del aparicoes["Carlos"]

aparicoes

"cachorro" in aparicoes  # Perguntar se um elemento está dentro de um dicionário é perguntar se a chave está lá dentro.

"Carlos" in aparicoes

for (
    elemento
) in (
    aparicoes
):  # Então o aparicoes é um iterável, e esse iterável retorna o quê? As chaves e não os valores, que é condizente com o in, certo?
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

1 in aparicoes.values()

for (
    elemento
) in (
    aparicoes.keys()
):  # uma das maneiras é passarmos pela lista da esquerda, das chaves. Outra maneira, pela lista da direita, dos valores. Agora eu queria passar linha a linha, meio que linha a linh
    print(elemento, aparicoes[elemento])

for (
    elemento
) in (
    aparicoes.items()
):  # Então ao invés de eu passar pelas chaves, eu passo pelos items(). Então um item é uma dupla, pensa que um item é uma dupla.
    print(
        elemento
    )  # linha, cada item, é uma tupla de tamanho 2. Por que escolheram tupla e não lista? Bom, não queremos mudar, porque não quero colocar um terceiro elemento ali, eu tenho exatamente dois, o primeiro elemento representa sempre a chave, o segundo elemento representa sempre o valor. Então é tudo a ver com tupla e não com lista, por isso que são tuplas aqui

for (
    chave,
    valor,
) in (
    aparicoes.items()
):  # E se são tuplas aqui, é o mesmo que fosse lista, podemos desempacotar de uma vez só
    print(chave, "=", valor)

["palavra {}".format(chave) for chave in aparicoes.keys()]

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto.lower()
meu_texto = meu_texto.lower()
aparicoes = {}  # como contar aparicoes de palavras em um texto
for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

aparicoes

from collections import (
    defaultdict,
)  # dicionário com valor padrão (ficou meio confuso ainda)

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

aparicoes

dicionario = defaultdict(int)
dicionario["guilherme"]

dicionario["guilherme"] = 15
dicionario["guilherme"]

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    aparicoes[
        palavra
    ] += 1  # erar o nosso contador de aparições de palavras em um texto.

aparicoes


class Conta:
    def __init__(self):
        print("Criando uma conta")


contas = defaultdict(
    Conta
)  # olha, esse dicionário referenciado pela variável contas, toda vez que eu buscar alguma conta que não está lá ainda, vai chamar essa função aqui, que é o nosso construtor, e criar uma conta nova
contas[15]

from collections import Counter

aparicoes = Counter()  # contador por padrão tem valor 0
for palavra in meu_texto.split():
    aparicoes[palavra] += 1

aparicoes

aparicoes = Counter(
    meu_texto.split()
)  # Então eu já vou passar um iterável para esse contador: vou criar um contador e aqui no contador eu já passo meu_texto.split() que é um iterável. Adivinha o que ele vai fazer? Contar. É um contador. Então ficou uma linha de código

aparicoes

"""Testando uso das coleções

"""

texto1 = """
Para começar a fazer vendas online, uma empresa que fabrica adesivos criou uma página para pré cadastro de cartão de crédito que contém campos como nome, idade, endereço, CPF entre outros.

O problema é que alguns cadastros não possuem um formato de CPF válido, isso porque o campo não possui nenhuma validação. Ou seja, o campo está aceitando não só números como letras e outros tipos de caractere.

O que vamos fazer é encontrar uma maneira de ajudar o usuário de forma mais clara possível a preencher o cadastro e garantir a validação no front-end antes que os dados sejam enviados para o back-end.
Como podemos notar não temos nenhuma validação, então fica confuso se devemos ou não colocar ponto ou traço no CPF e pode acontecer do usuário colocar outros caracteres no campo sem querer.

Para isso evitar que isso ocorra vamos usar o atributo pattern do HTML5 que nos permite fazer uso das famosas expressões regulares que nada mais são que padrões utilizados para selecionar caracteres em uma string.

Na nossa verificação vamos usar a lista [0-9], esse padrão indica que queremos os números de 0 até 9 e o intervalo {11}, indicando que temos que ter um número de 11 dígitos no nosso campo.

Com a adição do pattern nosso campo de CPF ficou da seguinte maneira:
Com a ajuda do pattern e das expressões regulares conseguimos resolver uma parte da tarefa, agora o que precisamos fazer encontrar uma maneira de formatar o CPF no padrão que precisamos enviar ao back-end.
Mais um pouco de Regex

Para começar vamos criar uma função que vai ser responsável por formatar o CPF. Dentro dessa função vamos ter as variáveis :

    elementoAlvo: responsável pelo parâmetro que vai ser passado na função
    cpfAtual: responsável por capturar os números do CPF digitados
    cpfAtualizado: responsável por receber o CPF formatado.
"""

texto2 = """
    Vamos imaginar uma empresa como o Nubank, seu nome é ByteBank. A primeira vista ela vende cartões de crédito e possui uma estratégia de marketing de conteúdo para seus clientes (Business to Consumer, B2C).

Agora ela está lançando um novo cartão focado em empresas e quer criar uma estratégia de marketing de conteúdo para outras empresas (business to business, B2B).

Como eles podem criar essa estratégia? É possível utilizar ideias e ferramentas do marketing de conteúdo B2C para o B2B?

No marketing de conteúdo criado para B2C da ByteBank é muito enfatizado que as principais vantagens da empresa são:

    saber o limite na hora;
    não pagar qualquer tarifa e
    não ter que lidar com burocracia na hora de fazer o cartão.

Então, todo o plano é focado em criar conteúdos sobre questões relacionadas ao mundo financeiro, para mostrar que a empresa é especialista no assunto, transmitindo uma confiança aos clientes.

A equipe de marketing escreveu um texto no qual foram explicadas todas as taxas do cartão de crédito. Depois de explicar com detalhes o que é cada taxa, foi mostrado o porquê do cartão dessa empresa não cobrar nenhuma delas.

Para mostrar na prática o quanto o consumidor economizaria, eles deram como um exemplo que mostram o que pode ser comprado com o dinheiro economizado em tarifas do cartão. Veja como ficou o texto:
Será que se pode fazer a mesma coisa para o B2B, já que não existem tarifas para empresas também?

As empresas que querem comprar um produto precisam avaliar muito bem toda a compra, sempre se perguntando se aquele produto realmente compensa para ela, principalmente a longo prazo.

Então, e se fosse dito coisas que a empresa poderia fazer com o dinheiro que também vão trazer um retorno financeiro, ao contrário das taxas dos bancos? Como fazer pesquisas com usuários, desenvolver novos produtos, treinar pessoas para marketing, entre outras coisas?

Pensando nessas diferenças, utilizamos o mesmo exemplo: quanto seria economizado por ano pela empresa cliente. Porém, no texto inteiro, queremos também mostrar dicas de como ela pode poupar, de diversas maneiras, mesmo usando um cartão de crédito. Então, o exemplo de economia no texto ficou assim:
Foi usada uma linguagem mais formal do que a B2C porque quando estamos lidando com empresas temos que ser mais práticos e mostrar exatamente o que a empresa ganha, e, no caso, até como poderia ganhar mais depois.

Além dessa mudança na linguagem, tivemos ideias diferentes de conteúdo. No B2C foram apresentados conhecimentos a respeito de cada taxa, para que a pessoa entenda o que está pagando e confie em empresas que não cobra as taxas.

Agora para B2B foram apresentadas formas para economizar no cartão, pois, muitas vezes, os empresários sabem o que é cada taxa do cartão e tem que utilizá-lo mesmo assim. Então, mostramos como ele pode economizar e, uma dessas formas, é usar o cartão da ByteBank.

Nesse mesmo texto para B2B também acrescentamos o conteúdo de outra vantagem do cartão: poder determinar um limite de gastos para cada categoria nos cartões dos funcionários da empresa.

Dessa forma, os funcionários não podem gastar mais do que o determinado e, assim, a empresa consegue economizar e planejar os gastos e não extrapolar com compras dos funcionários.

O foco da comunicação B2B que utilizamos foi dar dicas para não cometer erros e economizar mais, para que a empresa perceba que utilizar o cartão é vantagem.

E caso a sua empresa seja diferente da ByteBank, seja só B2B e não tenha nenhum plano de comunicação focado para B2C para se basear?

Existem diversas empresas B2B:

    as que vendem tanto para B2B quanto para B2C, como a ByteBank;
    as que vendem para ambos os consumidores, mas possuem um foco maior no B2B, como a Marmotex, que tem como serviço entrega de marmitas e entregam tanto para consumidores quanto empresas, mas possuem um foco maior em organizações e catering para eventos, ou seja, B2B
    as empresas somente B2B, como as de agências de publicidade.

Cada uma das empresas que são B2B possui um produto e um serviço para mostrar.

Então, caso você trabalhe em uma empresa que não possui um plano de marketing de conteúdo para B2C para se basear, é só seguir a ideia do marketing de conteúdo, de passar informações relacionados a sua empresa, tornando-a uma autoridade no assunto. E, além disso, mostrar maneiras que o seu produto e/ou serviço pode ajudar a empresa em determinado tema.

No B2B, como no marketing de conteúdo focado no B2C, é importante frisar a importância e a relevância do produto e/ou serviço para o cliente. E, melhor, a longo prazo.

A empresa cliente precisa entender e saber que a vantagem trazida pelo produto será duradoura. Pois o processo de compra B2B é mais longo justamente porque há muito em jogo e muitas pessoas envolvidas.

Mudar de produto ou serviço é trabalhoso e pode causar prejuízo para a empresa, assim, eles buscam e precisam de garantias de que a solução funcionará por muito tempo.

Assim, como no marketing B2C, os tipos de conteúdo devem se atentar aos clientes em cada fase do funil de marketing de conteúdo para trazer o conteúdo certo para a empresa em cada momento da obtenção do cartão.

Para isso, a Bytebank utilizou dados, números, infográficos e mostrou com exemplos práticos maneiras de ajudar a contratante. Também escreveu conteúdos com histórias de empresas - os chamados cases de sucesso - que obtiveram lucro ou sucesso com o produto/serviço.

Além disso, apresentou novidades e dicas tanto da sua empresa, que passou a fornecer uma conta para pessoas físicas e jurídicas, quanto do segmento dela, com informações que podem ser úteis ao cliente do setor financeiro.

Como vimos, as principais diferenças entre os conteúdos B2C para o B2B são a linguagem, que deve ser mais formal se for B2B e apelar para o emocional se for B2C.

No B2B você estará lidando com pessoas que tomam decisões nas empresas, então deverá mostrar como o produto pode ajudar a empresa, de preferência a longo prazo.

Fora isso, o tipo de conteúdo pode ser o mesmo do marketing de conteúdo B2C. Passando desde textos sobre novidades, inovações e dicas na área, até infográficos com dados de pesquisas, vídeos, áudios de podcast, imagens e publicações nas redes sociais.

Também, para conteúdo B2B, é muito comum encontrar whitepapers, grupos de usuários, meetups, cases de sucesso, trial gratuito, e até mesmo vídeos ou campanhas e posts de marketing com influenciadores.

Agora, se você quiser saber mais sobre marketing de conteúdo, 

"""

Counter(texto1.lower())

aparicoes = Counter(texto1.lower())
total_de_caracteres = sum(aparicoes.values())
print(total_de_caracteres)

for (
    letra,
    frequencia,
) in (
    aparicoes.items()
):  # Eu quero pegar a letra, por exemplo a letra "A", e falar: a letra "A" apareceu 182 vezes. Se ela apareceu 182 de 1821, isso significa 10%, que é 0.1. 10% das aparições nesse texto1 são da letra "A"
    tupla = (letra, frequencia / total_de_caracteres)
    print(tupla)

proporcoes = [
    (letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()
]  # transformou tupla em lista, depois a lista em dicionário
proporcoes = Counter(
    dict(proporcoes)
)  # no dicionário colocou um contador pq o contador tem a propriedade most_common, pra achar as letras + frequentes no texto
proporcoes.most_common(10)  # achei os 10 mais comuns


def analisa_frequencia_de_letras(
    texto,
):  # cria uma função pra analisar as letras mais comuns no texto, usando como base o código anterior.
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [
        (letra, frequencia / total_de_caracteres)
        for letra, frequencia in aparicoes.items()
    ]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print((caractere, proporcao))


analisa_frequencia_de_letras(texto1)


def analisa_frequencia_de_letras(
    texto,
):  # funcão pra analisar frequencia das letras melhorada, com valores em porcentagem
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [
        (letra, frequencia / total_de_caracteres)
        for letra, frequencia in aparicoes.items()
    ]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))


analisa_frequencia_de_letras(texto1)

analisa_frequencia_de_letras(texto2)
