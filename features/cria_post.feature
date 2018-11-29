# language:pt
Funcionalidade:: Cria Post

Cenário: Novo post criado
    Dado que o usuário entra na página de criação de postagem
    Dado que o usuário preenche o título com "Teste com BDD"
    Dado que o usuário preenche o texto com "Olá mundo! ^^"
    Quando o usuário clica no botão "id_submit"
    Então o usuário visualiza a página "/post/1/"
    Então o usuário visualiza o conteúdo "Teste com BDD"
    Então o usuário visualiza o conteúdo "Olá mundo! ^^"

Cenário: Post com campos de dados em branco
    Dado que o usuário entra na página de criação de postagem
    Quando o usuário clica no botão "id_submit"
    Então o usuário visualiza a página "/post/new"
    Então o usuário não visualiza o conteúdo "Teste com BDD"
    Então o usuário não visualiza o conteúdo "Olá mundo! ^^"