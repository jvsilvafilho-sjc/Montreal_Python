import pandas as pd #Uso de Dataframe
import requests #biblioteca requisições http
import xml.etree.ElementTree as ET #biblioteca para parsing xml
import ETL_dyn_manager_webscraping_services as obj_services
import os
import logging

from datetime import datetime
from pathlib import Path

'''
Instanciando Classes de Servico ou Apoio
'''
oGet_ClassApoio = obj_services.Get_ClassApoio() 


dthsdescfiles = datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss')
dtdescfiles = datetime.now().strftime('%Y%m%d')





'''
Atribuições de Variaveis do App.config
'''

'''
Diretorio de Trabalho
'''
if( os.environ['COMPUTERNAME']=='DAMOLANDIA' or os.environ['COMPUTERNAME']=='DIORAMA' or os.environ['COMPUTERNAME']=='CAMALAU'):    
    appCnnstring='DBconnectionString_Prod'
    origem_pathwork = 'D:/Metricas/'       
else:
    appCnnstring='DBconnectionString_Dev'
    origem_pathwork = 'C:/Metricas/'

origem_pathapps = origem_pathwork + 'Scripts/SQLServer/Release/'
origem_pathappETL = origem_pathapps + 'ETL_DYN_MANAGER_WEBSCRAPING/'
#oGet_ClassApoio.Criar_diretorios(origem_pathappETL)

#CRIANDO PATH DE LOG CASO NÃO EXISTA
pathlog = origem_pathappETL + 'Log'
oGet_ClassApoio.Criar_diretorios(pathlog)
filelog = pathlog + "/LOG_ETL_DYN_MANAGER_WEBSCRAPING_{}".format(datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss')) + ".log"

logfilename = oGet_ClassApoio.Configurar_Log(filelog)
logging.warning('(1), Arquivo LOG : "{}"...'.format(logfilename))

'''
Connection string
'''
origem_appconfigfilepath = Path(origem_pathapps+'App.config')
oGet_ClassApoio.Criar_diretorios(origem_appconfigfilepath)
#print(origem_appconfigfilepath)

appCnnstring = oGet_ClassApoio.AppConfig(str(origem_appconfigfilepath),appCnnstring)
#print(appCnnstring)




