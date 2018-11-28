from splinter import Browser

def before_all(context):
    context.browser = Browser(executable_path='/home/ifpb/django/geckodriver')
    context.server_url = 'http://localhost:8000'

def after_all(context):
    context.browser.quit()
