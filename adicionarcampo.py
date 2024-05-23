import requests
from bs4 import BeautifulSoup
import dicionario
import urllib.request


def getLink(nome):
    text = requests.get(f'https://www.google.com/search?q=medicamento:{nome}&tbm=isch&tbs=isz:lt,islt:2mp').text
    html = BeautifulSoup(text, 'html.parser')
    print(nome)
    try:
        htmlTodo = html.find('img').find_next('img')
        if htmlTodo is not None:
            print("Retorno feito")
            return htmlTodo.get('src')
        else:
            return ""
        
    except AttributeError:
        print("Html n encontrado")
        return ""
    
dados = dicionario.lerArquivo()
for itens in dados:
    path = f"static/assets/imagensRemedios/{dados[itens]['nome']}.jpeg"
    try:
        urllib.request.urlretrieve(getLink(dados[itens]['nome']), path)
    except ValueError:
        print(f"Link do {dados[itens]['nome']} não obitido")

    dados[itens]['link'] = path
 
dicionario.atualizarArquivo(dados)
