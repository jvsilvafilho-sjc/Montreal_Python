import requests #biblioteca requisições http
from bs4 import BeautifulSoup
import pandas as pd #dataframe
from pathlib import Path

lista_noticias = [] #criando lista vazia

response = requests.get("https://g1.globo.com/",verify=False)

if  ( response.status_code == 200 ) :    
    content = response.content
    site = BeautifulSoup(content, 'html.parser') #convertendo o resultado da requisição para um objeto beautifulsoup
    #print(site.prettify())

    #elemento div classe
    noticias = site.findAll('div', attrs={'class': 'feed-post-body'})
    #print(noticias.prettify())
    
    
    for noticia in noticias:
        titulolink = noticia.find('a', attrs={'class': 'feed-post-link'})
        if (titulolink) :
            print('\nTitulo (link): '+titulolink.text)
            print('Link: '+titulolink['href'])  
            
        resumo = noticia.find('a', attrs={'class': 'feed-post-body-resumo'})        
        if  (resumo):
            print('Titulo (resumo): '+resumo.text)
            print('Link: '+resumo['href']+'\n')            

        subtitulotitle = noticia.find('a', attrs={'class': 'feed-post-body-title'})        
        #subtitulo = noticia.find('a', attrs={'class': 'gui-color-primary'})        
        if  (subtitulotitle):
            print('Subtitulo (title): '+subtitulotitle.text)
            print('Link: '+subtitulotitle['href']+'\n')
            lista_noticias.append([titulolink.text,subtitulotitle.text,titulolink['href']]) #armazenando linhas e colunas 
        else:
            lista_noticias.append([titulolink.text,'',titulolink['href']]) #armazenando linhas e colunas na lista

        subtituloprimary = noticia.find('a', attrs={'class': 'gui-color-primary'})        
        if  (subtituloprimary):
            print('Subtitulo (primary): '+subtituloprimary.text)
            print('Link: '+subtituloprimary['href']+'\n')
    
    #print(lista_noticias) 

    #criando Dataframe
    df_news = pd.DataFrame(lista_noticias,columns=['Titulo','Subtitulo','Link'])
    
    #print(df_news) 
    #print(df_news.describe())

    csvfilepath = Path('FilesCSV/noticiasg1.csv')
    excelfilepath = Path('FilesExcel/noticiasg1.xlsx')
    csvfilepath.parent.mkdir(parents=True, exist_ok=True) 
    excelfilepath.parent.mkdir(parents=True, exist_ok=True) 

    # Export to csv, codificação utf-8 , entre aspas e separador ','
    df_news.to_csv(csvfilepath, index=False, encoding='utf-8',sep=',')

    # Export to excel, codificação utf-8 , entre aspas e separador ','
    df_news.to_excel(excelfilepath, index=False )

        
else :
    print ('\n Falha!',response.status_code) #conteudo da resposta