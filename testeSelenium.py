from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()
chrome.get('http:/')

campo_busca = chrome.find_element_by_name('usuario')
campo_busca.send_keys('')

campo_busca = chrome.find_element_by_name('senha')
campo_busca.send_keys('')

#campo_busca.send_keys(Keys.ENTER) #esse aperta enter
botao = chrome.find_element_by_id('')
botao.click()


