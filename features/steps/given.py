from behave import given

@given ('que o usuário entra na página de criação de postagem')
def acessa_page(context):
    context.browser.visit(context.base_url+'/post/new')

@given ('que o usuário preenche o título com "{titulo}"')
def set_titulo(context, titulo):
    context.browser.fill('title', titulo)

@given ('que o usuário preenche o texto com "{texto}"')
def set_texto(context, texto):
    context.browser.fill('text', texto)
