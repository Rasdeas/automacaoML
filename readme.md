# Automação ML

Este é um projeto de automação e coleta de dados utilizando as bibliotecas Selenium para a automação e Openpyxl para criação e edição do arquivo.<br>

----
### Bibliotecas que precisam de instalação
~~~Terminal
pip install selenium
pip install openpyxl
~~~

----
### Webdriver
O webdriver utilizado foi o chromedriver, que deve ter a mesma versão do navegador Chrome utilizado.

O chromedriver pode ser baixado <a href="https://chromedriver.chromium.org/downloads" target="_blank" rel="noopener">aqui</a> neste site. <br>
Basta buscar a versão do seu navegador e baixar. <br>

Após baixar, basta por o execultável na mesma pasta onde o código da automação vai estar. <br>

----
### Sobre o código
Essa automação constiste em acessar o site do Mercado Livre, coletar alguns dados de um produto previamente selecionado e guardar esse dados. <br>

Após isso, ele consulta no Google a cotação do euro e do dólar e também guarda esses dados. <br>

Em seguida os dados que foram coletados, tanto do produto quando das cotações são utilizados para alimentar o arquivo que foi criado no começo do código.