import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


url = 'http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar'

option = Options()
option.headless = True
driver = webdriver.Firefox() 

driver.get(url)
time.sleep(10)
#CLICA NO ELEMENTO QUE FICA A ULTIMA VERSÃO
driver.find_element_by_xpath('//*[@id="sidebarleft"]/ul/li[1]/ul/li[1]').click()
#CLICA EM VISUALIZAR ANEXO
driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[3]/a').click()
time.sleep(10)
#CLICA NO ELEMENTO DOWNLOAD
driver.find_element_by_xpath('//*[@id="download"]').click()
time.sleep(15)
driver.find_element_by_xpath('//*[@id="download"]').click()
#O BROWSER JÁ ESTÁ CONFIGURADO PARA DOWNLOAD SEM MSGBOX DE CONFIRMAÇÃO, EMSEGUIDA ENCERRA A NAV.
driver.quit()
