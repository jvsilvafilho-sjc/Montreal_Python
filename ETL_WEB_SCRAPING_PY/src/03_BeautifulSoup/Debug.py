import requests #biblioteca requisições http
from bs4 import BeautifulSoup

response = requests.get("https://g1.globo.com/",verify=False)

'''
if  ( response.status_code == 200 ) :
    print('\n Header: ',response.headers) #Formato Dicionário do Python
    print ('\n content: ',response.content) #conteudo da resposta
else :
    print ('\n Falha!',response.status_code) #conteudo da resposta
'''

if  ( response.status_code == 200 ) :    
    content = response.content
    site = BeautifulSoup(content, 'html.parser') #convertendo o resultado da requisição para um objeto beautifulsoup
    #print(site.prettify())

    #elemento div classe
    noticia = site.find('div', attrs={'class': 'feed-post-body'})
    #print(noticia.prettify())

    # Titulo: Hacker disse à PF que Bolsonaro perguntou se ele poderia invadir urnas
    # Subtitulo: Preso de novo hoje, Walter Delgatti vazou conversas da Lava Jato em 2019
    #Titulo <a class="feed-post-link
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    print(titulo)
    print('\n Titulo: '+titulo.text)
    

    #Subtitulo
    subtitulo = noticia.find('a', attrs={'class': 'feed-post-body-title'})
    print(subtitulo)
    print('\n Subtitulo: '+subtitulo.text)

else :
    print ('\n Falha!',response.status_code) #conteudo da resposta