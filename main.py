from flask import Flask,url_for,render_template,send_file,request, session, jsonify
from flask_paginate import Pagination, get_page_parameter
import funcoesSite
import os
import dicionario

# inicializaçaõ
catalogo = {}
textoRecebido = ''
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'chave'

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/delete',  methods=['GET', 'POST'])
def delete():
    dados = request.json
    mensagem = dados['mensagem']
    print("Mensagem recebida do JavaScript:", mensagem)
    resposta = "Mensagem recebida com sucesso!"
    return jsonify(f'Vai se ferrar js {mensagem}')

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
    return send_file(path, as_attachment=True)




app.run(debug = True)

