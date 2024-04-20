from flask import Flask,url_for,render_template,send_file,request
import os
import dicionario

# inicializaçaõ

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/catalogo')
def catalogo():
    titulo= "Catalogo"
    catalogo = dicionario.lerArquivo()
    print(f"Esse é o catalogo: {catalogo}")
    #     {"nome": "Cadeira", "quantidade": 8, "preco" : 10},
    #     {"nome": "Cafeteira", "quantidade": 4, "preco" : 20},
    #     {"nome": "Mixer", "quantidade": 6, "preco" : 30},
    
    return render_template('catalogo.html', titulo = titulo, catalogo = catalogo)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/download')
def download():
    path = 'arquivos/teste.txt'
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
print(f"Esse é o catalogo: {catalogo}")
print("iae alysson")
app.run(debug = True)