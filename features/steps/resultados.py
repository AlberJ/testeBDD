from behave import then

@then('o usuário visualiza a página de detalhes da postagem')
def verifica_pagina (context):
    post = context.base_url+'/post/1/'
    assert context.browser.url == post

@then("o usuário visualiza o título")
def ver_titulo (context):
    assert context.browser.is_text_present('Teste com BDD')

@then ('o usuário visualiza o texto')
def ver_texto (context):
    assert context.browser.is_text_present('Olá mundo! ^^')