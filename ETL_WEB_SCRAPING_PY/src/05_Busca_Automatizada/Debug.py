import requests #Requisições
from bs4 import BeautifulSoup #Converter html para objetos


url_base = "https://lista.mercadolivre.com.br/"

produto_nome = input('Qual produto você deseja? ')

#mi band 5
#print(url_base+produto_nome)

response = requests.get(url_base + produto_nome,verify=False)
#print(response.text) 

if  ( response.status_code == 200 ) : 
    site = BeautifulSoup(response.text,'html.parser')
    print(site.prettify()) 
    
    produto = site.find('a', attrs={'class': 'andes-card ui-search-result shops__cardStyles ui-search-result--core andes-card--flat andes-card--padding-16'})
    
    if (produto) :
        print(produto.prettify()) 
    else :
        print('\n Nok')
        

else :
    print ('\n Falha!',response.status_code) #conteudo da resposta

