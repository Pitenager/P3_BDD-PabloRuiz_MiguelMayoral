# -*- coding: utf-8 -*-

import unittest
from urllib.error import URLError
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class TestTextAnalyzer(unittest.TestCase):

    def test_analyze_text_one_word(self):
        browser = webdriver.Firefox()
        browser.get("http://localhost:8000/index/")
        campoTexto = browser.find_element_by_id("id_my_text")
        campoTexto.send_keys("Hola")
        botonEnviar = browser.find_element_by_id("analyze")
        botonEnviar.click()
        resultado = browser.find_element_by_id("resultado").text
        assert 'hola' and '1' in resultado
        browser.close()

    def test_analyze_text_two_different_words(self):
        browser = webdriver.Firefox()
        browser.get("http://localhost:8000/index/")
        campoTexto = browser.find_element_by_id("id_my_text")
        campoTexto.send_keys("Hola adios")
        botonEnviar = browser.find_element_by_id("analyze")
        botonEnviar.click()
        resultado = browser.find_element_by_id("resultado").text
        assert 'hola' and '1' and 'adios' and '1' in resultado
        browser.close()

    def test_analyze_text_two_same_words(self):
        browser = webdriver.Firefox()
        browser.get("http://localhost:8000/index/")
        campoTexto = browser.find_element_by_id("id_my_text")
        campoTexto.send_keys("Hola hoLa")
        botonEnviar = browser.find_element_by_id("analyze")
        botonEnviar.click()
        resultado = browser.find_element_by_id("resultado").text
        assert 'hola' and '2' in resultado
        browser.close()

    def test_write_more_than_hundred_characters(self):
        browser = webdriver.Firefox()
        browser.get("http://localhost:8000/index/")
        campoTexto = browser.find_element_by_id("id_my_text")
        texto100Caracteres = "01234567890123456789012345678901234567890123456789012345678901234567890123456789012345" \
                             "67890123456789"
        textoMas100Caracteres = "012345678901234567890123456789012345678901234567890123456789012345678901234567890123" \
                                "456789012345678901234567890123456789"
        campoTexto.send_keys(textoMas100Caracteres)
        textoEscrito = campoTexto.get_attribute('value')
        assert textoEscrito == texto100Caracteres
        browser.close()

    def test_reset_textfield_with_reset_button(self):
        browser = webdriver.Firefox()
        browser.get("http://localhost:8000/index/")
        campoTexto = browser.find_element_by_id("id_my_text")
        campoTexto.send_keys("Texto de prueba")
        botonBorrar = browser.find_element_by_id("reset")
        botonBorrar.click()
        textoEscrito = campoTexto.get_attribute('value')
        assert textoEscrito == ""
        browser.close()

    def test_reset_textfield_with_analyze_button(self):
        browser = webdriver.Firefox()
        browser.get("http://localhost:8000/index/")
        campoTexto = browser.find_element_by_id("id_my_text")
        campoTexto.send_keys("Texto de prueba")
        botonBorrar = browser.find_element_by_id("analyze")
        botonBorrar.click()
        campoTexto = WebDriverWait(browser, 20).until(lambda browser: browser.find_element_by_id("id_my_text"))
        textoEscrito = campoTexto.get_attribute('value')
        assert textoEscrito == ""
        browser.close()

    def test_click_execute_button_without_text(self):
        browser = webdriver.Firefox()
        browser.get("http://localhost:8000/index/")
        botonExecute = browser.find_element_by_id("analyze")
        botonExecute.click()
        campoTexto = browser.find_element_by_id("id_my_text")
        textoEscrito = campoTexto.get_attribute('value')
        assert textoEscrito == ""
        browser.close()

if __name__ == '__main__':
    unittest.main()
