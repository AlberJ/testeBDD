from behave import then

@then('o usuário visualiza a página "{page}"')
def verifica_pagina (context,page):
    post = context.base_url + page
    assert context.browser.url == post

@then ('o usuário visualiza o conteúdo "{txt}"')
def ver_texto (context,txt):
    assert context.browser.is_text_present(txt)