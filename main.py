from flask import Flask,url_for,render_template
import os

# inicializaçaõ
app = Flask(__name__)

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Configurar o diretório de templates para o diretório atual
app.jinja_loader.searchpath = diretorio_atual
# rotas
app.static_folder = 'static'

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/catalogo')
def catalogo():
    titulo= "Catalogo"
    catalogo = [
        {"nome": "Cadeira", "quantidade": 8},
        {"nome": "Cafeteira", "quantidade": 4},
        {"nome": "Mixer", "quantidade": 6},
    ]
    return render_template('catalogo.html', titulo = titulo, catalogo = catalogo)

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/index')
# def sobre3():
#     return render_template('index.html')

#exemplo no navegador
#http://localhost:5000/paginaEDII


#execução
app.run(debug = True)