from behave import when

@when('o usuário clica no botão save')
def submit (context):
    context.browser.find_by_id('id_submit').first.click()