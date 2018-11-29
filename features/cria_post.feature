# language:pt
Funcionalidade:: Cria Post

Cenário:Cenário: Novo post será criado
    Dado que o usuário entra na página de criação de postagem
    Dado que o usuário preenche o título
    Dado que o usuário preenche o texto
    Quando o usuário clica no botão save
    Então o usuário visualiza a página de detalhes da postagem
    Então o usuário visualiza o título
    Então o usuário visualiza o texto
