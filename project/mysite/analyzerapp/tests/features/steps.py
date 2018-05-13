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

@after.all
def after_all():
    world.browser.close()

@step(r'I write text in the textarea')
def write_in_textarea_to_reset(self):

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
    #world.browser.close()

@step (r'I write chamber token chamber in the textarea')
def write_in_textarea_to_analyze_repeated_word(self):
    campoTexto = world.browser.find_element_by_id("id_my_text")
    campoTexto.send_keys("chamber token chamber")

@step (r'I click the execute button')
def click_the_reset_button(self):
    botonBorrar = world.browser.find_element_by_id("analyze")
    botonBorrar.click()

@step (r'I should see the results:')
def click_the_reset_button(self):
    resultado = world.browser.find_element_by_id("resultado").text
    assert 'chamber' and '2' and 'token' and '1' in resultado
    #world.browser.close()

@step (r'I write in the textarea more than 100 characters')
def write_more_than_hundred_characters (self):
    campoTexto = world.browser.find_element_by_id("id_my_text")
    textoMas100Caracteres = "012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"
    campoTexto.send_keys(textoMas100Caracteres)

@step (r'I should see only the first 100')
def see_the_first_hundred(self):
    texto100Caracteres = "0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"
    campoTexto = world.browser.find_element_by_id("id_my_text")
    textoEscrito = campoTexto.get_attribute('value')
    assert textoEscrito == texto100Caracteres
    #world.browser.close()

@step (r'I write in the textarea')
def write_random_text(self):
    campoTexto = world.browser.find_element_by_id("id_my_text")
    campoTexto.send_keys("Texto de prueba")

@step (r'I click the execute button')
def click_the_reset_button(self):
    botonExecute = world.browser.find_element_by_id("analyze")
    botonExecute.click()


@step (r'The textarea looks empty')
def see_textarea_empty(self):
    campoTexto = WebDriverWait(world.browser, 20).until(lambda browser: world.browser.find_element_by_id("id_my_text"))
    textoEscrito = campoTexto.get_attribute('value')
    assert textoEscrito == ""
    #world.browser.close()

@step (r'The textarea is empty')
def empty_textarea (self):
    campoTexto = world.browser.find_element_by_id("id_my_text")
    textoEscrito = campoTexto.get_attribute('value')
    assert textoEscrito == ""

@step (r'I click the execute button')
def click_execute_button(self):
    botonExecute = world.browser.find_element_by_id("analyze")
    botonExecute.click()

@step(r'There is no result')
def empty_result(self):
    campoTexto = world.browser.find_element_by_id("id_my_text")
    textoEscrito = campoTexto.get_attribute('value')
    assert textoEscrito == ""
    #world.browser.close()

@step (r'I have the textarea empty')
def text_area_empty(self):
    campoTexto = world.browser.find_element_by_id("id_my_text")
    textoEscrito = campoTexto.get_attribute('value')
    assert textoEscrito == ""

@step (r'I click the reset button')
def click_reset_button (self):
    botonExecute = world.browser.find_element_by_id("reset")
    botonExecute.click()


@step (r'The textarea continues empty')
def text_area_continues_empty(self):
    campoTexto = world.browser.find_element_by_id("id_my_text")
    textoEscrito = campoTexto.get_attribute('value')
    assert textoEscrito == ""