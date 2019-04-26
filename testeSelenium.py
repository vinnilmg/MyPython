from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()
chrome.get('http://saude.sulamerica.br/ressarcimentosus/public/login.jsf')

campo_busca = chrome.find_element_by_name('usuario')
campo_busca.send_keys('susis')

campo_busca = chrome.find_element_by_name('senha')
campo_busca.send_keys('sas155')

#campo_busca.send_keys(Keys.ENTER) #esse aperta enter
botao = chrome.find_element_by_id('loginBtn')
botao.click()


