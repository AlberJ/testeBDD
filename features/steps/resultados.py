from behave import then

# br = context.browser
# body = br.find_by_css('body')

# @then('o usuário visualiza a página de detalhes da postagem')

@then("o usuário visualiza o título")
def ver_titulo (context):
    br = context.browser
    body = br.find_by_css('body')    
    assert 'Teste com BDD' in body.text

@then ('o usuário visualiza o texto')
def ver_texto (context):
    br = context.browser
    body = br.find_by_css('body')
    assert 'Olá mundo! ^^' in body.text