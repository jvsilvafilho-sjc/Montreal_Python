import requests

response = requests.get("https://www.walissonsilva.com/",verify=False)

print('Status Code: ',response.status_code) #status code 200/400/500

if  ( response.status_code == 200 ) :
    print('Header: ',response.headers) #Formato Dicionário do Python
    print ('\n',response.content) #conteudo da resposta
else :
    print ('\n Falha!',response.status_code) #conteudo da resposta