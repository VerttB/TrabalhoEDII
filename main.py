from flask import Flask,url_for,render_template,send_file
import os

# inicializaçaõ

app = Flask(__name__, template_folder='templates', static_folder='static')

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

@app.route('/download')
def download():
    path = 'arquivos/teste.txt'
    return send_file(path, as_attachment=True)

# @app.route('/index')
# def sobre3():
#     return render_template('index.html')

#exemplo no navegador
#http://localhost:5000/paginaEDII


#execução
print("iae alysson")
app.run(debug = True)