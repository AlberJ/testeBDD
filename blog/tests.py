from django.test import TestCase, Client, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestePost(LiveServerTestCase):
    
    def setUp(self):
        self.selenium = webdriver.Firefox(executable_path='/home/alber/django/geckodriver')
        super(TestePost, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(TestePost, self).tearDown()


    def test_cadastro_post(self):
        selenium = self.selenium

        selenium.get('http://localhost:8000/post/new')

        titulo = selenium.find_element_by_id('id_title')
        textarea = selenium.find_element_by_id('id_text')
        submit = selenium.find_element_by_id('id_submit')

        titulo.send_keys("Teste do selenium")
        textarea.send_keys("Deu certo?!")
        submit.click()

        assert 'Teste do selenium' in selenium.page_source