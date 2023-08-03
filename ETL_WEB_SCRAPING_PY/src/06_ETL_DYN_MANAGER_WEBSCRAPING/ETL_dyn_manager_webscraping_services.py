import os
import logging
import boto3
import pandas as pd
import pyodbc

import xml.etree.ElementTree as ET #biblioteca para parsing xml

class Get_ClassApoio:

    #CONFIGURAR ARQUIVO DE LOG     
    def Configurar_Log(self,logfilename):
        log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
        #logger = logging.getLogger('root')
        logging.basicConfig ( 
                    filename=logfilename,
                    filemode='a',
                    level=logging.INFO,
                    format=log_format )
        #logger = logging.getLogger('root')
        return logfilename

    #LEITURA APP.CONFIG
    def AppConfig(self,origem_appconfigfilepath,tagvalue):
        
        tagvalue = "./appSettings/add[@key='"+tagvalue+"']"
        tree = ET.parse(origem_appconfigfilepath)
        root = tree.getroot()        
        retorno = None
        
        try:

            '''
            <?xml version="1.0" encoding="utf-8" ?>
            <configuration>
                <appSettings>	
                    <add key="DBconnectionString_Prod" value="Driver={ODBC Driver 17 for SQL Server};Server=10.200.163.14,1433;UID=adm-antonioalmeida;PWD=gn$!2-hu78;Database=Dbpslmprodespdc;Application Name=SLM-Prodesp;"/>

            for tag_add in root.iter('add'):
            print(tag_add.attrib)

            for tag_add in root.findall("./appSettings/add[@key='DBconnectionString_Prod']"):
                print((tag_add.attrib)['value'])
            '''

            if (tagvalue):
                for tag_add in root.findall(tagvalue):            
                    retorno = (tag_add.attrib)['value']

        except OSError as err:
            print("OS error:", err)
        
        except ValueError:
            print("Could not convert data to an integer.")
        
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

        return retorno 
    
    #CRIAR TODA A ESTRUTURA DE DIRETORIOS 
    def Criar_diretorios(self,dest_csvfilepath):
        #print(dest_csvfilepath)

        '''
        dest_csvfilepath.parent.mkdir(parents=True, exist_ok=True) 
        dest_csvfilepath.parent.mkdir(parents=True, exist_ok=True) 
        '''

        if not os.path.exists(dest_csvfilepath):            
            os.makedirs(dest_csvfilepath) 
            retorno = os.path.dirname
        else:
            retorno = dest_csvfilepath #os.path.dirname      
        return retorno  

    #APLICAR PROXY, CASO ESTEJA EM ALGUM DOS SERVIDORES
    def Aplicar_Proxy(self,appurlproxy):
        if( os.environ['COMPUTERNAME']=='DAMOLANDIA' or os.environ['COMPUTERNAME']=='DIORAMA' or os.environ['COMPUTERNAME']=='CAMALAU' ):
            os.environ["HTTPS_PROXY"] = appurlproxy
            os.environ["HTTP_PROXY" ] = appurlproxy
            os.environ["https_proxy"] = appurlproxy
            os.environ["http_proxy" ] = appurlproxy
            logging.warning('(), Proxy Aplicado : "{}"...'.format(appurlproxy))
        else:
            logging.warning('(), Proxy: "{}" , Sem necessidade de ser Aplicado Host:  "{}"...'.format(appurlproxy,os.environ['COMPUTERNAME']))
        
