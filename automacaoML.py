from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date
import os, openpyxl, time

class automation:
    def __init__(self):
        drive_options = Options()

        arguments = ['--lang=pt-BR', '--window-size=800,800',
                     '--disable-notifications']
        for argument in arguments:
            drive_options.add_argument(argument)

        chromeDriver = os.getcwd() + os.sep + 'chromedriver.exe'
        s = Service(chromeDriver)

        self.driver = webdriver.Chrome(service = s, options = drive_options)

    def Iniciar(self):
        # Este trecho precisa ser execultado apenas na primeira vez
        self.planilha = openpyxl.Workbook()
        self.planilha.create_sheet('Produtos')
        self.planilha.create_sheet('Cotação')
        headerProduto = ['Nome_Produto', 'Preço - R$', 'Data']
        headerCotacao = ['Dólar', 'Euro', 'Data']
        self.produto = self.planilha['Produtos']
        self.cotacao = self.planilha['Cotação']
        self.produto.append(headerProduto)
        self.cotacao.append(headerCotacao)
        self.planilha.save('produtos_cotacao.xlsx')
        # Até aqui -> E após isso ele pode ser comentado
         
        self.planilha = openpyxl.load_workbook('produtos_cotacao.xlsx')
        self.produto = self.planilha['Produtos']
        self.cotacao = self.planilha['Cotação']
        
        self.BuscarProdutos()
        self.ColetarDadosProdutos()
        self.BuscarCotacao()
        self.MontarArquivo()
       
        self.driver.quit()
        
    def BuscarProdutos(self):
        self.driver.get('https://www.mercadolivre.com.br/')
        time.sleep(5)
        inputBusca = self.driver.find_element(By.XPATH, "//*[name()='input'][@aria-label='Digite o que você quer encontrar']")
        inputBusca.click()
        inputBusca.send_keys("celular")
        inputBusca.send_keys(Keys.ENTER)

    def ColetarDadosProdutos(self):
        time.sleep(5)
        tagNomeProduto = self.driver.find_elements(By.XPATH, "//h2[@class='ui-search-item__title']")   
        self.listaNomeProduto = [x.text for x in tagNomeProduto]
        
        tagPrecoProduto = self.driver.find_elements(By.XPATH, "//div[@class='ui-search-price ui-search-price--size-medium shops__price']//div[@class='ui-search-price__second-line']//span[@class='price-tag-fraction']")
        self.listaPrecoProduto = [x.text for x in tagPrecoProduto]

    def BuscarCotacao(self):
        self.driver.get('https://www.google.com.br/')
        searchInput = self.driver.find_element(By.XPATH, "//*[name()='input'][@aria-label='Pesquisar']")
        searchInput.click()
        searchInput.send_keys("Cotação do dolar")
        searchInput.send_keys(Keys.ENTER)
        dolarElement = self.driver.find_element(By.XPATH, "//div[@data-name='Real brasileiro']//*[name()='input'][@aria-label='Campo do montante da moeda']")
        self.dolar = dolarElement.get_dom_attribute('value')
        
        self.driver.back()
        
        searchInput = self.driver.find_element(By.XPATH, "//*[name()='input'][@aria-label='Pesquisar']")
        searchInput.click()
        searchInput.send_keys("Cotação do euro")
        searchInput.send_keys(Keys.ENTER)
        euroElement = self.driver.find_element(By.XPATH, "//div[@data-name='Real brasileiro']//*[name()='input'][@aria-label='Campo do montante da moeda']")       
        self.euro = euroElement.get_dom_attribute('value')

        self.driver.close()
        
    def MontarArquivo(self):
        contadorCelula = 0 
        contadorLista = 0
        while contadorLista < len(self.listaNomeProduto):
            if self.produto[f'A{contadorCelula + 1}'].value != None:
                print(f"Célula já ocupada com {self.produto[f'A{contadorCelula + 1}']}")
                
                contadorCelula+=1
            else:
                self.produto[f'A{contadorCelula + 1}'].value = self.listaNomeProduto[contadorLista]
                self.produto[f'B{contadorCelula + 1}'].value = self.listaPrecoProduto[contadorLista]
                self.produto[f'C{contadorCelula + 1}'].value = date.today()
                
                contadorLista+=1
        
        contadorCtCelula = 0
        verificador = 0
        while verificador < 1:
            if self.cotacao[f'A{contadorCtCelula + 1}'].value != None:
                    print(f"Célula já ocupada com {self.cotacao[f'A{contadorCtCelula + 1}']}")
                    
                    contadorCtCelula+=1
            else:
                self.cotacao[f'A{contadorCtCelula + 1}'].value = self.dolar
                self.cotacao[f'B{contadorCtCelula + 1}'].value = self.euro
                self.cotacao[f'C{contadorCtCelula + 1}'].value = date.today()
                
                verificador+=1
        
        
        self.planilha.save('produtos_cotacao.xlsx')
        
autoML = automation()
autoML.Iniciar()