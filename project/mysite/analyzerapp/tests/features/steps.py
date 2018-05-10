from aloe import *
from selenium import webdriver
from aloe import before, step, world
from aloe.tools import guess_types
from aloe_django.steps.models import get_model
from nose.tools import assert_true
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from nose.tools import assert_equals
from project.mysite.mysite import *
import os

@before.all
def before_all():
    world.browser = webdriver.Firefox()
    world.browser.get("http://localhost:8000/index/")

@step(r'I write text in the textarea')
def write_in_textarea(self):

    campoTexto = world.browser.find_element_by_id("id_my_text")
    campoTexto.send_keys("Texto de prueba")

@step (r'I click the reset button')
def click_the_reset_button(self):
    botonBorrar = world.browser.find_element_by_id("reset")
    botonBorrar.click()


@step (r'I should see the textarea empty')
def see_textarea_empty(self):
    campoTexto = world.browser.find_element_by_id("id_my_text")
    textoEscrito = campoTexto.get_attribute('value')
    assert textoEscrito == ""