from behave import given

@given ('Cria a postagem')
def set_titulo(context):
    br = context.browser
    br.visit(context.base_url+'/post/new')
    br.fill('title', 'Teste com BDD')
    br.fill('text', 'Olá mundo! ^^' )
    br.find_by_id('id_submit').first.click()
