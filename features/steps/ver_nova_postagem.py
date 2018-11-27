from behave import then

@then("Visualiza a postagem")
def avalia_resultado (context):
    br = context.browser
    body = br.find_by_css('body')
    assert 'Teste com BDD' in body.text
