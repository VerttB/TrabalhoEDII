from flask import Flask,url_for,render_template,send_file,request
from flask_paginate import Pagination, get_page_parameter
import funcoesSite
import os
import dicionario

# inicializaçaõ

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/catalogo')
def catalogo():
    catalogo = dicionario.lerArquivo()  # Supondo que lerArquivo() é uma função que retorna o dicionário
    total = len(catalogo)
    pagina = request.args.get(get_page_parameter(), type=int, default=1)
    qtd_por_pagina = 15
    
    pagination_data = funcoesSite.get_pagina(catalogo, (pagina - 1) * qtd_por_pagina, qtd_por_pagina)
    paginacao = Pagination(page=pagina, total=total, qtd_per_page=qtd_por_pagina, per_page = qtd_por_pagina,search =False, format_number=True, aria_label='e')  
    return render_template('catalogo.html', paginacao = paginacao, catalogo = pagination_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/download')
def download():
    path = 'arquivos/catalago.json'
    return send_file(path, as_attachment=True)

# @app.route('/lerTexto', methods=['POST'])
# def lerTexto():
#     texto = request.form['texto']
#     return f"O texto digitado foi {texto}"

# @app.route('/index')
# def sobre3():
#     return render_template('index.html')

#exemplo no navegador
#http://localhost:5000/paginaEDII


#execução
app.run(debug = True)