from flask import Flask,url_for,render_template,send_file,request, session, jsonify, redirect, make_response
from flask_paginate import Pagination, get_page_parameter
import funcoesSite
import os
import dicionario
import Grafo


# inicializaçaõ
mensagens = ['nome','crescemte','','']
textoRecebido = ''
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'chave'

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/comprar' , methods=['GET', 'POST'])
def comprar():
    dados = request.json
    print(dados)
    mensagem = dados['mensagem']
    dados_dict = dicionario.lerArquivo()
    dicionario.retirar_itens_comp(dados_dict, mensagem[0])
    return jsonify("Compra feita com sucesso")

@app.route('/frete' , methods=['GET', 'POST'])
def frete():
    dados = request.json
    print(dados)
    mensagem = dados['mensagem']
    print("Dados", mensagem)
    Grafo.criaGrafo(mensagem)
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
    print("Tamanho mensagem", len(mensagem))    

    if len(mensagem) == 0: 
        mensagem = "Nome |crescente| | "

    if mensagem is not None and mensagem != "":
        print(type(mensagem))
        mensagens = mensagem.split("|")
        print(mensagens)
        if len(mensagens) == 2:
            if len(mensagens) < 4:
                mensagens.extend([''] * (4 - len(mensagens)))
        catalogoNovo = funcoesSite.verificaOrdenacao(mensagens[0], mensagens[1],catalogoNovo, mensagens[2], mensagens[3])
        print(len(mensagens))
        #Isso aqui lida com a primeira execução do código que é quando a lista só tem 2 valores, pois nós usamos 4

        
    print("Nome a procurar:",nomeAprocurar)
    pagina = request.args.get(get_page_parameter(), type=int, default=1)
    qtd_por_pagina = 15
    paginacao, pagination_data = funcoesSite.criarPagina(nomeAprocurar, pagina, qtd_por_pagina, catalogoNovo, mensagens[0], mensagens[1], mensagens[2], mensagens[3])

    return render_template('catalogo.html', paginacao=paginacao, catalogo=pagination_data, nomeAprocurar=nomeAprocurar, mensagem = mensagem, valorMin = mensagens[2], valorMax = mensagens[3])


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
        print("Tamanho mensagem", len(mensagem))    

        if len(mensagem) == 0: 
            mensagem = "Nome |crescente| | "

        if mensagem is not None and mensagem != "":
            print(type(mensagem))
            mensagens = mensagem.split("|")
            print(mensagens)
            if len(mensagens) == 2:
                if len(mensagens) < 4:
                    mensagens.extend([''] * (4 - len(mensagens)))
            catalogoNovo = funcoesSite.verificaOrdenacao(mensagens[0], mensagens[1],catalogoNovo, mensagens[2], mensagens[3])
            print(len(mensagens))
            #Isso aqui lida com a primeira execução do código que é quando a lista só tem 2 valores, pois nós usamos 4

            
        print("Nome a procurar:",nomeAprocurar)
        pagina = request.args.get(get_page_parameter(), type=int, default=1)
        qtd_por_pagina = 21
        paginacao, pagination_data = funcoesSite.criarPagina(nomeAprocurar, pagina, qtd_por_pagina, catalogoNovo, mensagens[0], mensagens[1], mensagens[2], mensagens[3])

        return render_template('produtos.html', paginacao=paginacao, catalogo=pagination_data, nomeAprocurar=nomeAprocurar, mensagem = mensagem, valorMin = mensagens[2], valorMax = mensagens[3])
    


app.run(debug = True)