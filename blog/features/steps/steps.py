from behave import given, then

@given("que preenche o 'titulo' com 'Meu primeiro Post'")
def set_title (context, titulo):
    pass


@then("preenche o 'texto' com 'Olá mundo! ^^'")
def set_text (context, texto):
    pass