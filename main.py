from flask import Flask,url_for,render_template,send_file,request, session, jsonify, redirect, make_response
from flask_paginate import Pagination, get_page_parameter
import funcoesSite
import os
import dicionario
import zipfile
import csv
import json

# inicializaçaõ
catalogo = dicionario.lerArquivo()
textoRecebido = ''
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'chave'

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/modifica', methods=['POST'])
def modifica_produto():
    dados = request.json
    mensagem = dados['mensagem']
    print(f'Mensagem {mensagem}')
    return jsonify('mensagem recebida')


@app.route('/delete',  methods=['POST'])
def delete_produto():
    dados = request.json
    mensagem = dados['mensagem']
    print("Mensagem recebida do JavaScript:", mensagem)
    print(f'Tipo do dado {type(mensagem)}')
    dados = dicionario.lerArquivo()
    dicionario.removerProduto(dados, str(mensagem))
    return jsonify('Mensagem recebida')

@app.route('/catalogo', methods=['GET', 'POST'])
def catalogo():
    catalogo = dicionario.lerArquivo()
    

    if(request.method == 'POST'):
        nomeAprocurar = request.form.get('texto', '')
        textoRecebido = request.form.get('texto_recebido', '')
        
        session['nomeAprocurar'] = nomeAprocurar
    else:
         nomeAprocurar = request.args.get('texto', '')
         nomeAprocurar = session.get('nomeAprocurar', '')

    if(nomeAprocurar is not None and nomeAprocurar != ''):
        catalogo = funcoesSite.filtrarDicionario(catalogo, nomeAprocurar)
    
    total = len(catalogo)
    pagina = request.args.get(get_page_parameter(), type=int, default=1)
    qtd_por_pagina = 15
    pagination_data = funcoesSite.Organizar_Dados_Dentro_Da_Pagina(catalogo, (pagina - 1) * qtd_por_pagina, qtd_por_pagina, pagina-1)
    
    paginacao = Pagination(page=pagina, total=total, qtd_per_page=qtd_por_pagina, per_page = qtd_por_pagina,search =False, format_number=True)  
    return render_template('catalogo.html', paginacao = paginacao, catalogo = pagination_data, nomeAprocurar = nomeAprocurar)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/download')
def download():
    path = 'arquivos/catalogo.json'
    csv_path = 'arquivos/catalogo_csv.csv'

    #Abre o arquivo JSON
    with open(path, 'r') as file:
        Arqui_JSON = json.load(file)

    #Transforma JSON em CSV

    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['id', 'nome', 'quantidade', 'preco', 'descricao']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for key, value in Arqui_JSON.items():
            writer.writerow({'id': key, 'nome': value['nome'], 'quantidade': value['quantidade'], 'preco': value['preco'], 'descricao': value['descricao']})

    #Gera arquivo ZIP

    zip_path = 'arquivos/catalogo.zip'
    
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(path, 'catalogo.json')
        zipf.write(csv_path, 'catalogo_csv.csv')
    
    return send_file(zip_path, as_attachment=True)



app.run(debug = True)