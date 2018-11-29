from behave import given

# br = context.browser

@given ('que o usuário entra na página de criação de postagem')
def acessa_page(context):
    br = context.browser
    br.visit(context.base_url+'/post/new')

@given ('que o usuário preenche o título')
def set_titulo(context):
    br = context.browser
    br.fill('title', 'Teste com BDD')

@given ('que o usuário preenche o texto')
def set_titulo(context):
    br = context.browser
    br.fill('text', 'Olá mundo! ^^')
    br.find_by_id('id_submit').first.click()
