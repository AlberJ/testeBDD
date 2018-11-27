from behave import given

# Dado
@given ('Cria a postagem')
def set_titulo(context):
    br = context.browser
    br.visit(context.base_url+'/post/new')
    br.fill('title', 'Teste com BDD')
    br.fill('text', 'Olá mundo! ^^' )
    br.find_by_id('id_submit').first.click()

    # br = context.browser
    # br.visit(context.base_url + '/admin/')
    # br.fill('username', 'test')
    # br.fill('password', 'test')
    # br.find_by_css('.submit-row input').first.click()
