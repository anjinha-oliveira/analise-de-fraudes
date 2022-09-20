from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def pagina_de_clientes():
    
    clientes = [
        {
            'nome': 'Luan Fonseca de Farias',
            'email': 'email@exemplo.com'
        }, 
        {
            'nome': 'Angela Lucia',
            'email': 'email@exemplo.com'
        }, 
        {
            'nome': 'Sandra de Sá',
            'email': 'email@exemplo.com'
        }, 
        {
            'nome': 'Rita de Cassia',
            'email': 'rita@exemplo.com'
        }
    ]
    return render_template('clientes.html', clientes=clientes)

@app.route("/transacoes")
def pagina_de_transacoes():
    return render_template('transacoes.html')



if __name__ == '__main__':
    app.run(debug=True)    