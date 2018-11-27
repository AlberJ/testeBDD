# language:pt
Funcionalidade:: Cria Post

Cenário: Novo post será criado
    Dado que preenche o 'titulo' com 'Meu primeiro Post'
    E preenche o 'texto' com 'Olá mundo! ^^'
    E clica em salvar
    Então o Post é criado mostrando o o titulo 'Meu primeiro Post' e o texto 'Olá mundo! ^^' 