from flask import Flask,url_for,render_template,send_file,request, session, jsonify, redirect, make_response
from flask_paginate import Pagination, get_page_parameter
import funcoesSite
import os
import dicionario


# inicializaçaõ
textoRecebido = ''
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'chave'

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/comprar' , methods=['GET', 'POST'])
def comprar():
    dados = request.json
    mensagem = dados['mensagem']
    print(mensagem)
    print(type(mensagem))
    dados_dict = dicionario.lerArquivo()
    print(type(dados_dict))
    dicionario.retirar_itens_comp(dados_dict, mensagem)
    return jsonify("Compra feita com sucesso")

@app.route('/adiciona', methods=['GET', 'POST'])
def adiciona_produto():
    dados = request.json
    mensagem = dados['mensagem']
    dados_dict = dicionario.lerArquivo()
    print(f"Comunicação com uscesso da mensagem {mensagem}")
    dicionario.adicionarProdutoatalogo(dados_dict, mensagem[0], int(mensagem[1]), float(mensagem[2]), mensagem[3])
    return jsonify('Produto adicionado com sucesso')

@app.route('/delete',  methods=['GET' ,'POST'])
def delete_produto():
    dados = request.json
    mensagem = dados['mensagem']
    print("Dados recebidos pelo Request JSON:", dados)
    print("Mensagem recebida do JavaScript:", mensagem)
    print(f'Tipo do dado {type(mensagem)}')
    dados_dict = dicionario.lerArquivo()
    dicionario.removerProduto(dados_dict, str(mensagem))
    return jsonify('Produto deletado com sucesso')


@app.route('/modifica', methods=['GET', 'POST'])
def modifica_produto():
    dados = request.json
    print(f"dados:{dados}")
    mensagem = dados['mensagem']
    print(f"Comunicação com uscesso da mensagem {mensagem}")
    dados_dict = dicionario.lerArquivo()
    dicionario.modificarProduto(dados_dict, mensagem[0], mensagem[1], int(mensagem[2]), float(mensagem[3]))
    return jsonify('Mensagem recebida')

@app.route('/catalogo', methods=['GET', 'POST'])
def catalogo():
    catalogoNovo = None
    mensagem = None
    nomeAprocurar = ''
    if request.method == 'POST':
        nomeAprocurar = request.form.get('texto', '')
        session['nomeAprocurar'] = nomeAprocurar
        print(f"Nome a procurar {nomeAprocurar}")
        mensagem = request.form.get('comunicacao', '')
        session['mensagem'] = mensagem
        print("Mensagem:" ,mensagem)
    else:
        nomeAprocurar = session.get('nomeAprocurar', '')
        mensagem = session.get('mensagem', '')
        
    if mensagem is not None and mensagem != "":
        print(type(mensagem))
        mensagens = mensagem.split("|")
    
        print(mensagens)
        catalogoNovo = funcoesSite.verificaOrdenacao(mensagens[0], mensagens[1])
        
    print("Nome a procurar:",nomeAprocurar)
    pagina = request.args.get(get_page_parameter(), type=int, default=1)
    qtd_por_pagina = 15
    paginacao, pagination_data = funcoesSite.criarPagina(nomeAprocurar, pagina, qtd_por_pagina, catalogoNovo, mensagens[0], mensagens[1])

    return render_template('catalogo.html', paginacao=paginacao, catalogo=pagination_data, nomeAprocurar=nomeAprocurar, mensagem = mensagem)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/download')
def download():    
    return send_file(funcoesSite.gerarDownload(), as_attachment=True)


@app.route('/produtos', methods=['GET', 'POST'])
def produtos():
    nomeAprocurar = ''
    if(request.method == 'POST'):
        nomeAprocurar = request.form.get('texto', '')
        session['nomeAprocurar'] = nomeAprocurar
    else:
        nomeAprocurar = session.get(nomeAprocurar)
        
    pagina = request.args.get(get_page_parameter(), type=int, default=1)
    qtd_por_pagina = 18
    paginacao,paginacao_data = funcoesSite.criarPagina(nomeAprocurar, pagina, qtd_por_pagina)
    return render_template('produtos.html', paginacao=paginacao, catalogo=paginacao_data, nomeAprocurar = nomeAprocurar)


app.run(debug = True)