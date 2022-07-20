_**For the English version of this file [click here](README.md).**_

# GlouphrieTranslator

**GlouphrieTranslator** (ou **GT**) é uma intregração do **MWParserFromHell** e **PyWikiBot** em Python. Essa ferramente permite editores da **PT-BR Runescape Wiki** aumentar a velocidade tradução das páginas em inglês da **RSW** (Runescape Wiki). O foco de tal ferramenta é entregar ao utilizador a versão traduzida de predefinições.

## Instalação

1. Antes de instalar a ferramenta, você precisa instalar as seguintes dependências:

- [Pywikibot](https://github.com/wikimedia/pywikibot);
- [MWParserFromHell](https://github.com/earwig/mwparserfromhell); e
- [requests](https://github.com/psf/requests).

2. Instale [git](https://git-scm.com/) para ser capaz de prosseguir com a instalação.

3. Vá para o diretório de instalação do seu Python e encontre as pasta `Lib/site-packages`, para então abrir a pasta `pywikibot`. Dentro da pasta `pywikibot` procure e abra a pasta `families` e adicione o arquivo `rsw_family.py` a ele (este arquivo pode ser encontrado em [pywikibot_family](pywikibot_family)).

4. Finalmente, você pode instalar a ferramenta executando o seguinte comando:

```pip install git+https://github.com/Toktom/GlouphrieTranslator```.

## Funções

A ferramenta tem as seguintes funções:

- Extração da predefinição Infobox Objeto da página que não utiliza os parâmetros de versão (por exemplo: versão1 e versão2 que resultam em nome1 e nome2);

## Exemplos

A pasta [examples](examples) contém alguns exemplos de como utilizar a ferramenta. Atualmente, existe apenas um exemplo: voltado para extrair a predefinição Infobox Objeto de uma página de Objeto.

## Para fazer

- Adicionar suporte para mais predefinições de infoboxes;
- Adicionar suporte para predefinições de caixas de navegação;
- Adicionar documentação para funções;
- Adicionar verificação automática de instalação;
- Adicionar suporte para os parâmetros de versão;
- Adicionar logging;
- Acelerar o desenvolvimento (remover loops quando possível); e
- Melhorar a utilização de try/except em funções e classes.
