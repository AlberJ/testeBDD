from behave import when

@when('o usuário clica no botão "{btn}"')
def click (context, btn):
    context.browser.find_by_id(str(btn)).click()