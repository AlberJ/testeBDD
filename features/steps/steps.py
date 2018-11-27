from behave import given, when, then
from blog.tests import TestePost
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def setUp(self):
    self.selenium = webdriver.Firefox(executable_path='/home/alber/django/geckodriver')
    super(TestePost, self).setUp()

def tearDown(self):
    self.selenium.quit()
    super(TestePost, self).tearDown()

# Dado
@given("Acessa a página de criar posts")
def go_pagina (context):
    context.browser.get('http://localhost:8000/post/new')

# Quando
@when ('Prenche o titulo')
def set_titulo(context):
    titulo = context.find_element_by_id('id_title')
    titulo.send_keys("Teste com BDD")

# Quando
@when ('Prenche o texto')
def set_texto(context):
    textarea = context.find_element_by_id('id_text')
    textarea.send_keys("Olá mundo! ^^")

# Quando
@when ('Clica em salvar')
def clica_salvar(context):
    submit = context.find_element_by_id('id_submit')

# Então
@then("Vejo o titulo a postagem")
def avalia_resultado (context):
    assert 'Teste com BDD' in context.page_source