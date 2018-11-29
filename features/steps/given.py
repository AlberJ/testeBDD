from behave import given

@given ('que o usuário entra na página de criação de postagem')
def acessa_page(context):
    context.browser.visit(context.base_url+'/post/new')

@given ('que o usuário preenche o título')
def set_titulo(context):
    context.browser.fill('title', 'Teste com BDD')

@given ('que o usuário preenche o texto')
def set_titulo(context):
    context.browser.fill('text', 'Olá mundo! ^^')
